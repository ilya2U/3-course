import networkx as nx
import matplotlib.pyplot as plt
import random
from matplotlib.pyplot import figure


def print_to_file(s=''):
    print(s)


def probability(probability, str):
    if random.random() < probability:
        print_to_file("Произошло событие: " + str)
        return True
    else:
        return False


def calc_way(way, arr):
    sum = 0
    for i in range(len(way) - 1):
        sum += arr[way[i]][way[i + 1]]
    return sum


def genetic(graph, P_cross, P_mutant, arr):
    for i in range(len(graph)):
        print_to_file("\n")
        if probability(P_cross, "кросовер"):
            row = (lambda x, y=i: x + 1 if x >= y else x)(random.randint(0, len(graph) - 2))
            print_to_file(
                f"{graph[i]}. Сумма = {calc_way(graph[i], arr)}\n{graph[row]}. Сумма = {calc_way(graph[row], arr)}")
            matrix = [list(graph[i]), list(graph[row])]
            point = random.randint(1, len(graph[i]) - 2)

            print_to_file(f"\nТочка кроссовера - {point}")
            tmatrix0 = matrix[0][:point]
            tmatrix1 = matrix[1][:point]

            for g in matrix[1][point:]:
                if g not in tmatrix0:
                    tmatrix0.append(g)
            for g in matrix[1][:point]:
                if g not in tmatrix0:
                    tmatrix0.append(g)

            for g in matrix[0][point:]:
                if g not in tmatrix1:
                    tmatrix1.append(g)
            for g in matrix[0][:point]:
                if g not in tmatrix1:
                    tmatrix1.append(g)

            matrix[0][point:len(tmatrix0)] = tmatrix0[point:len(tmatrix0)]
            matrix[1][point:len(tmatrix1)] = tmatrix1[point:len(tmatrix1)]

            print_to_file(
                f"{matrix[0]}. Сумма = {calc_way(matrix[0], arr)}\n{matrix[1]}. Сумма = {calc_way(matrix[1], arr)}\n")
            if probability(P_mutant, "мутация"):
                for j in range(len(matrix)):
                    point0 = random.randint(1, len(matrix[j]) - 2)
                    point = (lambda x, y=point0: x + 1 if x >= y else x)(random.randint(1, len(matrix[j]) - 3))
                    matrix[j][point0], matrix[j][point] = (matrix[j][point], matrix[j][point0])
                    print_to_file(
                        f"Меняем местами {point0} и {point}\n{matrix[j]}. Сумма = {calc_way(matrix[j], arr)}\n")
            if calc_way(graph[i], arr) < calc_way(matrix[0], arr) and calc_way(matrix[1], arr):
                print_to_file(f"{i} родитель с суммой {calc_way(graph[i], arr)} лучше потомков")
            elif calc_way(matrix[0], arr) < calc_way(matrix[1], arr):
                print_to_file("1 потомок лучше 2 потомка")
                graph[i] = matrix[0]
            else:
                print_to_file("2 потомок лучше 1 потомка")
                graph[i] = matrix[1]
        else:
            print_to_file(f"{i}. {graph[i]}. Сумма = {calc_way(graph[i], arr)}\n")
            if probability(P_mutant, "мутация"):
                point0 = random.randint(1, len(graph[i]) - 2)
                point = (lambda x, y=point0: x + 1 if x >= y else x)(random.randint(1, len(graph[i]) - 3))
                matrix = list(graph[i])
                matrix[point0], matrix[point] = (matrix[point], matrix[point0])
                print_to_file(f"Меняем местами {point0} и {point}\n{matrix}. Сумма = {calc_way(matrix, arr)}\n")
                if calc_way(matrix, arr) < calc_way(graph[i], arr):
                    graph[i] = list(matrix)
                    print_to_file(f"Потомок добавляется. Сумма = {calc_way(graph[i], arr)}")
                else:
                    print_to_file(f"Родитель остается. Сумма = {calc_way(graph[i], arr)}")
    return


