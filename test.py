import numpy as np 

a = np.array(( [1,2,3],[4,5,6] ))
b = np.resize(a,(3,2))
print(a.shape)
print(a)
print(b)

b = np.arrange(10,10,20)
print(b)
print(b.ndim)
b = np.arrange(20)
print(b)
b = b.reshape(2,2,5)