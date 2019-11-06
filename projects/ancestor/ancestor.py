from util import Graph, Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    # vertices: digits
    anGraph = Graph()

    for item in ancestors:
        anGraph.add_vertex(item[0])
        anGraph.add_vertex(item[1])

    for item in ancestors:
        # anGraph.add_edge(item[0], item[1])
        # anGraph.add_edge(item[1], item[0])
        anGraph.add_edge(item[1], item[0])

    stack = Stack()
    visited = set()
    stack.push([starting_node])
    paths = []

    print(anGraph.vertices)

    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        if vertex not in visited:
            paths.append(path)
            print(paths)
            visited.add(vertex)
            for next_vert in anGraph.vertices[vertex]:
                # if vertex > 9 and next_vert > vertex:
                #     new_path = list(path)
                #     new_path.append(next_vert)
                #     stack.push(new_path)
                #     continue

                # if vertex < 10 and (next_vert < vertex or next_vert > 9):
                for next_vert in anGraph.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    if len(paths) == 1:
        return -1

    if len(paths[-1]) == len(paths[-2]):
        print(paths[-2][-1])
        return paths[-2][-1]
    else:
        print(paths[-1][-1])
        return paths[-1][-1]


an_test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
           (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


earliest_ancestor(an_test, 9)
print(earliest_ancestor(an_test, 9))
