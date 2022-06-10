
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    root.add_child(laptop)
    laptop.add_child(TreeNode("Acer"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Lenovo"))

    cellphone=TreeNode("cell phone")
    root.add_child(cellphone)
    cellphone.add_child(TreeNode("Apple"))
    cellphone.add_child(TreeNode("Infinix"))
    cellphone.add_child(TreeNode("MI"))

    tv=TreeNode("TV")
    root.add_child(tv)
    tv.add_child(TreeNode("sony"))
    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("LG"))
    
    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
    
