import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Функція для створення графа з вагами
def create_weighted_graph():
    G = nx.Graph()
    # Додавання вершин і ребер із вагами
    G.add_edge("A", "B", weight=4)
    G.add_edge("A", "C", weight=2)
    G.add_edge("B", "C", weight=1)
    G.add_edge("B", "D", weight=5)
    G.add_edge("C", "D", weight=8)
    G.add_edge("C", "E", weight=10)
    G.add_edge("D", "E", weight=2)
    G.add_edge("E", "F", weight=3)
    G.add_edge("F", "G", weight=6)
    return G

# Алгоритм Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней: всі вершини мають нескінченність
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0  # Відстань до початкової вершини - 0
    priority_queue = [(0, start)]  # Черга з пріоритетами (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за відому, пропустити
        if current_distance > distances[current_vertex]:
            continue

        # Перевірка сусідів поточної вершини
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            # Якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Візуалізація графа
def visualize_weighted_graph(graph):
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()

# Основна функція
if __name__ == "__main__":
    # Створення графа
    graph = create_weighted_graph()
    visualize_weighted_graph(graph)  # Візуалізація графа

    # Виконання алгоритму Дейкстри
    start_node = "A"
    shortest_paths = dijkstra(graph, start=start_node)

    # Виведення результатів
    print(f"Найкоротші відстані від вершини {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"До вершини {node}: {distance}")
