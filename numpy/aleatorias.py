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

print(np.random.randint(10, size=[3, 2]))
print(spaceChart)

print(np.random.randint(-10, 10, size=[3, 2]))
print(spaceChart)

print(np.random.normal(size=20))
print(spaceChart)

arr = np.arange(10)
print(spaceChart)
print(arr)
print(spaceChart)

np.random.shuffle(arr)
print(arr)
print(spaceChart)

print(np.random.permutation(15))
print(spaceChart)

