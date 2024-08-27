import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def add_edges(graph):
    print("Enter edges in the format 'node1 node2 weight'. Type 'done' when finished:")
    while True:
        edge_input = input().strip()
        if edge_input == 'done':
            break
        node1, node2, weight = edge_input.split()
        node1, node2 = node1.strip(), node2.strip()  # Strip any extra spaces
        weight = int(weight.strip())
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = weight
        graph[node2][node1] = weight  # Comment this line if the graph is directed

def main():
    graph = {}
    
    # Number of nodes
    num_nodes = int(input("Enter the number of nodes: ").strip())

    # Adding edges
    add_edges(graph)
    
    # Starting node
    start_node = input("Enter the starting node: ").strip()

    # Run Dijkstra's algorithm
    distances = dijkstra(graph, start_node)

    # Display distances
    print("\nShortest distances from node", start_node, ":")
    for node, distance in distances.items():
        print(f"Node {node}: {distance}")

    # Visualization using networkx
    G = nx.Graph()
    for node1 in graph:
        for node2, weight in graph[node1].items():
            if not G.has_edge(node1, node2):
                G.add_edge(node1, node2, weight=weight)
    
    pos = nx.spring_layout(G, seed=42)  # Seed for reproducible layout
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(12, 8))  # Set the figure size
    nx.draw_networkx_nodes(G, pos, node_color='lightcoral', node_size=700, edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')
    
    plt.title("Graph Visualization with Dijkstra's Algorithm", fontsize=18)
    plt.axis('off')  # Hide the axes
    plt.show()

if __name__ == "__main__":
    main()
