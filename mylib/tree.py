class Tree(object):
    def __init__(self):
        self.children = []
        self.data = None

    def __repr__(self, level=0):
        ret = "-"*level+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
