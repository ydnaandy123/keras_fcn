import numpy as np
import keras
import dataset_parser
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD

cityscapesParser = dataset_parser.CityscapesParser('./dataset/CITYSCAPES')
print(cityscapesParser.)