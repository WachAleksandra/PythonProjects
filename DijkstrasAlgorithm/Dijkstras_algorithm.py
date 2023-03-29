import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

def read_graph(file_name):
    with open(file_name, 'r') as f:
        v, e, s, k = map(int, f.readline().split())
        G = {i: set() for i in range(v)}
        D = nx.DiGraph() 
        for line in f:
            u, v, w = map(int, line.split())
            G[u].add((v, w))
            D.add_edge(u, v, weight=w) 
    return G, s, k, D

def dijkstra(G, s, k):
    visited = set()
    cost = {s: 0}
    parent = {s: None}
    todo = PriorityQueue()
    todo.put((0, s))
    try:
        while todo:
            while not todo.empty():
                _, vertex = todo.get() # find the lowest vertex cost
            #loop until a new vertex is found
                if vertex not in visited: break
            else: 
                break 
            visited.add(vertex)
            if vertex == k:
                break
            if G[vertex]:
                for neighbor, distance in G[vertex]:
                    if neighbor in visited: continue 
                    old_cost = cost.get(neighbor, float('inf')) #default to infinity
                    new_cost = cost[vertex] + distance
                    if new_cost < old_cost:
                        todo.put((new_cost, neighbor))
                        cost[neighbor] = new_cost
                        parent[neighbor] = vertex
        print("The shortest path is:", cost[k])
        return parent
    except KeyError:
            print("Path does not exist.")
            return parent
    
def make_path(parent, k):
    if k not in parent:
        return None
    v = k
    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1]

def show_wpath(D, s, k,custom_node_positions=None):
    if custom_node_positions==None:
        pos = nx.spring_layout(D)
    else:
        pos=custom_node_positions
    
    weight_labels = nx.get_edge_attributes(D,'weight')
    path = nx.dijkstra_path(D, source = s, target = k)

    edges_path = list(zip(path,path[1:])) #creating a list of edges
    edges_path_reversed = [(y,x) for (x,y) in edges_path]
    edges_path = edges_path + edges_path_reversed
    edge_colors = ['black' if not edge in edges_path else 'red' for edge in D.edges()]

    nodecol = ['steelblue' if not node in path else 'red' for node in D.nodes()]
    total_weight = 0
    node_label = {}
    for i in range(len(path)-1):
        total_weight += D[path[i]][path[i+1]]['weight']
        if i == 0:
            node_label[path[i]] = 0
    node_label[path[-1]] = (total_weight)
    
    pos_higher = {}
    for k, v in pos.items():
        if(v[1]>0):
            pos_higher[k] = (v[0]-0.1, v[1]+0.1)
        else:
            pos_higher[k] = (v[0]-0.1, v[1]-0.1)
    nx.draw_networkx_labels(D, pos_higher, labels = node_label, verticalalignment='bottom')
    nx.draw(D, pos, with_labels = True, font_color = 'white', edge_color= edge_colors, node_shape = 's', node_color = nodecol)    
    nx.draw_networkx_edge_labels(D,pos,edge_labels=weight_labels)

pos_node = {0:(1,2),1:(2,3),2:(2,1),3:(10,3),4:(4,3),5:(5,1), 6:(6,2), 7:(7,3), 8:(8,3),9:(8,1),10:(10,1)}

if __name__ == '__main__':
    file_name = 'example_graph.txt'
    G, s, k, D = read_graph(file_name)
    parent = dijkstra(G, s, k)
    path = make_path(parent, k)
    print(path)
    show_wpath(D,s,k,pos_node)
    plt.savefig("example_graph.png")