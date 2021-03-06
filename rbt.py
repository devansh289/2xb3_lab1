class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        # left_child = self.left
        # if left_child is not None:
        #     if left_child.right is not None:
        #         left_child.right.parent = self
        #     if self.parent is not None:
        #         left_child.parent = self.parent
        # self.parent = left_child
        # return self
        y = self.left
        self.left = y.right
        if y.right != None:
            y.right.parent = self

        y.parent = self.parent
        if self == self.parent.right:
            self.parent.right = y
        else:
            self.parent.left = y
        y.right = self
        self.parent = y
        # x = self
        # left_child = self.left
        # right_child = self.right
        # self.left = left_child.left
        # self.right = x
        # self.right.left = left_child.right
        # self.right.right = right_child
        # return left_child

    def rotate_left(self):
        # right_child = self.right
        # if right_child is not None:
        #     if right_child.left is not None:
        #         right_child.left.parent = self
        #     if self.parent is not None:
        #         right_child.parent = self.parent
        # self.parent = right_child
        # return self
        y = self.right
        self.right = y.left
        if y.left != None:
            y.left.parent = self

        y.parent = self.parent
        if self == self.parent.left:
            self.parent.left = y
        else:
            self.parent.right = y
        y.left = self
        self.parent = y
        # x = self
        # left_child = self.left
        # right_child = self.right
        # self.left = x
        # self.left.left = left_child
        # self.left.right = right_child.left
        # self.right = right_child.right
        # return right_child


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        # You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        if node != None and node.parent != None and node.parent.is_red():
            if node.get_uncle() is not None and node.get_uncle().is_red():
                node.parent.make_black()
                node.get_uncle().make_black()
                node.parent.parent.make_red()
                node = node.parent.parent
            else:
                # left left case
                if node.parent.left != None and node.parent.parent.left != None:
                    if node.parent.left.is_red() and node.parent.parent.left.is_red():
                        grandfather = node.parent.parent
                        x = node.parent.parent.rotate_right()
                        if grandfather == self.root:
                            self.root = x
                        x.make_black()
                        x.right.make_red()
                        node = node.parent

                # left right case
                if node.parent.right != None and node.parent.parent.left != None:
                    if node.parent.right.is_red() and node.parent.parent.left.is_red():
                        node = node.parent.rotate_left()
                        parent = node.parent
                        node = node.parent.rotate_right()
                        if parent == self.root:
                            self.root = node
                        node.make_black()
                        node.right.make_red()

                # right right case
                if node.parent.right != None and node.parent.parent.right != None:
                    if node.parent.right.is_red() and node.parent.parent.right.is_red():
                        grandfather = node.parent.parent
                        x = node.parent.parent.rotate_left()
                        if grandfather == self.root:
                            self.root = x
                        x.make_black()
                        x.left.make_red()
                        node = node.parent

                # right left case
                if node.parent.left != None and node.parent.parent.right != None:
                    if node.parent.left.is_red() and node.parent.parent.right.is_red():
                        node.parent.rotate_right()
                        parent = node.parent
                        node.parent.rotate_left()
                        if parent == self.root:
                            self.root = node
                        node.make_black()
                        node.left.make_red()

        self.root.make_black()

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
