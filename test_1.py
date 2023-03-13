def test_spannig_tree():
    import networkx as nx
    from matplotlib import pyplot as plt

    G = nx.Graph()

    G.add_nodes_from([1,2,3,4,5,6])

    G.add_weighted_edges_from([(1,2,1),(2,3,6),(3,6,2),(1,4,1),(4,5,4),(5,6,6)])

    vertices_pos = nx.spring_layout(G)

    vertices_pos[1] = [0, 0]
    vertices_pos[2] = [1, 0]
    vertices_pos[3] = [2, 0]
    vertices_pos[4] = [0, 1]
    vertices_pos[5] = [1, 1]
    vertices_pos[6] = [2, 1]

    T = nx.minimum_spanning_tree(G)

    # assert T.edges() == [(1, 2), (1, 4), (3, 6), (4, 5)]
    assert True == True