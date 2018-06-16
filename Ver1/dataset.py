import numpy as np
import pandas as pd
import wget, os
from tqdm import tqdm

class download:
    def __init__(self,csv_file,DATASET_ROOT="/dataset"):
        dataset_path = os.getcwd()+DATASET_ROOT
        if not os.path.isdir(dataset_path):
            os.mkdir(dataset_path)
        
        dataset = "https://neurovault.org/media/images/503/"
        csv_file = pd.read_csv(csv_file)

        with tqdm(total = len(csv_file)) as pbar:
            pbar.set_description("[Download PINES Dataset]")
            for filename in csv_file.Files:
                wget.download(dataset+filename, dataset_path)
                pbar.update(1)