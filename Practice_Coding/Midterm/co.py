def build_tree(levels):
  tree = []
  for i in range(levels):
    subtree = []
    for j in range(i + 1):
      subtree.append(j + 1)
    tree.append(subtree)
  return tree

# Example usage
levels = 5
tree = build_tree(levels)
print(tree)