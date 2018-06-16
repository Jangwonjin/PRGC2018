import numpy as np
import cv2
from tqdm import tqdm

class reload(object):
    
    def __init__(self):
        tr_f_d = open('annotations/train_list.txt', 'r')
        tr_f_l = open('annotations/train_labels.txt', 'r')
        te_f_d = open('annotations/test_list.txt', 'r')
        te_f_l = open('annotations/test_labels.txt', 'r')
        
        tr_lb = tr_f_l.readlines()
        tr_img_paths = tr_f_d.readlines()
        te_lb = te_f_l.readlines()
        te_img_paths = te_f_d.readlines()
        
        train_num = int(len(tr_img_paths)/64)
        test_num = int(len(te_img_paths)/64)
        
        self.train_dataset = np.zeros((train_num,64,64,64), dtype=np.float64)
        self.train_labels = np.zeros((train_num,1), dtype=np.int32)
        
        self.test_dataset = np.zeros((test_num,64,64,64), dtype=np.float64)
        self.test_labels = np.zeros((test_num,1), dtype=np.int32)

        with tqdm(total = train_num+test_num) as pbar:
            pbar.set_description("[ Load Dataset ]")
            for i in range(train_num):
                for j in range(64):
                    self.train_dataset[i][j]=cv2.imread(tr_img_paths[j + i*64][:-1], cv2.IMREAD_GRAYSCALE)
                self.train_labels[i] = tr_lb[i*64]
                pbar.update(1)
            tr_f_d.close()
            tr_f_l.close()

            for i in range(test_num):
                for j in range(64):
                    self.test_dataset[i][j]=cv2.imread(te_img_paths[j + i*64][:-1], cv2.IMREAD_GRAYSCALE)
                self.test_labels[i] = te_lb[i*64]
                pbar.update(1)
            te_f_d.close()
            te_f_l.close()