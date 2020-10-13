import random

buyers = 5
value_bonds = [0, 100]
trials = 100000


revenue = []
for _ in range(trials):
    values = [random.randrange(value_bonds[0], value_bonds[1]) for _ in range(buyers)]
    revenue.append(sorted(values)[-2])

print(sum(revenue) / trials)