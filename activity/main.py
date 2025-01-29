from collections import deque
def repeat_bfs(adj_dict):
    """
    Below is a sample implementation of the basic version of breadth first search from Learn. Alter the code below so that it starts traversing from the first node in the adjacency dictionary and finds all of the nodes in the graph, even if it is a disconnected graph. 
    
    Each graph will contain nodes from 1 -> n. Keep in mind some of the nodes may be connected to the first node in the adjacency dictionary, and others may be "islands" or disconnected from the first node in the dictionary.  
    """
    # if there are no nodes in the graph
    if len(adj_dict) == 0:
        # return an empty list
        return []
        
    # initialize visited list
    visited = []
    
    # outer loop to guarantee we perform bfs on all nodes, whether connected to the starting node or not
    for node in adj_dict.keys():
        if node in visited:
            # already covered by a previous traversal so skip
            continue
            
        # initialize a new queue and add i as the starting node
        visited.append(node)
        # initialize a list of visited nodes and add start_node
        queue = deque([node])

        # while there are still nodes in the queue
        while queue:
        # pop node off the queue and set it as current
            current = queue.popleft()
            
            # loop through current's neighbors
            for neighbor in adj_dict[current]:
                # if the neighbor has not yet been visited
                if neighbor not in visited:
                    # add it to the list of visited nodes
                    # (we've now visited it!)
                    visited.append(neighbor)
                    # append the node to the queue so we can visit its neighbors!
                    queue.append(neighbor)
    # return list of visited nodes
    return visited