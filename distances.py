import json
import math

code = 'uy734'
data_file = 'cidades/' + code + '.tsp'


def create_distances_file(lines):
    distances = {}
    
    distances['cities'] = len(lines)
    distances['distances'] = {}
    
    mean_distance = 0
    min_distance = None
    max_distance = None
    
    for i in lines:
        for j in lines:
            distances['distances'][str(i[0]) + '_' + str(j[0])] = round(math.sqrt(pow((j[1] - i[1]), 2) + pow((j[2] - i[2]), 2)))
            
            mean_distance = mean_distance + distances['distances'][str(i[0]) + '_' + str(j[0])]
            
            if i != j:
                if min_distance == None or min_distance > distances['distances'][str(i[0]) + '_' + str(j[0])]:
                    min_distance = distances['distances'][str(i[0]) + '_' + str(j[0])]
                if max_distance == None or max_distance < distances['distances'][str(i[0]) + '_' + str(j[0])]:
                    max_distance = distances['distances'][str(i[0]) + '_' + str(j[0])]
                    
    #print(mean_distance, min_distance, max_distance)
                
    distances['mean_distance'] = round(mean_distance/(distances['cities']*distances['cities']))
    distances['min_distance'] = min_distance
    distances['max_distance'] = max_distance
            
    #create_distances_version2(distances)
    
    with open('cidades/' + code + '.json', 'w') as json_file:
        json.dump(distances, json_file, indent=4)
        

def read_data(data_file=data_file):
    lines = []
    
    file = open(data_file, "r")
    data = file.readlines()
    
    for i in data:
        lines.append(i.split())
        
    for i in lines[:-1]:
        i[1] = float(i[1])
        i[2] = float(i[2])
        
    return lines[:-1]
        
    
if __name__ == "__main__":
    
    lines = read_data()
    create_distances_file(lines)
    
