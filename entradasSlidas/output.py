v = "otro texto"
n = 10
print("Un texto",v,"y un número",n)

c = "Un texto '{}' y un número '{}'".format(v,n)

print(c)

print("Un texto '{1}' y un número '{0}'".format(v, n))

print("Un texto '{v}' y un número '{n}'".format(n=n, v=v))

print("{v},{v},{v}".format(v=v))

print("{:>30}".format("palabra"))

print("{:30}".format("palabra"))

print("{:^30}".format("palabra"))

print("{:.5}".format("palabra"))

print("{:>30.3}".format("palabra"))

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))