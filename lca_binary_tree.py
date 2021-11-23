class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Python Program for Lowest Common Ancestor in a Binary Tree
# O(n) solution to find LCS of two given values n1 and n2

# A binary tree node
# Enter your code here. Read input from STDIN. Print output to STDOUT
def pathFinder(root, path, k):
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root)

    if root.info == k:
        return True

    # Check if k is found in left or right sub-tree
    if (root.left != None and pathFinder(root.left, path, k)) or\
            (root.right != None and pathFinder(root.right, path, k)):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False
    path.pop()
    return False


'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''


# Returns LCA if node n1 , n2 are present in the given
# binary tree otherwise return -1
def lca(root, v1, v2):
    # Enter your code here
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if not pathFinder(root, path1, v1) or not pathFinder(root, path2, v2):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i].info != path2[i].info:
            break
        i = i + 1

    return path1[i - 1]


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
