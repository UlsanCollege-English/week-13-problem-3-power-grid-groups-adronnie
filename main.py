def count_power_groups(stations, lines):
    # Build adjacency list for all stations (include isolated stations)
    graph = {s: set() for s in stations}

    # Add undirected edges
    for a, b in lines:
        graph[a].add(b)
        graph[b].add(a)

    visited = set()
    groups = 0

    # DFS for each unvisited station
    for station in stations:
        if station not in visited:
            # New connected component
            groups += 1

            # Explore it using a stack
            stack = [station]
            visited.add(station)

            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

    return groups
