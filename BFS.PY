from collections import deque

def breadth_first_search(graph, start, goal):
    queue = deque([(start, [start])])  
    visited = set() 

    while queue:
        current, path = queue.popleft()  

        if current == goal:
            return " -> ".join(path)  

        if current not in visited:
            visited.add(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))  

    return "No path found"

def get_user_graph():
    graph = {}
    num_nodes = int(input("Enter number of nodes in the graph: "))

    for _ in range(num_nodes):
        node = input("Enter node name: ").strip()
        neighbors = input(f"Enter neighbors of {node} (comma separated): ").strip().split(',')
        graph[node] = [n.strip() for n in neighbors if n.strip()]  

    return graph

graph = get_user_graph()
start_node = input("Enter the start node: ").strip()
goal_node = input("Enter the goal node: ").strip()

result = breadth_first_search(graph, start_node, goal_node)
print("Path:", result)