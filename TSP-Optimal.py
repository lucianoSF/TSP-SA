import json
from docplex.mp.model import Model
import time

def read_distances(file_name='cidades/ar35.json'):
    
    fp = open(file_name)
    distances = json.load(fp)

    return (distances['cities'], distances['distances'])


if __name__ == '__main__':
    start = time.time()
    num_cities, distances = read_distances()
    
    mdl = Model(name='TSP', log_output=True)
    mdl.parameters.mip.tolerances.absmipgap = 1
    
    ## Create decision variables
    key = [(i, j) for i in range(1,num_cities+1) for j in range(1,num_cities+1)]
    mdl.x = mdl.binary_var_dict(keys=key, name='x')
    mdl.u = mdl.integer_var_dict(keys=[i for i in range(2,num_cities+1)], name='u')
    
    ## Objetive Function
    total_cost = mdl.sum(mdl.x[(i,j)]*distances[str(i) + '_' + str(j)] for i in range(1,num_cities+1) for j in range(1,num_cities+1))
    mdl.minimize(total_cost)
    
    
    ## Every city has to be visited once
    for i in range(1,num_cities+1):
        mdl.add_constraint(mdl.sum(mdl.x[(i, j)] for j in range(1,num_cities+1))==1)
        
    for j in range(1,num_cities+1):
        mdl.add_constraint(mdl.sum(mdl.x[(i, j)] for i in range(1,num_cities+1))==1)
        
        
    ## No self loops
    for i in range(1,num_cities+1):
        mdl.add_constraint(mdl.x[(i, i)] == 0)
        
        
    ## No sub-tours
    for i in range(2,num_cities+1):
        mdl.add_constraint(mdl.u[i] >= 1)
        mdl.add_constraint(mdl.u[i] <= num_cities-1)
        
        
        for j in range(2,num_cities+1):
            if(i!=j):
                mdl.add_constraint((num_cities * mdl.x[(i, j)]) + mdl.u[i] - mdl.u[j] <= num_cities - 1)

              
    mdl.solve()
    final = time.time()
    
    for item in key:
        if mdl.x[item].solution_value > 0:
            print("x{} -> {}".format(item, mdl.x[item].solution_value))
            
    print("FO: {}".format(mdl.solution.get_objective_value()))
    print('Time: ', final-start)    
        
        
        
   
    

    
    
    
    
    
    