import random
from util import Queue, Stack, Graph


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # call addUser until number of users is numUsers
        for i in range(numUsers):
            self.addUser(f'User {i+1}')

        # Create random friendships

        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        # Generate list of all possible friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID+1, self.lastID+1):
                possibleFriendships.append((userID, friendID))
        # print("possible friendships:")
        # print(possibleFriendships)

        # shuffle list
        random.shuffle(possibleFriendships)

        # slice off totalFriendships from the front, create friendships
        totalFriendships = avgFriendships * numUsers // 2
        # print(f"Friendships to create: {totalFriendships}")
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        qq = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        qq.enqueue([userID])  # starting node
        # BFT
        while qq.size() > 0:
            path = qq.dequeue()
            vertex = path[-1]
            # print(vertex)
            if vertex not in visited:
                visited[vertex] = path
                for next_vert in self.friendships[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        # print("FINAL VISITED:")
        # print(visited)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(20, 5)
    # print("USERS:")
    # print(sg.users)
    # print("FRIENDSHIPS:")
    # print(sg.friendships)
    test_user = 3
    connections = sg.getAllSocialPaths(test_user)
    print(f"CONNECTIONS TO USER: {test_user}")
    print(connections)


# if roomID not in visited:
#             visited.add(roomID)
#             if '?' in traversalGraph[roomID].values() and lastRoom in traversalGraph[roomID].values():
#                 route.append(opp_dir(lastDir))
#                 qq.dequeue()
#                 break
#             else:
#                 for dir, id in traversalGraph[roomID].items():
#                     if id == lastRoom:
#                         route.append(opp_dir(dir))
#                         lastDir = dir
#                     lastRoom = path[-1]
#                     new_path = list(path)
#                     new_path.append(id)
#                     qq.enqueue(new_path)
