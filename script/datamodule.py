import pytorch_lightning as pl
import os

class CADataset(pl.LightningDataModule):

    def __init__(self, data_dir, num_workers):
        super().__init__()
        self.data_dir = data_dir
        self.num_workers = num_workers

    def setup(self, stage):

        files = os.listdir(self.data_dir)

        return super().setup(stage)
