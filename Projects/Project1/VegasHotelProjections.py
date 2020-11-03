
''' Improvements
renamed constructing to is_constructing to clarify it holds a boolean value
shortened get_construction_profile to still be clear but more concise
added comments for clarity
fixed logical error in line 37, should be an elif not if
'''

import random

# forcasts profit given a construction profile
# T - number of years we are forcasting
def get_profit(T, hotels):
    profit = 0
    for year in range(T):
        profit += (750 + 50*(year+1)) / (hotels[year]+1)
    return profit

# generate a profile of when hotels will be constructed
def get_profile(T, m):
    profile = []
    construction_time = m-1 # the length it takes to build a hotel
    is_constructing = False
    count = 0

    # for every year, decided if hotel construction should start
    for t in range(T):
        # if not currently constructing, randomly choose to construct or not
        if not is_constructing and random.randint(0, 1) == 1:
            is_constructing = True
        # finished constructing
        elif construction_time == 0:
            construction_time = m-1
            is_constructing = False
            count += 1
        # if constructing, then count current year towards construction
        elif is_constructing:
            construction_time -= 1
        profile.append(count)
        
    return profile


T = 10
m = 2
hotels = [0,1,1,2,2,2,3,3,3,3]
profits = []
trials = 100000

for _ in range(trials):
    profile = get_profile(T, m)
    profits.append(get_profit(T, profile))

print(f"With hotels taking {m} years to construct,")
print(f"Profit over {T} years is expected to be approximately ${round(sum(profits) / trials, 2)}.")

