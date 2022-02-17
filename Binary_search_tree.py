class Binary_Search_tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

################# add data ########################

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data) 
            else:
                self.left = Binary_Search_tree(data)

        else:
            if self.right:
                self.right.add_child(data) 
            else:
                self.right = Binary_Search_tree(data)


    ##################### in order traversal ###################
    
    def in_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            left_elements = self.left.in_order_traversal()

            elements += left_elements

        # visit root element
        elements.append(self.data)

        # visit right subtree
        if self.right:
            right_elements = self.right.in_order_traversal()

            elements += right_elements
        return elements

    ############################ pre order traversal ##########################

    def pre_order_traversal(self):
        elements = []

        # visit root element
        elements.append(self.data)

        # visit left subtree
        if self.left:
            left_elements = self.left.in_order_traversal()

            elements += left_elements

        # visit right subtree
        if self.right:
            right_elements = self.right.in_order_traversal()

            elements += right_elements
        return  elements
    
    ###################### post order traversal #############################

    def post_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            left_elements = self.left.in_order_traversal()

            elements += left_elements

        # visit right subtree
        if self.right:
            right_elements = self.right.in_order_traversal()

            elements += right_elements

        # visit root element
        elements.append(self.data)
        return  elements

    ################## search method #########################

    def search(self,val):
        if self.data == val:
            return "right value"
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return "wrong value"
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return "wrong value"

    ################## delete method ###########################

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
                if self.right:
                    self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val =self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()    
 
    ########### build tree ##################################

def build_tree(elements):
    print("building tree",elements)
    root = Binary_Search_tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root


if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    root = build_tree(numbers)
    print("in order traversal =",root.in_order_traversal())
    print("pre order traversal=",root.pre_order_traversal())
    print("post order traversal=",root.post_order_traversal())
    n = int(input("Enter search value ="))
    print(root.search(n))
    b = int(input("enter delete value ="))
    delete_element = root.delete(b)
    print("modified list",root.in_order_traversal())
    
