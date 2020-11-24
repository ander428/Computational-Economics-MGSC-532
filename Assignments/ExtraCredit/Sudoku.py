import os
import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp


### helper functions ###

# prints 9 x 9 dataframe as sudoku
def print_sudoku(df):
    data = df.copy()

    for i, row in data.iterrows():
        row = map(int, row)
        new_row = []
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                new_row.append("|")

            if val == 0:
                new_row.append('_')
            else:
                new_row.append(val)
        print(*new_row)
        if i == 2 or i == 5:
            print("---------------------")


# build example problem
def get_example_df():
    example_str = """5,3,,,7,,,,
        6,,,1,9,5,,,
        ,9,8,,,,,6,
        8,,,,6,,,,3
        4,,,8,,3,,,1
        7,,,,2,,,,6
        ,6,,,,,2,8,
        ,,,4,1,9,,,5
        ,,,,8,,,7,9"""
    data = [row.split(',') for row in example_str.split('\n')]
    for i in range(len(data)):
        data[i] = [val.strip() for val in data[i]]

    return pd.DataFrame(data).replace('', 0).astype(int)


solver = pywraplp.Solver.CreateSolver('SCIP')

dir_path = os.path.dirname(os.path.realpath(__file__))

game = pd.DataFrame()

print()
print("Welcome to the Sudoku Solver!")
print()
while True:
    print("Which problem would you like to solve?")
    print("1. Example problem\n2. Problem from csv file")
    print()
    option = 0
    try:
        option = int(input("Please select an option: "))
        if option != 1 and option != 2:
            raise Exception()
        else:
            print()
    except:
        print("Invalid input! Please choose either 1 or 2!")
        print()
        continue

    if option == 1:
        game = get_example_df()
        break
    elif option == 2:
        while True:
            try:
                filename = input("Please enter csv file: ")
                game = pd.read_csv(os.path.join(
                    dir_path, filename), header=None)
                game = game.fillna(0)
                if game.shape[0] != 9 or game.shape[1] != 9:
                    raise Exception()
                else:
                    print()
                    break
            except:
                print("Invalid file name! Please enter a valid 9x9 csv file including the .csv extention and the file is in the same directory.")
                print()
        break

print("Sudoku game to solve:")
print_sudoku(game)
print()

int_df = pd.DataFrame(columns=list(range(9)), index=list(range(9)))

# create second dataframe holding boolean solver variables
# each cell holds a dictionary with keys 1-9 with a boolean value
# if the boolean is set to 1 then that key is the selected value for that cell
for i in range(9):
    for j in range(9):
        int_df.iloc[i, j] = [{k: solver.IntVar(
            0, 1, f"Bool_{i}_{j}_{k}") for k in range(1, 10)}]
# constraints
for i in range(9):
    for j in range(9):
        if game.iloc[i, j] != 0:
            # set value to game's predefined value if applicable
            solver.Add(sum([int_df.iloc[i, j][0][key] *
                            key for key in int_df.iloc[i, j][0].keys()]) == game.iloc[i, j])

        # each cell can only select one value
        solver.Add(sum([int_df.iloc[j, i][0][key]
                        for key in int_df.iloc[j, i][0].keys()]) == 1)

        ### Columns ###
        # all values in column must be different
        # checks that only one boolean is set to 1 for each possible value (1-9)
        solver.Add(sum([int_df.iloc[k, i][0][j+1] for k in range(9)]) == 1)

        ### Rows ###
        # all values in row must be different
        # checks that only one boolean is set to 1 for each possible value (1-9)
        solver.Add(sum([int_df.iloc[i, k][0][j+1] for k in range(9)]) == 1)

        ### Subgrids ###
        if i % 3 == 0 and j % 3 == 0 and not int_df.iloc[i:i+3, j:j+3].empty:
            sub_grid = []
            for k, row in enumerate(int_df.iloc[i:i+3, j:j+3].values.tolist()):
                sub_grid += row

                # subgrid built into one list
                if k == 2:
                    # each number should only show up once
                    # checks that only one boolean is set to 1 for each possible value (1-9)
                    for key in range(1, 10):
                        solver.Add(sum([sub_grid[l][0][key]
                                        for l in range(9)]) == 1)

# reassign values of int_df to selected number rather than list
for i in range(9):
    for j in range(9):
        int_df.iloc[i, j] = sum(
            [int_df.iloc[i, j][0][key] * key for key in int_df.iloc[i, j][0].keys()])

# Had to chose some objective to allow the solver to operate.
# Chosing maximize will give a bias of choosing a higher number at the first check
# than a lower number for problems with multiple solutions.
solver.Maximize(sum(int_df.sum(axis=1)))

status = solver.Solve()

for i in range(9):
    for j in range(9):
        # reassign each cell to be the solution value rather than the solver variable
        int_df.iloc[i, j] = int_df.iloc[i, j].solution_value()

if status == solver.OPTIMAL and 0 not in int_df.values:
    print("Solution:")
    print_sudoku(int_df)

else:
    print("Could not find a solution!")
