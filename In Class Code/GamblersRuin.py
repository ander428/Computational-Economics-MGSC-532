import random

trials = 100000
budget = 1000
bet = 100
goal = 2 * budget
probability = 18/37

def gamblers_ruin(budget, bet, goal, probability):
    current_budget = budget
    num_bets = 0
    while current_budget > 0 and current_budget < goal:
        num_bets += 1
        if random.random() < probability:
            current_budget += bet
        else:
            current_budget -= bet 
    return (num_bets, current_budget)


results = [gamblers_ruin(budget, bet, goal, probability) for _ in range(trials)]

def probability_of_goal(results):
    return sum([result[1] > 0 for result in results]) / len(results)

def expected_profit(results):
    return sum([result[1] for result in results]) / len(results)

def extreme_runs(results):
    bet_counts = [result[0] for result in results]
    return (min(bet_counts), max(bet_counts))

print(probability_of_goal(results))
print(expected_profit(results))
print(probability_of_goal(results) * goal)

import numpy as np

def bet_percentiles(results, percentile):
    bet_counts = [result[0] for result in results]
    return np.percentile(bet_counts, percentile)


print(extreme_runs(results))
print(bet_percentiles(results, 95))