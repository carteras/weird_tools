    # Add links to the graph
    links = topo['topology']['links']
    for link in links:
        endpoints = link['endpoints']
        node1, iface1 = endpoints[0].split(":")
        node2, iface2 = endpoints[1].split(":")
        dot += f'  "{node1}" -- "{node2}" [label="{iface1}-{iface2}"];\n'

    dot += "}"

    # Save to .dot file
    with open('topology.dot', 'w') as file:
        file.write(dot)

    print("DOT file created: topology.dot")
else:
    print("Error: 'topology' or 'nodes' key not found in the YAML file")