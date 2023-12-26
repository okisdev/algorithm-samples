
def solve_queens(problem):
    if len(problem) == 8:
        return [problem]
    else:
        return extend_problem(problem)

def extend_problem(problem):
    solutions = []
    for new_column in range(1, 9):
        if no_conflict(new_column, problem):
            solutions += solve_queens(problem + [new_column])
    return solutions

def no_conflict(new_column, problem):
    for row in range(len(problem)):
        if problem[row] == new_column or problem[row] - row == new_column - len(problem) or problem[row] + row == new_column + len(problem):
            return False
    return True

# Testing
for solution in solve_queens([]):
    print(solution)  # Prints all solutions to the 8 queens problem
