import numpy as np
import cv2
from tqdm import tqdm

class reload(object):
    
    def __init__(self):
        
        self.train_x_dataset = list()
        self.train_y_dataset = list()
        self.train_z_dataset = list()
        self.test_x_dataset = list()
        self.test_y_dataset = list()
        self.test_z_dataset = list()
        
        self.train_x_labels = list()
        self.train_y_labels = list()
        self.train_z_labels = list()
        self.test_x_labels = list()
        self.test_y_labels = list()
        self.test_z_labels = list()

        num_img = sum(len(open("annotations/"+filename+"_list.txt", 'r').readlines()) for filename in {"train_x","train_y","train_z","test_x","test_y","test_z"})
        with tqdm(total = num_img) as pbar:
            pbar.set_description("[ Load Dataset ]")
            
            f_d = open('annotations/train_x_list.txt', 'r')
            f_l = open('annotations/train_x_labels.txt', 'r')
            lb = f_l.readlines()
            for i, path in enumerate(f_d.readlines()):
                self.train_x_dataset.append(cv2.imread(path[:-1], cv2.IMREAD_GRAYSCALE))
                self.train_x_labels.append(lb[i][:-1])
                pbar.update(1)
            f_d.close()
            f_l.close()

            f_d = open('annotations/train_y_list.txt', 'r')
            f_l = open('annotations/train_y_labels.txt', 'r')
            lb = f_l.readlines()
            for i, path in enumerate(f_d.readlines()):
                self.train_y_dataset.append(cv2.imread(path[:-1], cv2.IMREAD_GRAYSCALE))
                self.train_y_labels.append(lb[i][:-1])
                pbar.update(1)
            f_d.close()
            f_l.close()

            f_d = open('annotations/train_z_list.txt', 'r')
            f_l = open('annotations/train_z_labels.txt', 'r')
            lb = f_l.readlines()
            for i, path in enumerate(f_d.readlines()):
                self.train_z_dataset.append(cv2.imread(path[:-1], cv2.IMREAD_GRAYSCALE))
                self.train_z_labels.append(lb[i][:-1])
                pbar.update(1)
            f_d.close()
            f_l.close()

            f_d = open('annotations/test_x_list.txt', 'r')
            f_l = open('annotations/test_x_labels.txt', 'r')
            lb = f_l.readlines()
            for i, path in enumerate(f_d.readlines()):
                self.test_x_dataset.append(cv2.imread(path[:-1], cv2.IMREAD_GRAYSCALE))
                self.test_x_labels.append(lb[i][:-1])
                pbar.update(1)
            f_d.close()
            f_l.close()

            f_d = open('annotations/test_y_list.txt', 'r')
            f_l = open('annotations/test_y_labels.txt', 'r')
            lb = f_l.readlines()
            for i, path in enumerate(f_d.readlines()):
                self.test_y_dataset.append(cv2.imread(path[:-1], cv2.IMREAD_GRAYSCALE))
                self.test_y_labels.append(lb[i][:-1])
                pbar.update(1)
            f_d.close()
            f_l.close()

            f_d = open('annotations/test_z_list.txt', 'r')
            f_l = open('annotations/test_z_labels.txt', 'r')
            lb = f_l.readlines()
            for i, path in enumerate(f_d.readlines()):
                self.test_z_dataset.append(cv2.imread(path[:-1], cv2.IMREAD_GRAYSCALE))
                self.test_z_labels.append(lb[i][:-1])
                pbar.update(1)
            f_d.close()
            f_l.close()
