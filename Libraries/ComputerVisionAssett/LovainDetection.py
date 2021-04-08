from cdlib import algorithms
import networkx as nx
G = nx.karate_club_graph()
coms = algorithms.louvain(G, weight=’weight’, resolution=1., randomize=False)


G = nx.karate_club_graph()
coms = algorithms.leiden(G)


G = nx.karate_club_graph()
coms = algorithms.walktrap(G)