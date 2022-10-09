import numpy as np

data13_1=np.arange(9).reshape(3,3)
data13_2=np.arange(9,18).reshape(3,3)
print(data13_1)
print(data13_2)
print("-----------")
print(np.multiply(data13_1, data13_2))

print("-------------")
print(np.linalg.det(data13_1))
print(np.linalg.det(data13_2))