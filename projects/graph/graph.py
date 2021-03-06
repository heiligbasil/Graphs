"""
Simple graph implementation
"""
import io
import sys

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
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                print(v)
                # Enqueue all of its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """Print each vertex in depth-first order beginning from starting_vertex"""
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                print(v)
                # Push all of its neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """Print each vertex in depth-first order beginning from starting_vertex, using recursion"""
        # Initialize the default parameter if necessary
        if visited is None:
            visited = set()
        # Check if the vertex has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
            print(starting_vertex)
            # Push all of its neighbors onto the stack
            for neighbor in self.get_neighbors(starting_vertex):
                # Call dft_recursive on each neighbor
                self.dft_recursive(neighbor, visited)

    def dft_recursive_guided_lecture(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
​        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # Check if the node has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
            print(starting_vertex)
            # Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive_guided_lecture(neighbor, visited)

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

    def bfs_guided_lecture(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # Check if it's been visited
            if v not in visited:
                # If it hasn't been visited...
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # ENQUEUE THE COPY
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """Return a list containing a path from starting_vertex to destination_vertex in depth-first order"""
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]
            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    return path
                else:
                    for neighbor in self.get_neighbors(vertex):
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        s.push(path_copy)

    def dfs_guided_lecture(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        s = Stack()
        # Push A PATH TO the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # PUSH THE COPY
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """Return a list containing a path from starting_vertex to destination_vertex in depth-first order, using recursion"""
        if visited is None:
            visited = set()
        if path is None:
            path = [starting_vertex]
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            if starting_vertex == destination_vertex:
                return path
            for neighbor in self.get_neighbors(starting_vertex):
                path_copy = path.copy()
                path_copy.append(neighbor)
                result = self.dfs_recursive(path_copy[-1], destination_vertex, path_copy, visited)
                if result:
                    return result

    def dfs_recursive_guided_lecture(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive_guided_lecture(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None

    def dfs_recursive_eric(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            if starting_vertex == destination_vertex:
                return [starting_vertex]
            for vertex in self.vertices[starting_vertex]:
                vertices = self.dfs_recursive_eric(vertex, destination_vertex, visited)
                if destination_vertex in vertices:
                    return [starting_vertex, *vertices]
        return []


if __name__ == '__main__':
    stdout_ = sys.stdout
    sys.stdout = io.StringIO()
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

    print(f'\nBreadth-First Order: ')
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''

    print(f'\nDepth-First Order: ')
    graph.dft(1)
    print(f'\nDepth-First Traversal (recursive): ')
    graph.dft_recursive(1)
    print(f'\nDepth-First Traversal (recursive) GL: ')
    graph.dft_recursive_guided_lecture(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f'\nBreadth-First Search path: {graph.bfs(1, 6)}')
    print(f'\nBreadth-First Search path GL: {graph.bfs_guided_lecture(1, 6)}')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(f'\nDepth-First Search path (iterative): {graph.dfs(1, 6)}')
    print(f'\nDepth-First Search path (iterative) GL: {graph.dfs_guided_lecture(1, 6)}')

    print(f'\nDepth-First Search path (recursive): {graph.dfs_recursive(1, 6)}')
    print(f'\nDepth-First Search path (recursive) GL: {graph.dfs_recursive_guided_lecture(1, 6)}')
    print(f'\nDepth-First Search path (recursive) ERIC: {graph.dfs_recursive_eric(1, 6)}')

    output = sys.stdout.getvalue()
    sys.stdout = stdout_
    output = output.strip().replace('\n', ',').replace(',,', '\n').replace(' ,', ' ')
    print(output)
