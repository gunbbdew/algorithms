def inorder_traversal_iterative(root):
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
                stack.append((node, True))    
                stack.append((node.left, False))
    return res

def inorder_traversal_recursive(root):
    '''
        time: O(n), space: O(n)
    '''
    res = []
    def traverse(node):
        if node:
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
    traverse(root)
    return res

def morris_inorder_traversal(root):
    '''
        time: O(n), space: O(1)
        referece: https://medium.com/@mssandeepkamath/morris-tree-traversal-the-o-n-time-and-o-1-space-algorithm-5d2d2d47814a
    '''
    cur = root
    while cur:
        if cur.left:
            prev = cur.left
            while prev.right:
                prev = prev.right

            prev.right = cur
            left = cur.left
            cur.left = None
            cur = left
        else:
            print(cur.val)
            cur = cur.right 