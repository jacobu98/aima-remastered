from search import *

dim = 7
def show_solution(type_search_graph, node):
    if node is None:
        print(type_search_graph, "no solution")
    else:
        print(type_search_graph, node.solution())
#print(dizionario)
# Creazione del grafo rappresentate lo stato iniziale del problema
# La funzione restituisce il dizionario, la partenza (indice di riga e di colonna)
def getFromMatrix(m,matrice,r,c):
  multiplier = dim*dim
  if m!=7:
    if m==5 or m==6 or m==0:
      return 1
    else:
      return m*multiplier
  else:
    return -1
def makegraph(out):
  dizionario = dict()
  locaziones = dict()
  for cnt, x in enumerate(out):
    if x == 6:
      source_row = int(cnt/dim)
      source_col = cnt%dim
  matrice = out.reshape(dim,dim)
  for r, row in enumerate(matrice):
    for c, el in enumerate(row):        
      if el != 7:
        locaziones[str(r)+str(c)]=[r,c]
        node = dict()
        if r-1>=0:
          v = getFromMatrix(matrice[r-1][c],matrice,r,c)
          if v != -1 :
            node[str(r-1)+str(c)] = v
        if r+1<dim:
          v = getFromMatrix(matrice[r+1][c],matrice,r,c)
          if v != -1 :
            node[str(r+1)+str(c)] = v
        if c-1>=0:
          v = getFromMatrix(matrice[r][c-1],matrice,r,c)
          if v != -1 :
            node[str(r)+str(c-1)] = v
        if c+1<dim:
          v = getFromMatrix(matrice[r][c+1],matrice,r,c)
          if v != -1 :
            node[str(r)+str(c+1)] = v
        dizionario[str(r)+str(c)] = node
  return dizionario, source_row, source_col, locaziones
def viewDict(dizionario):
  for key in dizionario:
    print("da ", key, " -> ", dizionario[key])
  print("----------------------------")
inizio = np.asarray(
      [6, 1, 1, 7, 7,
       2, 7, 1, 7, 7,
       3, 7, 1, 4, 5,
       1, 0, 0, 7, 7,
       5, 7, 7, 7, 7])
inizio_big = np.asarray(
  [
    0,0,6,1,1,1,1,
    1,7,4,7,7,0,7,
    1,0,1,7,0,7,7,
    7,7,1,1,4,7,7,
    1,1,1,7,4,7,5,
    7,7,0,0,0,7,1,
    5,0,0,7,1,1,1
  ]
)

dizionario, source_row, source_col, locaziones = makegraph(inizio_big)
viewDict(dizionario)
maze_graph = UndirectedGraph(dizionario)
maze_graph.locations = locaziones
maze_problem = GraphProblem('02', ['46','60'], maze_graph)

def best_first(problem, f):
    global numero_nodi
    nodo_iniziale = Node(problem.initial)
    numero_nodi = 1
    if problem.goal_test(nodo_iniziale.state):
        return nodo_iniziale
    f = memoize(f,'f')
    frontiera = PriorityQueue('min',f)
    frontiera.append(nodo_iniziale)
    visitati = set()

    while frontiera:
        nodo = frontiera.pop()
        visitati.add(nodo.state)
        for g in problem.goal:
          if nodo.state == g:
            return nodo 

        expand = nodo.expand(problem)
        numero_nodi += len(expand)
        for nodo_figlio in expand:
            if nodo_figlio.state not in visitati and nodo_figlio not in frontiera:
                frontiera.append(nodo_figlio)
            elif nodo_figlio in frontiera:
                nodo_prossimo = frontiera.get_item(nodo_figlio)
                if f(nodo_figlio) < f(nodo_prossimo):
                    del frontiera[nodo_prossimo]
                    frontiera.append(nodo_figlio)
def greedy_search(problem, h=None):
    """f(n) = h(n)"""
    h = memoize(h or problem.h, 'h') 
    return best_first(problem, lambda n: h(n))
def astar_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    return best_first(problem, lambda n: h(n)+n.path_cost)
def solo_costo(problem, h=None):
    return best_first(problem, lambda n: n.path_cost)
print("Problema iniziale. Andare da ", maze_problem.initial, " -> ", maze_problem.goal)

show_solution("Solo euristica:    ", greedy_search(maze_problem))
show_solution("Solo costo:        ", solo_costo(maze_problem))
show_solution("Euristica e costo: ", astar_search(maze_problem))
