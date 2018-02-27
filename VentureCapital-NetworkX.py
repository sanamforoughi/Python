import networkx
import networkx as nx
import matplotlib.pyplot as plt

'''orginal code from: https://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python
Sequoia Capital: Accel, 500Startups, NEA, ycombinator,NorwestVP, GVTeam,a16z
Accel Partners: sequoia, ycombinator,insightpartners,GVTeam,a16z
500 Startups: sequoia, Accel,NEA,ycombinator,GVTeam,a16z
New Enterprise Associates: sequoia, Accel,500Startups,ycombinator,lightspeedvp,GVTeam,NorwestVP,a16z
Y Combinator: sequoia
Tencent Holdings
*Insight Venture Partners: Accel,a16z
*Lightspeed Venture Partners: Accel,NorwestVP
GV: sequoia, Accel
*Norwest Venture Partners: NEA,lightspeedvp
SoftBank: 0
Andreessen Horowitz: 0'''


G = nx.DiGraph()
G.add_edges_from(
    [('Sequoia', 'Accel'), ('Sequoia ', '500Startups'),
    ('Sequoia ', 'NEA'), ('Sequoia ', ' YCombinator'),
    ('Sequoia ', 'NorwestVP'), ('Sequoia', 'GoogleVentures'),
    ('Sequoia ', 'a16z'), ('Accel', 'Sequoia '),
    ('Accel ', ' YCombinator'), ('Accel ', 'InsightVP'),
    ('Accel ', 'GoogleVentures'), ('Accel ', 'a16z'),
    ('500Startups', 'Sequoia '), ('500Startups', 'Accel '),('500Startups', 'NEA'),
    ('500Startups', 'Ycombinator'),('500Startups', 'GoogleVentures'),('500Startups', 'a16z'),
    ('NEA', 'Sequoia '),('NEA', 'Accel'), ('NEA', '500Startups'), 
    ('NEA', 'YCombinator'), ('NEA', 'LightspeedVP'),('NEA', 'GoogleVentures'),
    ('NEA', 'NorwestVP'), ('NEA', 'a16z'),('YCombinator', 'Sequoia'), ('InsightVP', 'Accel'), ('InsightVP', 'a16z'),
    ('LightspeedVP', 'Accel'), ('LightspeedVP', 'NorwestVP'), ('NorwestVP', 'NEA'), ('NorwestVP','lightspeedvp')]) 


val_map = {'Sequoia': 0.7,
           'Accel': 0.5,
           '500Startups': 0.6,
           'NEA': 0.8,
           'YCombinator': 0.1,
           'Tencent': 0,
           'InsightVP': 0.2,
           'LightspeedVP': 0.2,
           'GoogleVentures': 0.2,
           'NorwestVP': 0.2,
           'SoftBank': 0.0,
           'a16z': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = [('Sequoia', '500Startups'), ('YCombinator', '500Startups')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()


XX

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# fix sequoia, y combinator and accel: 

'''nx.draw(G,with_labels=True)
plt.draw()
plt.show()'''

G = nx.DiGraph()

#add your companies
G.add_node('Sequoia')
G.add_node('Accel')
G.add_node('500Startups')
G.add_node('NEA')
G.add_node('YCombinator')
G.add_node('InsightVP')
G.add_node('LightspeedVP')
G.add_node('GoogleVentures')
G.add_node('NorwestVP')
G.add_node('Tencent')
G.add_node('SoftBank')
G.add_node('a16z')


G.add_edges_from(
    [('Sequoia', 'Accel'), ('Sequoia', '500Startups'),
    ('Sequoia', 'NEA'),
    ('Sequoia', 'NorwestVP'), ('Sequoia', 'GoogleVentures'),
    ('Sequoia', 'a16z'), ('Accel', 'InsightVP'),
    ('Accel', 'GoogleVentures'), ('Accel', 'a16z'),
    ('500Startups', 'NEA'),
    ('500Startups', 'GoogleVentures'),('500Startups', 'a16z'),
    ('NEA', 'Sequoia'),('NEA', 'YCombinator'), ('NEA', 'LightspeedVP'),('NEA', 'GoogleVentures'),
    ('NEA', 'NorwestVP'), ('NEA', 'a16z'), ('InsightVP', 'a16z'),
    ('LightspeedVP', 'Accel'), ('LightspeedVP', 'NorwestVP'), ('NorwestVP', 'NEA'), ('NorwestVP','LightspeedVP')]) 

val_map = {'Sequoia': 0.7,
           'Accel': 0.5,
           '500Startups': 0.6,
           'NEA': 0.8,
           'YCombinator': 0.1,
           'Tencent': 0,
           'InsightVP': 0.2,
           'LightspeedVP': 0.2,
           'GoogleVentures': 0.2,
           'NorwestVP': 0.2,
           'SoftBank': 0.0,
           'a16z': 0.0}

'''val_map = {'Accel': 1.0,
           'NEA': 0.5714285714285714,
           'Tencent': 0.0}'''

values = [val_map.get(node, 0) for node in G.nodes()]

# Specify the edges you want here
red_edges = [('YCombinator', 'Sequoia')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()

'''

# Specify the edges you want here
red_edges = [('NEA', 'Sequoia'), ('Accel', 'YCombinator')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()

# Finalement tu as utilise celui ci:

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# fix sequoia, y combinator and accel: 

'''nx.draw(G,with_labels=True)
plt.draw()
plt.show()'''

G = nx.DiGraph()

#add your companies
G.add_node('Sequoia')
G.add_node('Accel')
G.add_node('500Startups')
G.add_node('NEA')
G.add_node('YCombinator')
G.add_node('InsightVP')
G.add_node('LightspeedVP')
G.add_node('GoogleVentures')
G.add_node('NorwestVP')
G.add_node('Tencent')
G.add_node('SoftBank')
G.add_node('a16z')


G.add_edges_from(
    [('Sequoia', 'Accel'), ('Sequoia', '500Startups'),
    ('Sequoia', 'NEA'),
    ('Sequoia', 'NorwestVP'), ('Sequoia', 'GoogleVentures'),
    ('Sequoia', 'a16z'), ('Accel', 'InsightVP'),
    ('Accel', 'GoogleVentures'), ('Accel', 'a16z'),
    ('500Startups', 'NEA'),
    ('500Startups', 'GoogleVentures'),('500Startups', 'a16z'),
    ('NEA', 'Sequoia'),('NEA', 'YCombinator'), ('NEA', 'LightspeedVP'),('NEA', 'GoogleVentures'),
    ('NEA', 'NorwestVP'), ('NEA', 'a16z'), ('InsightVP', 'a16z'),
    ('LightspeedVP', 'Accel'), ('LightspeedVP', 'NorwestVP'), ('NorwestVP', 'NEA'), ('NorwestVP','LightspeedVP')]) 

val_map = {'Sequoia': 0.70,
           'Accel': 0.50,
           '500Startups': 0.60,
           'NEA': 0.80,
           'YCombinator': 0.10,
           'Tencent': 0.00,
           'InsightVP': 0.20,
           'LightspeedVP': 0.20,
           'GoogleVentures': 0.20,
           'NorwestVP': 0.2,
           'SoftBank': 0.0,
           'a16z': 0.0}

'''val_map = {'Accel': 1.0,
           'NEA': 0.5714285714285714,
           'Tencent': 0.0}'''

values = [val_map.get(node) for node in G.nodes()]

# Specify the edges you want here
red_edges = [('YCombinator', 'Sequoia')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 1000)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()

'''

# Specify the edges you want here
red_edges = [('NEA', 'Sequoia'), ('Accel', 'YCombinator')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()
