import random
import statistics

trials = 1000
samples = 1000
b = 1
a = 0
areas = []
areas_antithetical = []

def cube(x):
    return x**3

for _ in range(trials):
    area = 0
    for i in range(samples):
        area += (b-a)*cube(random.random())
    area = area / samples
    areas.append(area)

print(statistics.mean(areas))
print(statistics.variance(areas))

for _ in range(trials):
    area = 0
    for i in range(samples):
        if i <= samples/2:
            area += (b-a)*cube(random.uniform(a, (b-a)/2))
        else:
            area += (b-a)*cube(random.uniform((b-a)/2, b))
        area = area / samples
        areas_antithetical.append(area)


print(statistics.mean(areas_antithetical))
print(statistics.variance(areas_antithetical))
