import numpy as np

spaceChart = '---------------'

print(np.random.rand())
print(spaceChart)

print(np.random.rand(4))
print(spaceChart)

print(np.random.rand(4, 2))
print(spaceChart)

print(np.random.uniform(10, size=[2, 2, 2]))
print(spaceChart)

print(np.random.uniform(-10, 10, size=[2, 2, 2, 2]))
print(spaceChart)

print(np.random.randint(10))
print(spaceChart)