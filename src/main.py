from PIL import Image
from torch.autograd import Variable
from torch.cuda import FloatTensor
import torch.nn as nn

import numpy as np
import os
import io

from math import *
import time

class DarkNet:
    pass

class Object:
    def __init__(self):
        self.pos_x = -1
        self.pos_y = -1
        self.attention_ratio = -1
        self.image2d_weight = -1
        self.image2d_height = -1

class Car(Object):
    pass

class Human(Object):
    pass

class Server:
    pass
