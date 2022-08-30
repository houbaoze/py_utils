import numpy as np
import time
import math
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from collections import namedtuple

def file2array(path,delimiter = ' '):
  fp = open(path,'r',encoding='utf-8')
  string = fp.read()
  fp.close()
  row_list = string.splitlines()
  data_list = [[float(i) for i in row.strip().split(delimiter)] for row in row_list]
  return np.array(data_list)

