from inspect import currentframe, getframeinfo
from pathlib import Path
import yaml

here = Path.cwd()

# Load Containerlab topology from YAML
# with open(here / 'topology.jims.network.yml', 'r') as file:
with open(r'C:\Users\furio\nerdstuff\weird_tools\topology_visualiser\topology.jims.network.yml', 'r') as file:
    topo = yaml.safe_load(file)

# Access the 'topology' key to reach 'nodes' and 'links'
if 'topology' in topo and 'nodes' in topo['topology']:
    dot = "graph G {\n"

    # Add nodes to the graph
    nodes = topo['topology']['nodes']
    for node, node_data in nodes.items():  # Ensure we are iterating over a dictionary
        dot += f'  "{node}" [label="{node} ({node_data["kind"]})"];\n'

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
