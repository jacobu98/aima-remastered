from search import *

def show_solution(type_search_graph, node):
    if node is None or type(node) == str:
        print(type_search_graph, "no solution")
    else:
        print(type_search_graph, node.solution())

diz_grafo = {
    '00':{'01':1, '10':1},
    '01':{'11':2},
    '10':{'11':3, '20':4},
    '11':{'12':5},
    '12':{'22':2},
    '20':{'30':1, '21':2},
    '21':{'22':2},
    '22':{'32':1},
    '32':{'33':8},
    '30':{'40':1},
    '40':{'41':1},
    '41':{'42':1},
    '42':{'43':1},
    '43':{'33':1}
    }
diz_loc = {
    '00':(0,0),
    '01':(0,1),
    '10':(1,0),
    '11':(1,1),
    '12':(1,2),
    '20':(2,0),
    '21':(2,1),
    '22':(2,2),
    '30':(3,0),
    '32':(3,2),
    '33':(3,3),
    '40':(4,0),
    '41':(4,1),
    '42':(4,2),
    '43':(4,3)
    }

grafo = Graph(diz_grafo, directed=False)
grafo.locations = diz_loc
prob = GraphProblem('00', '33', grafo)

for node in prob.graph.nodes():
    print("Nodo: ", node)
    locs = getattr(prob.graph, 'locations', None)
    if locs:
        if type(node) is str:
            print(int(man_distance(locs[node], locs[prob.goal])))
        #print(int(distance(locs[node], locs[prob.goal])))
    else:
        print('Infinito')
 


#distance(locs[node], locs[self.goal])

print(prob.actions('20'))
show_solution("UCS", uniform_cost_search(prob))
show_solution("Best First", best_first_graph_search(prob, prob.h))
show_solution("ASTAR", astar_search(prob))
