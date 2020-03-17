"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges"""

    def __init__(self):
        """Default constructor for this class"""
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """Add a vertex to the graph"""
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """Add a directed edge to the graph"""
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError('Vertex does not exist')

    def add_undirected_edge(self, v1, v2):
        """Add a directed edge to the graph"""
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """Get all neighbors (edges) of a vertex"""
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError('Vertex does not exist')

    def bft(self, starting_vertex):
        """Print each vertex in breadth-first order beginning from starting_vertex"""
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        print('Breadth-First Order:', end=' ')
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                print(v, end=', ')
                # Enqueue all of its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
        print()

    def dft(self, starting_vertex):
        """Print each vertex in depth-first order beginning from starting_vertex"""
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        print('Depth-First Order:', end=' ')
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                print(v,end=', ')
                # Push all of its neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
        print()

    def dft_recursive(self, starting_vertex, visited=None):
        """Print each vertex in depth-first order beginning from starting_vertex. This should be done using recursion"""
        # Initialize the default argument if necessary
        if visited is None:
            visited = set()
        # Check if the vertex has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
            print(starting_vertex, end=', ')
            # Push all of its neighbors onto the stack
            for neighbor in self.get_neighbors(starting_vertex):
                # Call dft_recursive on each neighbor
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order"""
        # Create a queue
        q = Queue()
        # Enqueue a path to the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # Grab the vertex from the end of the path
            vertex = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Check if it's the target
                if vertex == destination_vertex:
                    # If so, return the path
                    return path
                else:
                    # Enqueue a path to all of its neighbors
                    for neighbor in self.get_neighbors(vertex):
                        # Make a copy of the path
                        path_copy = path.copy()
                        # Add the neighbor to the path
                        path_copy.append(neighbor)
                        # Enqueue the copy
                        q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """Return a list containing a path from starting_vertex to destination_vertex in depth-first order"""
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """Return a list containing a path from starting_vertex to destination_vertex in depth-first order. This should be done using recursion"""
        pass  # TODO


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
    print(f'Graph vertices: {graph.vertices}')

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
    print('Depth-First Traversal (recursive): ', end=' ')
    graph.dft_recursive(1)
    print()

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f'Breadth-First Search path: {graph.bfs(1, 6)}')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(f'DFS path (iterative): {graph.dfs(1, 6)}')
    # print(f'DFS path (recursive): {graph.dfs_recursive(1, 6)}')
