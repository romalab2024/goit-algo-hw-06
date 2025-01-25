import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
def create_transport_graph():
    """
    Створює транспортну мережу міста у вигляді графа.
    :return: Об'єкт графа networkX.
    """
    G = nx.Graph()

    # Додаємо вузли (зупинки чи райони)
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    G.add_nodes_from(nodes)

    # Додаємо ребра (дороги) з відстанями
    edges = [
        ('A', 'B', 5),
        ('A', 'C', 3),
        ('B', 'D', 2),
        ('C', 'D', 4),
        ('C', 'E', 7),
        ('D', 'F', 6),
        ('E', 'F', 2)
    ]
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])  # weight — це відстань у км

    return G

# Аналіз графа
def analyze_graph(G):
    """
    Проводить аналіз графа: кількість вузлів, ребер, ступінь вершин.
    """
    print("Характеристики графа:")
    print(f"Кількість вузлів: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")

    print("\nСтупінь кожної вершини:")
    for node, degree in G.degree():
        print(f"Вершина {node}: ступінь {degree}")

# Візуалізація графа
def visualize_graph(G):
    """
    Візуалізує граф із позначенням ваг ребер.
    """
    pos = nx.spring_layout(G)  # Розташування вузлів графа
    plt.figure(figsize=(8, 6))

    # Малюємо вузли та ребра
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12)
    
    # Підписуємо ваги ребер
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Транспортна мережа міста")
    plt.show()

# Основна функція
if __name__ == "__main__":
    # Створюємо граф
    graph = create_transport_graph()

    # Аналізуємо граф
    analyze_graph(graph)

    # Візуалізуємо граф
    visualize_graph(graph)
