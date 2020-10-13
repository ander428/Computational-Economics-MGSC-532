import random
from matplotlib import pyplot as plt

# calculates the probability of heads given a certain number of samples


def prob_of_heads(samples):
    head_count = 0
    for i in range(samples):
        head_count += random.randint(0, 1)
    return head_count / samples


small_sample_estimates = []
large_sample_estimates = []
for i in range(1000):
    small_sample_estimates.append(prob_of_heads(8))
    large_sample_estimates.append(prob_of_heads(1000))

plt.hist(small_sample_estimates)
plt.hist(large_sample_estimates)

plt.show()