def tsp_greedy(graph, start_node):
    num_nodes = len(graph)
    way = [start_node]
    visited = [False] * num_nodes
    visited[start_node] = True

    while len(way) < num_nodes:
        current_node = way[-1]
        min_distance = float('inf')
        next_node = None

        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[current_node][neighbor] < min_distance:
                min_distance = graph[current_node][neighbor]
                next_node = neighbor

        way.append(next_node)
        visited[next_node] = True

    way.append(start_node)
    total_distance = sum(graph[way[i]][way[i + 1]] for i in range(num_nodes))
    return way, total_distance


def draw_tsp_graph(graph, way, color, title):
    figure(figsize=(10, 10))
    plt.title(title)
    num_nodes = len(graph)
    G = nx.Graph()

    options_node = {
        'node_color': 'white',
        'node_size': 1500,
        'linewidths': 3,
        'width': 3,
        'edge_color': 'black',
        'font_size': 30,
        'font_color': 'black',
        'verticalalignment': 'center_baseline',
    }

    for i in range(num_nodes):
        G.add_node(i)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = graph[i][j]
            if weight != 0:
                G.add_edge(i, j, weight=weight)

    pos = nx.circular_layout(G)

    nx.draw(G, pos, with_labels=True, **options_node)

    path_edges = [(way[i], way[i + 1]) for i in range(len(way) - 1)]
    path_edges.append((way[-1], way[0]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color=color, width=5.0)

    edge_labels = {(u, v): str(graph[u][v]) for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=15, font_color=color,
                                 font_family="sans-serif", font_weight="normal", horizontalalignment="center")
    ax = plt.gca()
    ax.collections[0].set_edgecolor('#000000')
    plt.show()


def initialize_diagonal(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0
    return matrix


# timer = time.time()

start_node = 8  # стартовая вершина от 0 до N-1
n = 11  # количество вершин
a = 10  # диапазон от
b = 30  # диапазон до

O_count = 11  # количество особей в популяции
N_repetition = 11  # количество повторов
P_cross = 1.0  # вероятность кроссовера
P_mutant = 1.0  # вероятность мутации

graph = [[random.randint(a, b) for j in range(n)] for i in range(n)]
graph = initialize_diagonal(graph)

for i in range(len(graph[0])):
    for j in range(len(graph[0]) - i):
        graph[j + i][i] = graph[i][j + i]

array = []
for _ in range(O_count):
    row = list(range(0, n))
    del row[start_node]
    random.shuffle(row)
    array.append([start_node] + row + [start_node])

My_Bests = []
count = 1

while True:
    My_gens = []
    print_to_file(f"Поколение: {len(My_Bests) + 1}")
    for i in range(len(array)):
        My_gens.append(calc_way(array[i], graph))
        print_to_file(f"{i + 1}. {array[i]}. Сумма = {My_gens[i]}")
    My_Bests.append(min(My_gens))
    print_to_file(f"Минимальный путь = {My_Bests[len(My_Bests) - 1]}")
    if count == N_repetition:
        for i in range(len(My_Bests)):
            print_to_file(f"Особь {i}. Сумма = {My_Bests[i]}")
        break
    elif My_Bests[len(My_Bests) - 1] == My_Bests[len(My_Bests) - 2]:
        count = count + 1
    else:
        count = 1
    genetic(array, P_cross, P_mutant, graph)

print_to_file("Матрица")
for row in graph:
    print_to_file(row)

print_to_file('\nГенетический алгоритм')
result = []
for i in array:
    current_result = calc_way(i, graph)
    result.append((current_result, i))

min_element = min(result, key=lambda x: x[0])
min_gen = min_element[1]

print_to_file(f"Минимальный путь: {min_gen}")
print_to_file(f"Минимальная сумма: {calc_way(min_gen, graph)}")

path, distance = tsp_greedy(graph, start_node)
print_to_file('\nЖадный алгоритм')
print_to_file(f"Минимальный путь: {path}")
print_to_file(f"Минимальная сумма: {distance}")

draw_tsp_graph(graph, path, 'green', 'Жадный')  # жадный

for row in array:
    if My_Bests[len(My_Bests) - 1] == calc_way(row, graph):
        path = row
        break
draw_tsp_graph(graph, path, 'purple', 'Генетический')  # генетический

# print_to_file(f'Время работы - {round((time.time() - timer), 2)} сек')
