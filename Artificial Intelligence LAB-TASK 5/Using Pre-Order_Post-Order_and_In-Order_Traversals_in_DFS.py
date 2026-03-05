tree = {
    "A": ["B","C"],
    "B": ["D","E"],
    "C": ["F","G"],
    "D": [], "E": [], "F": [], "G": []
}

def preorder(node):
    print(node, end=" ")
    for child in tree[node]:
        preorder(child)

def inorder(node):
    children = tree[node]
    if len(children) > 0: inorder(children[0])
    print(node, end=" ")
    if len(children) > 1: inorder(children[1])

def postorder(node):
    for child in tree[node]:
        postorder(child)
    print(node, end=" ")

print("Preorder Traversal:")
preorder("A")
print("\nInorder Traversal:")
inorder("A")
print("\nPostorder Traversal:")
postorder("A")