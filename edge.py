class Edge(object):
    """docstring for Edge"""
    def __init__(self, origin, destiny, value=None):
        super(Edge, self).__init__()
        if origin and destiny:
            self.origin = origin
            self.destiny = destiny
        else:
            raise Exception("Values of origin and destiny must be valid Nodes")
        if value:
            self.value = value

    def __str__(self):
        if hasattr(self, "value"):
            return "From: {} To: {} Value: {}".format(self.origin.value, self.destiny.value, self.value)
        return "From: {} To: {}".format(self.origin.value, self.destiny.value)

    def reverse(self):
        if hasattr(self, "value"):
            value = self.value
        else:
            value = None
        return Edge(self.destiny, self.origin, value)
