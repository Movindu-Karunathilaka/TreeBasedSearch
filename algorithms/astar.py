
import heapq
import math

#not fuctional yet

def astar(graph, start, goals, nodes):
    
    map()
    #need to do f(n) = g(n) + h(n)
    #f(n) = estimate distance from end node , g(n) = total cost so far to reach this node. , h(n) = heuristic score. \
    #Need to account for multiple goals: select the goal closest to the origin
    
    stack = [0, start, [start]]    
    total_cost = 0
    number_of_nodes = 0
    
    while stack:
        
        
        
        
        if nodes in goals:
            
            return
        
    
    
    
    




def heuristic(nodes, current_node, goals):
    
    return min(Euclidean_distance(nodes[current_node], nodes[goals]) for g in goals)
#Min means its selecting the closest goal node.

def Euclidean_distance(CNC, GNC,):
    
    return math.sqrt((GNC[0]-CNC[0])^2 + (GNC[1]-CNC[1])^2)
    
    # CNC = Current Node Coordinates
    # GNC = Goal Node Coordinates
    
    #distance between 2 points: current node and goal node (straight line calc) sqrt((x2-x1)^2+(y2-y1)^2)
    #Using Euclidean distance method for Heuristic 
    #method from: https://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
    
    



