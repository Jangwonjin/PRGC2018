import os, glob
import numpy as np

def get_filename(fulllocation):
    i=1
    while True:
        if fulllocation[-i] is not "/":i += 1
        else:
            name=fulllocation[-(i-1):]
            break
    return name

def explore_dir(dir,extension,count=0):
    if count==0:
        global n_dir, n_file, filenames, filelocations
        n_dir=n_file=0
        filenames=filelocations=np.array([])
    for img_path in sorted(glob.glob(os.path.join(dir,'*.'+extension))): # 가져올 파일 명시
        if os.path.isdir(img_path):
            n_dir +=1
            explore_dir(img_path,count+1)
        elif os.path.isfile(img_path):
            n_file += 1
            loc=np.array([img_path])
            name=np.array([get_filename(img_path)])
            filelocations=np.concatenate((filelocations, loc), axis=0)
            filenames=np.concatenate((filenames, name), axis=0)
    return np.array([filenames,filelocations])

def detect(img, num_channel=3, threshold=0):
    x_axis, y_axis=img.shape[:2]
    coors=[0,0,0,0,0] # x1,x2,y1,y2,exist
    
    for i in range(x_axis) :
        for j in range(y_axis) :
            if num_channel == 3: # RGB
                detected = True if img[i][j][0] > threshold or img[i][j][1] > threshold or img[i][j][2] > threshold else False
            elif num_channel == 1:
                detected = True if img[i][j] > threshold else False
            else :
                raise ValueError("num_channel should be 1 or 3.")
            
            if detected:    
                coors[4] =1 # exist
                if coors[0] == 0 and coors[2] ==0:
                    coors[0] = coors[1] = i
                    coors[2] = coors[3] = j
                    
                elif coors[0]<i and coors[1] < i: 
                    coors[1] = i
                elif coors[1]>i :
                    coors[0] = i
                    
                elif coors[2]>j and coors[3] > j: 
                    coors[2] = j
                elif coors[3]<j :
                    coors[3] = j
    return coors

def apply_3D_bbox(img):
    # Get valid boxes
    bbox_coors = list()
    for i in range(len(img)):
        bbox_coors.append(detect(img[i], num_channel=1))
    bbox_coors=np.array(bbox_coors)

    # Get X-axis indices
    x1 = 0
    x2 = 0
    status = 0
    if min(bbox_coors[:,4])==1:
        x2 = len(bbox_coors)
    else :
        for i in range(len(bbox_coors)):
            if status != bbox_coors[i,4]:
                if x1==0 and bbox_coors[i,4]==1:
                    x1=i
                if x2==0 and bbox_coors[i,4]==0:
                    x2=i-1
                status = bbox_coors[i,4]
        if status!=0:
            x2=len(bbox_coors)
    
    # Get Y-axis and Z-axis indices
    y1 = min(bbox_coors[x1:x2,0])
    y2 = max(bbox_coors[x1:x2,1])
    z1 = min(bbox_coors[x1:x2,2])
    z2 = max(bbox_coors[x1:x2,3])
    
    # Get 3D bbox data
    data = np.zeros((x2-x1, y2-y1, z2-z1), dtype=np.float64)
    for i in range(x2-x1):
        data[i] = img[x1+i, y1:y2, z1:z2]
        
    return data

def MinMaxScaler(data):
    numerator = data - np.min(data,0)
    denominator = np.max(data,0) - np.min(data,0)
    return numerator/ (denominator + 1e-8)

def project(dataset, axis):
    if axis=="x" :
        axis=1
    elif axis=="y" :
        axis=2
        dataset = dataset.transpose(0,2,1,3)
    elif axis=="z" :
        axis=3
        dataset = dataset.transpose(0,3,1,2)
    else : raise ValueError("axis should be 'x' or 'y' or 'z'.")
    projected_dataset = np.zeros(dataset.shape[:3], dtype=np.float64)
    for i in range(len(dataset)):
        for j in range(dataset.shape[axis]):
            projected_dataset[i] += dataset[i,j]
    return projected_dataset