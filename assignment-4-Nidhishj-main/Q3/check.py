import numpy as np
from select_best_binary_split import select_best_binary_split

N = 5
F = 1
prng = np.random.RandomState(0)
# x_N1 = np.asarray([0.0, 1.0, 2.0, 3.0, 4.0, 5.0]).reshape((6,1))
x_NF = np.asarray([3.0, 3.0, 3.0, 3.0, 3.0]).reshape((5,1))
y_N  = np.asarray([0.0, 0.0, 0.0, 1.0, 1.0])
feat_id, thresh_val, _, _, _, _ = select_best_binary_split(x_NF, y_N)
print(feat_id is None)
