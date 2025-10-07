from suffix_array import Node, SuffixTreeAndArray

tree = SuffixTreeAndArray("banana")
print(tree.search("ban"))
print(tree.search("baa"))
print(tree.suffix_array())