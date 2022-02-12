class treenode:
    def __init__(self,data):
        self.data=data
        self.children = []
        self.parent= None

    def add_child(self,child):
        child.parent = self
        self.children.append(child) 

    def get_level(self):
        level=0 
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

def build_product_tree():
    root = treenode("Electronics")

    laptop = treenode("laptops")
    laptop.add_child(treenode("mac"))
    laptop.add_child(treenode("surface"))
    laptop.add_child(treenode("Thinkpad"))

    cellphone = treenode("cellphone")
    cellphone.add_child(treenode("samsung"))
    cellphone.add_child(treenode("redmi"))
    cellphone.add_child(treenode("vivo"))

    tv = treenode("tv")
    tv.add_child(treenode("lgo"))
    tv.add_child(treenode("lcd"))
    

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree() 

if __name__ == '__main__':
    build_product_tree()
   