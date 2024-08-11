def preorder_traversal_iterative(root):
    '''
        time: O(n), space: O(n)
    '''
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                res.append(node.val)
            else:
                stack.append((node.right, False))    
                stack.append((node.left, False))
                stack.append((node, True))    
    return res

def preorder_traversal_recursive(root):
    '''
        time: O(n), space: O(n)
    '''
    res = []
    def traverse(node):
        if node:
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return res 