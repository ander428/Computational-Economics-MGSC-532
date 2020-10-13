# integrate x^2 between 1 and 4
# (1/3 4^3 - 1/3 1^3)

import random

count = 0
trials = 100000
estimates = []
for i in range(trials):
    x = random.uniform(1,4)
    estimates.append(x**2)

print((4-1) / trials*sum(estimates))