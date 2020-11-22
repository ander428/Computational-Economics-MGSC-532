# potential solution  [0,1,0,0,0,1,1,1,0]

import random

num_items = 10
max_weight = 2

values = [random.uniform(1,20) for _ in range(num_items)]
weights = [random.random() for _ in range(num_items)]

solution = []
for _ in range(num_items):
    solution.append(random.randint(0, 1))


def knapsack_fitness(solution, values, weights, max_weight):
    weighted_weights = []
    expected_value = []
    for i in range(num_items):
        weighted_weights.append(solution[i] * weights[i])
    weight = sum(weighted_weights)
    if weight > max_weight:
        return 0
    else:
        for j in range(num_items):
            expected_value.append(solution[j] * values[j])
        total_value = sum(expected_value)
        return total_value

#! generate population

# genetic algorithm params
population_size = 10
num_children = 6
mutate_prob = 0.05


def random_knapsack_solution(num_items):
    return [random.randint(0, 1) for _ in range(num_items)]


def generate_knapsack_population(num_items, population_size):
    population = [random_knapsack_solution(
        num_items) for _ in range(population_size)]
    return population

#! select parents and children

def generate_children(population, num_children, mutate_prob):
    children = []
    for i in range(num_children):
        split = random.randint(0, population_size-1)
        p1, p2 = random.sample(population, 2)

        c1 = p1[:split] + p2[split:]
        children.append(mutate_knapsack(c1, mutate_prob))

    return children

#! mutate children

# hit enter to edit
def mutate_knapsack(solution, prob):
  for i in range(len(solution)):
    if random.randint(0, 100) < prob*100:
      solution[i] = solution[i] ^ 1  # xor with True to flip
  return solution

#! Survival for next population

def tournament_survival(new_population, population_size):

    trimmed_population = []
    for i in range(population_size):
        individual = new_population[random.randint(0, population_size-1)]
        individual2 = new_population[random.randint(0, population_size-1)]

        # fitness func undefined so far
        if knapsack_fitness(individual, values, weights, max_weight) >= knapsack_fitness(individual2, values, weights, max_weight):
            trimmed_population.append(individual)
        else:
            trimmed_population.append(individual2)

    return trimmed_population
# select two and compare fitnesses, then select best individual among those 2 individuals to be parents.

#! run the simulation
initial_population = generate_knapsack_population(num_items, population_size)

children = generate_children(initial_population, num_children, mutate_prob)
new_population = initial_population + children
new_population = tournament_survival(new_population, population_size)

for _ in range(10):
  new_population = tournament_survival(new_population, population_size)

print(new_population)