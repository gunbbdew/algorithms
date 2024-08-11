def postorder_traversal_iterative(root):
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
                stack.append((node, True))    
                stack.append((node.right, False))    
                stack.append((node.left, False))
    return res

def postorder_traversal_recursive(root):
    '''
        time: O(n), space: O(n)
    '''
    res = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            res.append(node.val)
    traverse(root)
    return res 