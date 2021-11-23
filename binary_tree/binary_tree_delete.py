# Given a binary search tree
# and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):

    # Base Case
    if root is None:
        return root

    # Recursive calls for ancestors of
    # node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root

    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        return root

    # We reach here when root is the node
    # to be deleted.

    # If root node is a leaf node

    if root.left is None and root.right is None:
        return None

    # If one of the children is empty

    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp

    # If both children exist

    succParent = root

    # Find Successor

    succ = root.right

    while succ.left != None:
        succParent = succ
        succ = succ.left

    # Delete successor.Since successor
    # is always left child of its parent
    # we can safely make successor's right
    # right child as left of its parent.
    # If there is no succ, then assign
    # succ->right to succParent->right
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    # Copy Successor Data to root

    root.key = succ.key

    return root
