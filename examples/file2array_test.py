import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from file2array import file2array

a = file2array('test.txt')
