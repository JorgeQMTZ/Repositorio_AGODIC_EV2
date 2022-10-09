import numpy as np

np.random.seed(12345)

nsteps=50
draws=np.random.randint(0,2,size=nsteps)
steps=np.where(draws>0,1,-1)

walk=steps.cumsum()
print(walk)