def parse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    nodes = []
    edgesRaw = []
    edges = {}
    destinations = []
    origin = None
    
    section = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith("Nodes:"):
            section = "nodes"
            continue
        elif line.startswith("Edges:"):
            section = "edges"
            continue
        elif line.startswith("Origin:"):
            section = "origin"
            continue
        elif line.startswith("Destinations:"):
            section = "destinations"
            continue
        
        if section == "nodes":
            parts = line.split(": ")
            node_id = int(parts[0])
            coord = tuple(map(int, parts[1][1:-1].split(',')))
            nodes.append(coord)
        
        elif section == "edges":
            parts = line.split("): ")
            edge_nodes = tuple(map(int, parts[0][1:].split(',')))
            weight = int(parts[1])
            edgesRaw.append((edge_nodes[0], edge_nodes[1], weight))
        
        elif section == "origin":
            origin = int(line)
        
        elif section == "destinations":
            destinations = list(map(int, line.split('; ')))
    
    for edge in edgesRaw:
        if edge[0] - 1 not in edges:
            edges[edge[0] - 1] = []
        edges[edge[0] - 1].append((edge[1] - 1, edge[2]))
    
    return nodes, edges, origin - 1, [d - 1 for d in destinations]
