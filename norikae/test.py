
import json

outrages = open("outrages.json","r")
out_data = json.load(outrages)
url = open("data.json","r")
output = json.load(url)

def create_graph(output): 
	graph = {}
	for line_stations_map in output:
		eki_list = line_stations_map['Stations']
		for i, eki in enumerate(eki_list):
			if eki not in graph: 
				graph[eki] = []
			for j in (i-1, i+1):
				if 0 <= j < len(eki_list):
					graph[eki].append(eki_list[j])
	return graph 

def outrages(graph, out_data):
	for from_to in out_data:
		graph[from_to['From']].remove(from_to['To'])
	return graph
    
def find_route(graph, start, end, route=[]):
    route = route + [start]
    if start == end:
        return route
    if not graph.has_key(start):
        return None
    for node in graph[start]:
    	print start 
        print graph[start]

        if node not in route:
            newroute = find_route(graph, node, end, route)
            if newroute: return newroute
    return None

start = "Nowhere"
end = "Field of Flying Elephants"
# print create_graph(output)
# print '\n'
# print outrages(create_graph(output), out_data)

print '\n'
print find_route(create_graph(output), start, end)

print find_route(outrages(create_graph(output), out_data), start, end)
graph = outrages(create_graph(output), out_data)
print graph
print graph[start]
print graph['Woods of No Name']
print graph['City of Charity']
print graph['Living Flower Maze']

# graph = 
 
# print graph 

# print start
# print graph[start]
