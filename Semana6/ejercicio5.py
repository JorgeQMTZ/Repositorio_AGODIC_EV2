import numpy as np

data4=np.arange(64).reshape(4,4,4)
print(data4)

print(data4.dtype.name)
data4.dtype="float32"
print("---")
data4.dtype.name
print(data4)