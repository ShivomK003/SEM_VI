from constraint import Problem, AllDifferentConstraint

def tsp_csp(num_cities, distances):
    problem = Problem()

    cities = list(range(num_cities))

    problem.addVariables(cities, cities)

    problem.addConstraint(AllDifferentConstraint(), cities)

    for i in cities:
        for j in cities:
            if i != j:
                problem.addConstraint(lambda x, y, i=i, j=j: distances[i][j] == distances[x][y], (i, j))

    def total_distance(*order):
        return sum(distances[order[i]][order[i+1]] for i in range(num_cities-1))

    problem.addConstraint(total_distance, cities)

    solutions = problem.getSolutions()

    if solutions:
        best_solution = min(solutions, key=lambda sol: total_distance(*sol.values()))
        return best_solution
    else:
        return None

num_cities = 4
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 20],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

result = tsp_csp(num_cities, distance_matrix)

if result:
    print("Optimal Tour Order: ", result)
    print("Optimal Total Distance:",sum(distance_matrix[result[i]][result[i+1]] for i in range(num_cities-1)))
else:
    print('No solution found.')
