class Tree:
    def __init__(self, label, branches=[]):
        self.label= label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append(' ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

def leaves(t):
    """
    >>> leaves(fib_tree(6))
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
    """
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves

def height(t):
    """
    >>> height(fib_tree(6))
    5
    """
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])

def prune_tree(t, n):
    """
    Prune all sub-trees whose lable is n
    """
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune_tree(b, n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()