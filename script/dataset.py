import torch
from torch.utils.data import Dataset
from PIL import Image
import os


class CADataset(Dataset):

    def __init__(self, data_dir, augmentation=None):
        super().__init__()
        self.file_list = os.listdir(data_dir)

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, index):
        
        return super().__getitem__(index)



