G1 = {1:[2,3,4,5], 2:[3,5,1], 3:[2,4,1], 4:[3,5,1], 5:[4,2,1]}
G2 = {1:[2,3], 2:[3,1], 3:[2,1,6], 4:[5], 5:[4]}

def degree_sequence(graph):
    list_of_sequence = []

    for vertex in graph.keys():
        list_of_sequence.append(len(graph[vertex]))

    list_of_sequence.sort(reverse=True)
    print(list_of_sequence)

# def vertex_in_vertex(graph, vertex):


def number_of_components(graph):
    visited_vertex = []
    vertex_to_visit = []
    int_of_components = 0

    for vertex in graph.keys():
        visited_vertex.append(vertex)
        vertex_to_visit.extend(graph[vertex])

        for i in vertex_to_visit:
            print(i)
            for y in graph[i]:
                print(y)
                if y not in vertex_to_visit and y not in visited_vertex:
                    vertex_to_visit.append(y)
            if i not in visited_vertex:
                visited_vertex.append(i)
                vertex_to_visit.remove(i)

        int_of_components +=1
        print(vertex_to_visit)



degree_sequence(G1)
number_of_components(G2)