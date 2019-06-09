from node import Node

class Graph(object):
    """docstring for Graph"""
    def __init__(self, description="default graph", is_directional=False, nodes=None, edges=None):
        super(Graph, self).__init__()
        self.description = description
        self.is_directional = is_directional
        self.nodes = {}
        self.build_nodes(nodes)
        self.build_edges(edges)

    def __str__(self):
        return self.description

    def add_node(self, node):
        if node.value not in self.nodes.keys():
            self.nodes[node.value] = node
            node.sinalize_graph(self)
        else:
            # node alright in graph
            pass

    def add_edge(self, edge):
        invalid_edge = False
        if edge.origin.value not in self.nodes.keys():
            invalid_edge = True
        elif edge.destiny.value not in self.nodes.keys():
            invalid_edge = True
        else:
            # edge is valid
            pass

        if invalid_edge:
            raise Exception("Invalid edge")
        else:
            self.nodes[edge.origin.value].add_edge(edge)
            if not self.is_directional:
                self.nodes[edge.destiny.value].add_edge(edge.reverse())
            else:
                pass

    def build_edges(self, edges):
        if edges:
            for edge in edges:
                if type(edge) == type([]):
                    self.build_edges(edge)
                else:
                    self.add_edge(edge)
        else:
            pass

    def build_nodes(self, nodes):
        if nodes:
            for node in nodes:
                if type(node) == type([]):
                    self.build_nodes(node)
                else:
                    self.add_node(node)
        else:
            pass

    def reverse(self):
        new_nodes = [Node(x) for x in self.nodes.keys()]
        new_edges = [x.reverse() for y in self.nodes.keys() for x in self.nodes[y].edges]
        new_graph = Graph("Reverse for {}".format(self.description), nodes=new_nodes, edges=new_edges, is_directional=self.is_directional)
        return new_graph

    def bfs(self, origin_value=None, destiny_value=None):
        reachable_nodes = {}
        if origin_value != None:
            reachable_nodes[origin_value] = []
            self.nodes[origin_value].process = 1
            self.nodes[origin_value].predecessor = None
            self.nodes[origin_value].distance = 0
            fila = [self.nodes[origin_value]]
            while(fila):
                node, fila = fila[0], fila[1:]
                for adj in node.edges:
                    if adj.destiny.process == 0:
                        adj.destiny.process = 1
                        adj.destiny.predecessor = node
                        adj.destiny.distance = node.distance + 1
                        fila.append(adj.destiny)
                node.process = 2
                reachable_nodes[origin_value].append(node)
            if destiny_value != None:
                reachable = []
                if self.nodes[destiny_value].distance > 0:
                    aux = self.nodes[destiny_value]
                    reachable = aux + reachable
                    while(aux.predecessor):
                        aux = aux.predecessor
                        reachable = aux + reachable
                reachable_nodes[origin_value] = reachable
        else:
            for i in self.nodes.keys():
                reachable_nodes[i] = self.bfs(i, destiny_value)[i]

        return reachable_nodes

    def dfs(self):
        for i in self.nodes.keys():
            setattr(self.nodes[i], "process", 0)
            setattr(self.nodes[i], "predecessor", None)
        time = 0
        for i in self.nodes.keys():
            if self.nodes[i].process == 0:
                self.dfs_visit(self.nodes[i], tempo)

    def dfs_visit(self, node, tempo):
        tempo = tempo + 1
        setattr(node, "distance", tempo)
        node.process = 1
        for adj in node.edges:
            if adj.destiny.process == 0:
                adj.destiny.process = 1
                adj.destiny.predecessor = node
                dfs_visit(adj.destiny, tempo)
        node.process = 2
        tempo = tempo + 1
        setattr(node, "fall_back", tempo)
