"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices(vertex_id)
        
    def bft(self, starting_vertex):
        # create an empty Queue
        q = Queue()
        # create a set to store the visisted nodes
        visited = set()
        # init: enqueue the starting nodes
        q.enqueue(starting_vertex)
        # While the queue isn't empty
        while q.size() > 0:
            # Dequeue the first item
            v = q.dequeue()
            # If it's note been visisted:
            if v not in visited:
                # mark as visited
                visited.add(v)
                # Do something with the node
                print(f"Visited {v}")
                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        visited = []
        stack = Stack()
        stack.push(starting_vertex)
        while stack.size() > 0:
            item = stack.pop()
            if item not in visited:
                visited.append(item)
                print(item)
                for adj in self.vertices[item]:
                    stack.push(adj)

    def dft_recursive(self, starting_vertex):
        if not visited:
            visited = []
        print(starting_vertex)
        visited.append(starting_vertex)
        for adj in self.vertices[starting_vertex]:
            if adj not in visited:
                self.dft_recursive(adj, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visisted
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN PATH
                if v == destination_vertex:
                    return path
                # Mark it as visited
                visited.add(v)

                # Then add A PATH TO its neighbors to the back of the queue
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR TO THE BACK
                
                for next_vert in self.get_neighbors(v):
                    new_path = list(path) # Copy the list
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        
        # If we got here, we didn't find it
        return None

    def dfs(self, starting_vertex, destination_vertex):
        visited = [] 
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            v = path[-1]
            if v not in visited:
                visited.append(v)
                for adj in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(adj)
                    stack.push(new_path)
                    if adj == destination_vertex:
                        return new_path

    def dfs_recursive(self, starting_vertex, destination_vertex):
        if not path:
            path = []
        if not visited:
            visited = []
        path.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        if starting_vertex not in visited:
            visited.append(starting_vertex)
        for adj in self.vertices[starting_vertex]:
            if adj not in visited:
                new_path = list(path)
                next_path = self.dfs_recursive(adj, destination_vertex, new_path, visited)
                if next_path:
                    return next_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
