class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class QueueNode:
    def __init__(self, tree_node):
        self.tree_node = tree_node
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, tree_node):
        new_node = QueueNode(tree_node)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.tree_node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None
        while current:
            parent = current
            if key < current.data:
                current = current.left
            else:
                current = current.right

        if key < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def search(self, key):
        current = self.root
        while current:
            if key == current.data:
                return current
            elif key < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def find_min(self, node):
        while node and node.left:
            node = node.left
        return node

    def delete(self, node, key):
        if not node:
            return None
        if key < node.data:
            node.left = self.delete(node.left, key)
        elif key > node.data:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_larger_node = self.find_min(node.right)
            node.data = min_larger_node.data
            node.right = self.delete(node.right, min_larger_node.data)
        return node

    def mirror(self, node):
        if node:
            node.left, node.right = self.mirror(node.right), self.mirror(node.left)
        return node

    def copy(self, node):
        if not node:
            return None
        new_node = TreeNode(node.data)
        new_node.left = self.copy(node.left)
        new_node.right = self.copy(node.right)
        return new_node

    def height(self, node):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def leaf_nodes(self, node):
        if node:
            if not node.left and not node.right:
                print(node.data, end=' ')
            self.leaf_nodes(node.left)
            self.leaf_nodes(node.right)

    def parent_nodes(self, node):
        if node:
            if node.left and node.right:
                print(f"{node.data} -> {node.left.data}, {node.right.data}")
            elif node.left:
                print(f"{node.data} -> {node.left.data}")
            elif node.right:
                print(f"{node.data} -> {node.right.data}")
            self.parent_nodes(node.left)
            self.parent_nodes(node.right)

    def level_order(self):
        if not self.root:
            return
        q1 = Queue()
        q1.enqueue(self.root)
        while not q1.is_empty():
            q2 = Queue()
            while not q1.is_empty():
                current = q1.dequeue()
                print(current.data, end=' ')
                if current.left:
                    q2.enqueue(current.left)
                if current.right:
                    q2.enqueue(current.right)
            print()
            q1 = q2

#===================== Menu =======================

def main():
    bst = BST()
    while True:
        print("\nMain Menu")
        print("1. Create")
        print("2. Insert")
        print("3. Display Inorder")
        print("4. Search")
        print("5. Delete")
        print("6. Mirror Image")
        print("7. Create Copy")
        print("8. Find Height")
        print("9. Minimum")
        print("10. Display Level-wise")
        print("11. Display Leaf Nodes")
        print("12. Display Parent Nodes")
        print("13. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of nodes: "))
            for _ in range(n):
                key = int(input("Enter data: "))
                bst.insert(key)
        elif choice == 2:
            key = int(input("Enter number to insert: "))
            bst.insert(key)
        elif choice == 3:
            print("Inorder Traversal:")
            bst.inorder(bst.root)
            print()
        elif choice == 4:
            key = int(input("Enter key to search: "))
            result = bst.search(key)
            print(f"{key} found!" if result else f"{key} not found.")
        elif choice == 5:
            key = int(input("Enter node to delete: "))
            bst.root = bst.delete(bst.root, key)
            print(f"{key} deleted.")
        elif choice == 6:
            bst.root = bst.mirror(bst.root)
            print("Mirror image created.")
        elif choice == 7:
            new_root = bst.copy(bst.root)
            print("Copied Tree (inorder):")
            bst.inorder(new_root)
            print()
        elif choice == 8:
            print("Height of Tree:", bst.height(bst.root))
        elif choice == 9:
            min_node = bst.find_min(bst.root)
            print(f"Minimum is: {min_node.data}" if min_node else "Tree is empty.")
        elif choice == 10:
            print("Level-wise Display:")
            bst.level_order()
        elif choice == 11:
            print("Leaf Nodes:")
            bst.leaf_nodes(bst.root)
            print()
        elif choice == 12:
            print("Parent Nodes with Children:")
            bst.parent_nodes(bst.root)
        elif choice == 13:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

