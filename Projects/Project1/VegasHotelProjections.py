import random

# forcasting model
def get_profit(T, hotels):
    profit = 0
    for year in range(T):
        profit += (750 + 50*(year+1)) / (hotels[year]+1)
    return profit

def get_construction_profile(T, m):
    profile = []
    construction_time = m-1
    constructing = False
    count = 0

    for t in range(T):
        if not constructing and random.randint(0, 1) == 1:
            constructing = True
        elif construction_time == 0:
            construction_time = m-1
            constructing = False
            count += 1
        if constructing:
            construction_time -= 1
        profile.append(count)
        
    return profile


T = 10
m = 2
hotels = [0,1,1,2,2,2,3,3,3,3]
profits = []
trials = 100000

for _ in range(trials):
    profile = get_construction_profile(T, m)
    profits.append(get_profit(T, profile))

print(f"With hotels taking {m} years to construct,")
print(f"Profit over {T} years is expected to be approximately ${round(sum(profits) / trials, 2)}.")

