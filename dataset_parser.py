import os
from glob import glob

class CityscapesParser:
    def __init__(self, dataset_dir)
        img_dir = dataset_dir + '/leftImg8bit_trainvaltest/leftImg8bit'
        img_training_dir = img_dir + '/train'
        img_testing_dir = img_dir + '/val'

        self.img_testing_path = []
        for folder in os.listdir(img_testing_dir):
            path = os.path.join(img_testing_dir, folder, "*_leftImg8bit.png")
            self.img_testing_path.extend(glob(path))

