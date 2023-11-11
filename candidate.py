
def compute_nr_nodes(encoding):
    # subtract '#' nodes
    pound_nodes = encoding.count('#')
    return encoding.count('`') + 1 - pound_nodes


class Candidate:
    def __init__(self, id, encoding, root, s_expr):
        self.id = id
        self.encoding = encoding
        self.root = root
        self.s_expr = s_expr
        self.nr_nodes = compute_nr_nodes(encoding)

    def set_encoding(self, encoding):
        self.encoding = encoding

    def set_root(self, root):
        self.root = root

    def set_s_expr(self, s_expr):
        self.s_expr = s_expr

    def get_id(self):
        return self.id

    def get_encoding(self):
        return self.encoding

    def get_root(self):
        return self.root

    def get_s_expr(self):
        return self.s_expr

    def get_nr_nodes(self):
        return self.nr_nodes

    def __str__(self):
        return f"(CANDIDATE)[id: {self.id} \n encoding: {self.encoding} \n s_expr: {self.s_expr} \n nr_nodes: {self.nr_nodes}]"
