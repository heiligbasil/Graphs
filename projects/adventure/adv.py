import random
from ast import literal_eval

from player import Player
from util import Queue
from world import World

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# === FILL THIS OUT WITH DIRECTIONS TO WALK ===
# You are responsible for filling traversal_path with directions that, when walked in order, will visit every room on the map at least once
# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.
# To solve this path, you'll want to construct your own traversal graph. Your starting graph should look something like this:
# {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}
# You know you are done when you have exactly 500 entries (0-499) in your graph and no '?' in the adjacency dictionaries.
# To do this, you will need to write a traversal algorithm that logs the path into `traversal_path` as it walks.
# === HINTS ===
# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction,
# then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored
# paths), walk back to the nearest room that does contain an unexplored path. You can find the path to the shortest unexplored room by
# using a breadth-first search for a room with a '?' for an exit. If you use the bfs code from the homework, you will need to make a few
# modifications. Instead of searching for a target vertex, you are searching for an exit with a '?' as the value. If an exit has been
# explored, you can put it in your BFS queue like normal. BFS will return the path as a list of room IDs. You will need to convert this
# to a list of n/s/e/w directions before you can add it to your traversal path.

# 1. Pick a random direction
# 2. Walk in that direction
# 3. Log that direction in the traversal graph
# 4. Loop (DFT)
# 5. If dead-end, walk to nearest unexplored path
# 6. Search for '?' in a room instead of vertex (BFS)
# 7. Translate room_id to direction
# 8. Log that direction in the traversal graph

# 3 functions? Central engine + DFT + BFS


def central():
    """The central command point for the completely automatic maze traversal"""
    # The initial starting direction, chosen randomly
    direction = random.choice(player.current_room.get_exits())
    while True:
        if player.current_room.id not in traversal_graph:
            # Add the current room with exit information into the custom traversal list
            dictionary = {}
            for an_exit in player.current_room.get_exits():
                dictionary[an_exit] = '?'
            traversal_graph[player.current_room.id] = dictionary
        graph_id = traversal_graph[player.current_room.id]
        if '?' not in traversal_graph[player.current_room.id].values():
            # The current room has no more unexplored exits, so use BFS to find the closest unexplored room
            room_ids = bfs(player.current_room.id)
            if room_ids is None:
                # All of the rooms have been explored!
                break
            for an_id in room_ids:
                for a_direction in player.current_room.get_exits():
                    if player.current_room.get_room_in_direction(a_direction).id == an_id:
                        walk_to_room(a_direction)
                        break
            direction = get_random_direction()
        elif (direction in graph_id and graph_id[direction] != '?') or direction not in graph_id:
            # Get a new direction once the currently used direction is no longer valid
            direction = get_random_direction()
        # Add the entries and actually walk to the specified room
        walk_to_room(direction)


def get_random_direction():
    """Allow the computer to pick a direction"""
    graph_id = traversal_graph[player.current_room.id]
    while True:
        direction = random.choice(list(graph_id))
        if graph_id[direction] == '?':
            break
    return direction


def bfs(start):
    """Breadth-First Search to find the path to the closest unexplored room"""
    q = Queue()
    q.enqueue([start])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        room = path[-1]
        if room not in visited:
            visited.add(room)
            if room == '?':
                return path[1:-1]
            for r in traversal_graph[room].values():
                path_copy = path.copy()
                path_copy.append(r)
                q.enqueue(path_copy)


def walk_to_room(direction):
    """Update the traversal list, add the direction to the path list, and then actually walk to the room"""
    traversal_graph[player.current_room.id][direction] = player.current_room.get_room_in_direction(direction).id
    traversal_path.append(direction)
    player.travel(direction)


traversal_graph = {}
traversal_path = []
central()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms (out of {len(room_graph)} total)")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
