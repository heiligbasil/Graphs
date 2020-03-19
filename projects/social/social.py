import random
import pprint


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    """
        - Nodes are Users
        - Edges are friendships
        - Undirected
        - Cyclic
        - BFS
    """

    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """Creates a bi-directional friendship"""
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """Create a new user with a sequential integer ID"""
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships as arguments
        Creates that number of users and a randomly distributed friendships between those users
        The number of users must be greater than the average number of friendships
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        # Write a for loop that calls add_user the right amount of times
        for i in range(num_users):
            self.add_user(f'User_{i + 1}')
        # Create friendships: To create N random friendships, you could create a list with all possible friendship combinations,
        # shuffle the list, then grab the first N elements from the list. (You will need to import random to get shuffle)
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        # Create n friendships where n = avg_friendships * num_users // 2
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's extended network with the shortest friendship path between them
        The KEY is the friend's ID and the VALUE is the path
        """
        visited = {}
        for i in range(1, len(self.users) + 1):
            connection = self.bfs(user_id, i)
            if connection:
                visited[i] = connection
        return visited

    def bfs(self, user_id, connection_id):
        q = Queue()
        q.enqueue([user_id])
        visited = set()
        while q.size() > 0:
            network = q.dequeue()
            friend = network[-1]
            if friend not in visited:
                visited.add(friend)
                if friend == connection_id:
                    return network
                for connection in self.get_connections(friend):
                    network_copy = network.copy()
                    network_copy.append(connection)
                    q.enqueue(network_copy)

    def get_connections(self, friend):
        if friend in self.friendships:
            return self.friendships[friend]
        else:
            raise ValueError(f'Friend {friend} does not exist')


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'Friendships:\n{pprint.pformat(sg.friendships)}')
    connections = sg.get_all_social_paths(1)
    print(f'Connections:\n{pprint.pformat(connections)}')
