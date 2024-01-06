import json
#Data
f = open('Input data/level0.json')
data = json.load(f)
route=[]
nd=[0]
nd=nd+(data['restaurants']['r0']['neighbourhood_distance'])
route.append(nd)
j=1
for i in data['neighbourhoods']:
    te=[nd[j]]
    te=te+(data['neighbourhoods'][i]['distances'])
    route.append(te)
    j+=1
#[print(x, len(x)) for x in route]
    


def nearest_neighbor(route):
    num_nodes = len(route)
    start_node = 0
    current_node = start_node
    path = [current_node]
    remaining_nodes = set(range(0, num_nodes-1))

    while remaining_nodes:
        nearest_neighbor = min(remaining_nodes, key=lambda x: route[current_node][x])
        path.append(nearest_neighbor)
        remaining_nodes.remove(nearest_neighbor)
        current_node = nearest_neighbor
    path.append(start_node)

    return path


shortest_path = nearest_neighbor(route)
print("Shortest Path:", shortest_path)

'''from sys import maxsize 
from itertools import permutations'''
# implementation of traveling Salesman Problem 
'''def travellingSalesmanProblem(graph, s): 

	# store all vertex apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 

	# store minimum weight Hamiltonian Cycle 
	min_path = maxsize 
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost) 
		current_pathweight = 0

		# compute current path weight 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		# update minimum 
		min_path = min(min_path, current_pathweight) 
		
	return min_path '''



#s=0
#print(travellingSalesmanProblem(route, s))
#outputFormat
#{"v0": {"path": ["r0", "n14", "n9", "n4", "n17", "n2", "n19", "n10", "n15", "n18", "n5", "n16", "n11", "n13", "n7", "n8", "n20", "n6", "n1", "n12", "n3", "r0"]}}
f.close()
