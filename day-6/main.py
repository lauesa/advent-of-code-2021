import numpy as np

def population_estimator(current_pop, period):
    population = dict.fromkeys(range(-1, 9), 0)
    for x in current_pop:
        population[int(x)] +=1

    for i in range(0, period):
        for pop in range(0, 9):
            population[pop-1] += population[pop]
            population[pop] = 0
        else:
            population[6] += population[-1]
            population[8] += population[-1]
            population[-1] = 0
    else:
        print sum(population.values())

with open("input.txt") as file:
    for i, line in enumerate(file):
        if i == 0:
            data = np.asarray(line.strip().split(','))

population_estimator(data, 80)
population_estimator(data, 256)

