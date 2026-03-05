tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [None, 'F'],
    'D': [None, None],
    'E': [None, None],
    'F': [None, None]
}

def dfs_stack(tree, start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node:
            print(node, end=" ")
            right = tree[node][1]
            left = tree[node][0]
            if right:
                stack.append(right)
            if left:
                stack.append(left)

def preorder(tree, node):
    if node:
        print(node, end=" ")
        preorder(tree, tree[node][0])
        preorder(tree, tree[node][1])

def inorder(tree, node):
    if node:
        inorder(tree, tree[node][0])
        print(node, end=" ")
        inorder(tree, tree[node][1])

def postorder(tree, node):
    if node:
        postorder(tree, tree[node][0])
        postorder(tree, tree[node][1])
        print(node, end=" ")

print("DFS Stack:")
dfs_stack(tree, 'A')

print("\nPreorder:")
preorder(tree, 'A')

print("\nInorder:")
inorder(tree, 'A')

print("\nPostorder:")
postorder(tree, 'A')