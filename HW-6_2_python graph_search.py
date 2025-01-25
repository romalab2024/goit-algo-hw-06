import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Функція для створення графа (завдання 1)
def create_transport_graph():
    G = nx.Graph()
    # Додавання вершин і ребер (наприклад, транспортна мережа міста)
    G.add_edges_from([
        ("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"),
        ("C", "E"), ("D", "E"), ("E", "F"), ("F", "G")
    ])
    return G

# Функція для пошуку шляхів за допомогою DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]  # Використовуємо стек: вершина і шлях до неї
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph[vertex]) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            stack.append((neighbor, path + [neighbor]))
    return None

# Функція для пошуку шляхів за допомогою BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])  # Використовуємо чергу: вершина і шлях до неї
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in set(graph[vertex]) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))
    return None

# Візуалізація графа
def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)
    plt.show()

# Аналіз результатів
def compare_algorithms(graph, start, goal):
    print(f"Пошук із {start} до {goal}:")
    
    dfs_path = dfs(graph, start, goal)
    bfs_path = bfs(graph, start, goal)
    
    print(f"DFS: {dfs_path}")
    print(f"BFS: {bfs_path}")
    
    print("\nПояснення:")
    print("- DFS шукає шлях у глибину, тому може знайти довший або складніший шлях.")
    print("- BFS шукає шлях у ширину, гарантуючи найкоротший шлях у графі без ваг.")
    print("- У реальних задачах вибір алгоритму залежить від вимог до швидкості або якості результату.")

# Основний блок
if __name__ == "__main__":
    graph = create_transport_graph()
    visualize_graph(graph)  # Візуалізація графа
    
    # Виконуємо пошук і порівняння
    compare_algorithms(graph, start="A", goal="G")
