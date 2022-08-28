from collections import defaultdict
import csv


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


# This function searches the user's input-city in the data, exist or not
def does_exist(city, graph):
    for cities in graph:
        if city == cities:
            break
    if cities != city:
        CityNotFoundError(city)
        exit()


# Implement this function to read data into an appropriate data structure.
def build_graph(path):
    my_graph1 = defaultdict(list)
    with open(path, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)arch is an uniformed search algorithm that uses the lowest 
cost to find a path from the sources to the destination and mainly used in 
Artificial Intelligence.
In this algorithm from the starting state we will visit the neig

        for row in reader:
            value = (row["city2"].title(), row["distance"])
            my_graph1[row["city1"].title()].append(value)
            value = (row["city1"].title(), row["distance"])
            my_graph1[row["city2"].title()].append(value)
    return my_graph1


# Calculate path cost
def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        new_cost = int(cost)
        total_cost += new_cost
    return total_cost, path[-1][0]


def uniform_cost_search(graph, start, end):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == end:
            return path
        else:
            neighbour_nodes = graph.get(node, [])
            for (node2, cost) in neighbour_nodes:
                path_new = path.copy()
                path_new.append((node2, cost))
                queue.append(path_new)


def run():
    start_city = input("Enter start city : ").title()
    does_exist(start_city, my_graph)
    destination_city = input("Enter destination city: ").title()
    does_exist(destination_city, my_graph)
    my_path = uniform_cost_search(my_graph, start_city, destination_city)
    print("Shortest path :", my_path)
    print("Distance : ", path_cost(my_path))


# Implement main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    print("Write your path of the road map file ")
    path_of_file = input("or press enter to continue as a default 'cities.csv' : ")
    if path_of_file == "":
        path_of_file = "cities.csv"
    try:
        my_graph = build_graph(path_of_file)
        print("Implementaion is sensitive 'I' - 'İ' and capital 'İ' and lower 'i' are different ")
        run()
    except Exception:
        print("File does not exist or path is wrong check your data")
