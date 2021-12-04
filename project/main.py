import tensorflow as tf
import numpy as np


D = np.array([10,20,30,40,50,60]).reshape(3,2)

print(D[0:-1, 0:2])