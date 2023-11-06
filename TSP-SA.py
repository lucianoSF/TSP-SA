import json
import random
import time

code = 'ar35'

# Leitura dos dados, cidades e distâncias entre cada par
def read_distances(file_name='cidades/' + code + '.json'):
    
    fp = open(file_name)
    distances = json.load(fp)
    return (distances['cities'], distances['distances'])


#Criar uma solução inicial
def create_solution(num_cities):
    rc = num_cities
    solution = []
    list_of_cities = list(range(1, rc+1))
    
    # inserir cidades de forma aleatória na solução inicial
    while(rc != 1):
        random_city_index = random.randint(0, rc-1)
        # inserção de cidade na solução e remoção do conjunto de cidades disponíveis
        solution.append(list_of_cities[random_city_index])
        list_of_cities.remove(list_of_cities[random_city_index])
        rc = rc - 1
    # Inserir a última cidade, e única restante em list_of_cities
    solution.append(list_of_cities[0])
    return solution
    
#Criar uma solução candidata a partir da solução inicial 
def create_new_solution(initial_solution, num_cities):
    # Escolha de duas cidades na solução inicial para serem  alternadas
    cityX = random.randint(0, num_cities-1)
    cityY = cityX
    # Garantir que são duas cidades diferentes
    while(cityX == cityY):
        cityY = random.randint(0, num_cities-1)
        
    new_solution = list(initial_solution)
    # Troca de posição entre as cidades
    aux = new_solution[cityX]
    new_solution[cityX] = new_solution[cityY]
    new_solution[cityY] = aux

    return new_solution

    
    
# Calculo do custo de uma solução, ou seja a distância total a ser percorrida
def calculate_cost(solution, distances):
    cost = 0
    for item in range(0, len(solution)-1):
        cost_of_pair_of_cities = distances[str(solution[item]) + '_' + str(solution[item+1])]
        cost = cost + cost_of_pair_of_cities
        
    cost_of_pair_of_cities = distances[str(solution[len(solution)-1]) + '_' + str(solution[0])]
    cost = cost + cost_of_pair_of_cities
    return cost
    

# SA
def SimulatedAnnealing(initial_solution, num_cities, distances, temperature):
    
    k = 0
    LIST_OF_SOLUTIONS = []
    best_solution = None
    best_solution_cost = None
    # Itera enquanto a solução não melhorar em k iterações
    while k < number_iterations_solution_is_not_improved:
        # Numero de soluções vizinhas locais a serem criadas
        for l in range(iterations_each_temperature):
            # Criação de uma solução candidata
            candidate_solution = create_new_solution(initial_solution, num_cities)
            
            #print(initial_solution)
            #print(candidate_solution)
            #return
            
            # Calculo dos custos de cada uma das soluções: candidata e inicial
            cost_X = calculate_cost(initial_solution, distances)
            cost_Y = calculate_cost(candidate_solution, distances)
            
            
            delta_C = cost_Y - cost_X
            # Verificar se a solução candidata é melhor que a solução inicial
            if delta_C < 0:
                initial_solution = candidate_solution
            else:
                # Caso seja pior ainda é possível aceita-la, considerando a temperatura e o quanto pior for a nova solução
                variable_control = random.random()
                
                expo = (-1 * delta_C)/temperature
                # Aceitação da solução candidata    
                if variable_control <= pow(EULER, expo):
                    initial_solution = candidate_solution
        # Atualização da temperatura
        temperature = temperature*alpha
        
        cost = calculate_cost(initial_solution, distances)
        print('Best Solution Cost --> ', cost, 'k: ', k, 'T: ', temperature)
        
        # A melhor solução para cada temperatura é armazenada
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

    return best_solution

# Gravação da solução em arquivo
def record_solutions(solutions, code=code):
        with open('saidas/SA/' + code  + '_solution.csv', 'a') as file:
            file.write('Solution\n')
            for item in solutions:
                file.write(str(item) + '\n')
if __name__ == '__main__':
    
    start = time.time()
    
    EULER = 2.718281828459
    temperature = 1000
    alpha = 0.98
    iterations_each_temperature = 500
    number_iterations_solution_is_not_improved = 100
    # Ler dados
    num_cities, distances = read_distances()
    # Criar solução inicial
    initial_solution = create_solution(num_cities)
    # 
    print(initial_solution)
    # Rodar SA
    final_solution = SimulatedAnnealing(initial_solution, num_cities, distances, temperature)
    final = time.time()
    
    print('Final Solution: ', final_solution, '\nCost: ', calculate_cost(final_solution, distances))
    print('Time: ', final-start)
    
    
            
    
    
    
    
    
    