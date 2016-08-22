#!/usr/bin/python

import numpy as np

def dijkstra(graph, source):
    
    # Matrix size
    n = len(graph)
    
    # Assign an intital distance value of infinity to all the nodes 
    infinity = float('inf')
    distance = [infinity for i in range(n)]
    # Assign a distance value of zero to the starting node
    distance[source] = 0
    current_node = source
    # Variables to store visited nodes and their distance from the starting node
    visited_nodes = list()
    visited_nodes_and_cost = list()
    # Variable to store nodes and their distance from the starting node
    dictionary = {}
    dictionary.update({source:distance[source]})
    # Variable to store the previous nodes, reversed the assignment of key,value 
    # in order to correctly update
    preceeding_nodes = {}
    
    while((len(dictionary))!=0):
        
        # Identify the node with the smallest distance value in the dictionary
        current_node, cost = min(dictionary.items(), key=lambda x:x[1])
        # remove the node with the smallest distance value from the dictionary
        del dictionary[min(dictionary, key=dictionary.get)]
        # mark the current node as visited
        visited_nodes.append(current_node)
        visited_nodes_and_cost.append((current_node,cost))
        
        # check distances from all neighboring nodes to the current node
        for j in range(n):
            # only evaluate nodes in the graph that contain edges
            # and that have not been visited
            if(graph[current_node][j]!=0 and j not in visited_nodes):
                # update the distances from neighboring nodes to the current nodes
                # and store in the dictionary
                if(distance[current_node] + graph[current_node][j] < distance[j]):
                    distance[j] = distance[current_node] + graph[current_node][j]
                    dictionary.update({j:distance[j]})
                    preceeding_nodes[j] = current_node
                    
    return visited_nodes_and_cost, preceeding_nodes 

def main():
    
     # prompt user to enter the file name
     filename = raw_input('Enter the file name: ')+'.txt'
     
     # load adjacency matrix from text tile
     graph = np.loadtxt(filename)
     
     # prompt user to enter the source node
     start_node = input('Enter starting node: ')
     while start_node>=len(graph) or start_node<0:
        start_node = input('The value entered is out of bounds. Try again: ')
        
     # prompt user to enter the source node
     end_node = input('Enter end node: ')
     while end_node>=len(graph) or start_node<0:
        end_node = input('The value entered is out of bounds. Try again: ')
     target_node = end_node 
    
     costs = []
     previous = {}
     costs, previous = dijkstra(graph, start_node)
     
     # print the shortest path from the start node to every other node
     print "The shortest path from the start node %d to every other node in the graph is \n %s" %(start_node,costs)    
  
     # find the shortest path from source node to target node
     SSSPath = []
     while True:
         SSSPath.append(end_node)
         if(end_node == start_node):
             break
         end_node = previous[end_node]   
     SSSPath.reverse()
    
     # print the shortest path from the start node to the target node
     print "The shortest path from the start node %d to the target node %d is %s with a distance of %s"\
     %(start_node, target_node, SSSPath, dict(costs).get(target_node))
    
main()
    


