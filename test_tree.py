import Tree as tree

n = tree.Node("a")
n.add("b")
n.add("c")
n2 = tree.Node("a")
print(n.is_full())

tree = tree.Tree()

tree.create(5)
tree.draw()
print("-------------")
tree.head.draw()
