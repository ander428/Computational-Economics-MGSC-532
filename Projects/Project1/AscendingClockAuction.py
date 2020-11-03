''' Improvements
renamed monteCarloSimulation function to match naming convention
added more comments to be more clear on code
moved static variables to after function definitions
'''

import random
import numpy as np
import matplotlib.pyplot as plt

# this runs a single clock auction given given 
#   number of buyers, clock increment, and optionally reserve price
def ascending_clock_auction(num_buyers, clock_incr, reserve_price=None):
    buyers = {}
    for i in range(num_buyers):
        buyers[f"Buyer {i+1}"] = random.choice(range(val_min, val_max, val_incr))

    clock_price = 0
    last_buyer_dropped = {}
    winner_val = 0

    # end condition 1 - reserve price >= clock price
    while True:
        clock_price += clock_incr
        buyers, last_buyer_dropped = check_buyers(buyers, last_buyer_dropped, clock_price)

        # end condition 3 - clock price < reserve_price with a winner
        # checks if reserve price is provided (defaults to None)
        if reserve_price and len(buyers) == 0 and clock_price < reserve_price:
            return 0
        
        # end condition 2 - one or less buyers
        elif len(buyers) == 0:
            winner_val = random.choice(list(last_buyer_dropped.values()))
            break
        elif len(buyers) == 1:
            winner_val = list(buyers.values())[0]
            break

    posted_price = clock_price - clock_incr
    return posted_price

# helper function to check if a buyer will drop from an auction 
# given the list of buyers and clock price
# note: will also store the buyer in a new list if the buyer drops
def check_buyers(buyers, last_buyer_dropped, clock_price):
    for buyer in list(buyers.keys()):
        if buyer in buyers.keys() and buyers[buyer] < clock_price:
            if len(last_buyer_dropped) == 0 or not buyers[buyer] in last_buyer_dropped.values():
                last_buyer_dropped.clear()
            last_buyer_dropped[buyer] = buyers[buyer]
            del buyers[buyer]
            # print(last_buyer_dropped)
    return buyers, last_buyer_dropped

# a print function that neatly prints the results of an auction simulation
def print_results(num_buyers, clock_incr, avg_revenue, reserve_price=None):
    print("Number of buyers:", num_buyers)
    print("Clock Increment:", clock_incr)
    if reserve_price:
        print(f"Reserve Price: ${reserve_price}")
    print(f"Average Revenue: ${round(avg_revenue, 2)}")
    print()

# runs monte carlo simulation of ascending clock auctions
def monte_carlo_sim(num_buyers, clock_incr, reserve_price=None):
    revenue = 0
    for _ in range(trials):
        revenue += ascending_clock_auction(num_buyers, clock_incr, reserve_price)

    print_results(num_buyers, clock_incr, revenue/trials, reserve_price)
    return revenue/trials

# inputs
val_max = 100
val_min = 0
val_incr = 5
trials = 100000

# A. What is the expected revenue if there are 5 buyers and the clock increment is $1?
print("1a)")
monte_carlo_sim(num_buyers=5, clock_incr=1)
print("The expected revenue for 5 buyers and a $1 clock increment is around $64.23")
print()

# B. What is the expected revenue if there are 5 buyers and the clock increment is $10? 
#  How did the increment affect the expected revenue and why does it have that effect?
print("1b)")
monte_carlo_sim(num_buyers=5, clock_incr=10)
print("The expected revenue for 5 buyers and a $10 clock increment is around $61.70.")
print("The average revenue is lower. This could be because when a buyer wins, the price paid is a posted price which is " +
        "one clock increment less than the clock price. Having a higher clock increment means that the posted price the buyer pays" + 
        "will have a larger gap from the clock price meaning they pay less on average." )
print()


# C. What is the expected revenue if there are 20 buyers with a clock increment of $1? 
#   Compare with item (a) and explain the difference.
print("1c)")
monte_carlo_sim(num_buyers=20, clock_incr=1)
print("The expected revenue for 20 buyers and a $1 clock increment is around $87.95")
print("The average revenue is way higher as the probability of a buyer valuing the item is much larger with more buyers. " +
        "This means that there will more often be competition at higher prices.")
print()

# D. What reserve price should the seller choose (which price generates the most revenue)?
#  Provide an illustration that supports your result.

print("1d)")
reserve_price_results = [(monte_carlo_sim(5, 5, reserve_price)) for reserve_price in range(0, 100, 5)]
print(reserve_price_results)

plt.bar(range(0, 100, 5), reserve_price_results)
plt.xlabel("Reserve Price")
plt.ylabel("Average Revenue")
plt.show()

# the plot shows that the reserve price negatively affects revenue after $40. Anything less than 
# $40 on average returns a very similar revenue with the $0 reserve price having the highest revenue
