from collections import deque
def repeat_bfs(adj_dict):
    """
    Below is a sample implementation of the basic version of breadth first search from Learn (with a small modification). Alter the code below so that it starts traversing from the first node in the adjacency dictionary and finds all of the nodes in the graph, even if it is a disconnected graph. 
    
    Each graph will contain nodes from 1 -> n. Keep in mind some of the nodes may be connected to the first node in the adjacency dictionary, and others may be "islands" or disconnected from the first node in the dictionary. 
    """
    # if there are no nodes in the graph
    if len(adj_dict) == 0:
        # return an empty list
        return []

    # grab the first node in the adjacency dictionary
    first_node = list(adj_dict.keys())[0]
    # initialize visited list
    visited = [first_node]
    queue = deque([first_node])

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