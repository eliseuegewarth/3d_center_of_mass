class Node(object):
    """docstring for Node"""
    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.edges = []
        self.graphs = []
        self.process= 0
        self.predecessor= None
        self.distance= -1

    def __str__(self):
        return "Node: {} Edges: {}\n\t{}".format( self.value, len(self.edges), "\n\t".join([str(edge) for edge in self.edges]))
    
    def add_edge(self, edge):
        edge_exists = False
        for e in self.edges:
            if edge.destiny == e.destiny:
                edge_exists = True
        if edge_exists:
            pass
        else:
            self.edges.append(edge)

    def sinalize_graph(self, graph):
        if graph not in self.graphs:
            self.graphs.append(graph)

    def update_value(self, value):
        raise Exception("Value can't be updated")
