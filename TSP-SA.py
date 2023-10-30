import json
import random




code = 'qa194'

def read_distances(file_name='cidades/' + code + '.json'):
    
    fp = open(file_name)
    distances = json.load(fp)
    return (distances['cities'], distances['distances'])


def create_solution(num_cities):
    rc = num_cities
    solution = []
    list_of_cities = list(range(1, rc+1))
    
    while(rc != 1):
        random_city_index = random.randint(0, rc-1)
        
        solution.append(list_of_cities[random_city_index])
        list_of_cities.remove(list_of_cities[random_city_index])
        rc = rc - 1
    
    solution.append(list_of_cities[0])
    return solution
    
def create_new_solution(initial_solution, num_cities):
    
    cityX = random.randint(0, num_cities-1)
    cityY = cityX

    while(cityX == cityY):
        cityY = random.randint(0, num_cities-1)
        
        
    #print(cityX, cityY)  
    new_solution = list(initial_solution)
    
    aux = new_solution[cityX]
    new_solution[cityX] = new_solution[cityY]
    new_solution[cityY] = aux

    return new_solution

    
    
    
def calculate_cost(solution, distances):
    cost = 0
    for item in range(0, len(solution)-1):
        cost_of_pair_of_cities = distances[str(solution[item]) + '_' + str(solution[item+1])]
        cost = cost + cost_of_pair_of_cities
        
    cost_of_pair_of_cities = distances[str(solution[len(solution)-1]) + '_' + str(solution[0])]
    cost = cost + cost_of_pair_of_cities
    return cost
    
#def calculate_probability(initial_solution, candidate_solution):
    
    
    
def SimulatedAnnealing(initial_solution, num_cities, distances, temperature):
    
    k = 0
    LIST_OF_SOLUTIONS = []
    best_solution = None
    best_solution_cost = None
    
    while k < number_iterations_solution_is_not_improved:
        
        for l in range(iterations_each_temperature):
            
            candidate_solution = create_new_solution(initial_solution, num_cities)
            
            #print(initial_solution)
            #print(candidate_solution)
            #return
            cost_X = calculate_cost(initial_solution, distances)
            cost_Y = calculate_cost(candidate_solution, distances)
            
            
            #print(cost_X, cost_Y)
            #return
            delta_C = cost_Y - cost_X
            
            if delta_C < 0:
                initial_solution = candidate_solution
            else:
                variable_control = random.random()
                
                expo = (-1 * delta_C)/temperature
                    
                if variable_control <= pow(EULER, expo):
                    initial_solution = candidate_solution

        temperature = temperature*alpha
        
        cost = calculate_cost(initial_solution, distances)
        print('Best Solution Cost --> ', cost, 'k: ', k, 'T: ', temperature)
        
        
        if best_solution == None:
            best_solution = initial_solution
            best_solution_cost = calculate_cost(best_solution, distances)
        else:
            if cost < best_solution_cost:
                best_solution = initial_solution
                best_solution_cost = cost
                k = 0
            else:
                k = k + 1
                
        LIST_OF_SOLUTIONS.append(cost)
        
    record_solutions(solutions=LIST_OF_SOLUTIONS)
    #print('Temperature: ', temperature) 
    print(best_solution)
    return best_solution
        
def record_solutions(solutions, code=code):
        with open(code  + '_solution.csv', 'a') as file:
            file.write('Solution\n')
            for item in solutions:
                file.write(str(item) + '\n')
if __name__ == '__main__':
    
    
    EULER = 2.718281828459
    temperature = 1000
    alpha = 0.95
    iterations_each_temperature = 10
    number_iterations_solution_is_not_improved = 1000

    num_cities, distances = read_distances()
    
    initial_solution = create_solution(num_cities)
    
    print(initial_solution)
    
    final_solution = SimulatedAnnealing(initial_solution, num_cities, distances, temperature)
    
    print('Final Solution: ', final_solution, 'Cost: ', calculate_cost(final_solution, distances))
    
    
            
    
    
    
    
    
    