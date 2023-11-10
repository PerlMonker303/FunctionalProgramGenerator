import random

from procedural import eval_sexpression


class Node:
    def __init__(self, value='', is_root_node=False):
        self.value = value
        self.left = None
        self.right = None
        self.is_root_node = is_root_node
        self.fitness_score = None

    def get_nr_children(self):
        return (1 if self.left else 0) + (1 if self.right else 0)

    def get_is_root_node(self):
        return self.is_root_node

    def set_is_root_node(self, is_root_node):
        self.is_root_node = is_root_node

    def set_value(self, value):
        self.value = value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


class BinaryTreeCoder:
    def encode(self, root):
        encoding = []
        # Preorder search
        st = [root]
        while st:
            node = st.pop()
            if not node:
                encoding.append("#")
            else:
                encoding.append(node.value)
                st.append(node.right)
                st.append(node.left)

        return "`".join(str(el) for el in encoding)

    def decode(self, string):
        encoding = string.split("`")
        idx = [0]
        return self.decode_helper(encoding, idx)

    def decode_helper(self, encoding, idx):
        if idx[0] >= len(encoding):
            return None

        if encoding[idx[0]] == "#":
            idx[0] += 1
            return None

        is_root_node = (idx[0] == 0)
        root = Node(encoding[idx[0]], is_root_node)
        idx[0] += 1
        root.left = self.decode_helper(encoding, idx)
        root.right = self.decode_helper(encoding, idx)
        return root

    def get_lisp_expression(self, root):
        if not root:
            return ""

        result = root.value
        result_idx = 0
        current_question_mark = 1
        for i in range(len(root.value)):
            if root.value[i] == '?':
                if current_question_mark == 1:
                    # First '?' occurrence
                    left_value = self.get_lisp_expression(root.left)
                    assert left_value != ""
                    result = result[:result_idx] + left_value + result[result_idx+1:]
                    result_idx += len(left_value) - 1
                    current_question_mark += 1
                else:
                    # Second '?' occurrence
                    right_value = self.get_lisp_expression(root.right)
                    assert right_value
                    result = result[:result_idx] + right_value + result[result_idx+1:]
                    break
            result_idx += 1
        return result


def run_tests():
    print("[Test 1 start]")
    # Test1: Create a basic tree
    #   (+ ?     ?)
    #     /      \
    #   (+ ? ?) (+ ? ?)
    #      /  \    /  \
    #      1   2  3   4
    # expected result: 10
    n1 = Node("(+ ? ?)")
    n2 = Node("(+ ? ?)")
    n3 = Node("1")
    n4 = Node("2")
    n5 = Node("(+ ? ?)")
    n6 = Node("3")
    n7 = Node("4")
    n1.left = n2
    n1.right = n5
    n2.left = n3
    n2.right = n4
    n5.left = n6
    n5.right = n7

    btc = BinaryTreeCoder()
    string = btc.encode(n1)
    expected_string = "(+ ? ?)`(+ ? ?)`1`#`#`2`#`#`(+ ? ?)`3`#`#`4`#`#"
    print(f'Encoded string: {string}')
    assert string == expected_string
    root = btc.decode(string)
    assert root.value == n1.value
    assert root.left.value == n2.value
    assert root.right.value == n5.value
    assert root.left.left.value == n3.value
    assert root.left.right.value == n4.value
    assert root.right.left.value == n6.value
    assert root.right.right.value == n7.value

    # Get LISP code
    s_expr = btc.get_lisp_expression(root)
    expected_s_expr = '(+ (+ 1 2) (+ 3 4))'
    assert s_expr == expected_s_expr
    print(f'Lisp code: {s_expr}')
    eval_result = eval_sexpression(s_expr)
    print(f'Evaluation result: {eval_result}')
    assert int(eval_result) == 10
    print("[Test 1 end]")

    print("[Test 2 start]")
    # Test2: Create another simple tree
    #    (- ? ?)
    #      /   \
    #     5   (/ ? ?)
    #           /   \
    #          10    2
    # expected result: 0
    n1 = Node('(- ? ?)')
    n2 = Node('5')
    n3 = Node('(/ ? ?)')
    n4 = Node('10')
    n5 = Node('2')
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    string = btc.encode(n1)
    expected_string = "(- ? ?)`5`#`#`(/ ? ?)`10`#`#`2`#`#"
    print(f'Encoded string: {string}')
    assert string == expected_string
    print(string)

    root = btc.decode(string)
    assert root.value == n1.value
    assert root.left.value == n2.value
    assert root.right.value == n3.value
    assert root.right.left.value == n4.value
    assert root.right.right.value == n5.value

    s_expr = btc.get_lisp_expression(root)
    expected_s_expr = '(- 5 (/ 10 2))'
    assert s_expr == expected_s_expr
    print(f'Lisp code: {s_expr}')
    eval_result = eval_sexpression(s_expr)
    print(f'Evaluation result: {eval_result}')
    assert int(eval_result) == 0

    # Get LISP code
    s_expr = btc.get_lisp_expression(root)
    print(s_expr)
    print("[Test 2 end]")

    print("[Test 3 start]")
    # Test3: Create a factorial tree
    n1 = Node("(defun factorial (n) ?)")
    n2 = Node("(cond ? ?)")
    n3 = Node("(? ?)")
    n4 = Node("(zerop n)")
    n5 = Node("1")
    n6 = Node("(t ?)")
    n7 = Node("(* ? ?)")
    n8 = Node("n")
    n9 = Node("(factorial ?)")
    n10 = Node("(- ? ?)")
    n11 = Node("n")
    n12 = Node("1")
    n1.left = n2
    n2.left = n3
    n2.right = n6
    n3.left = n4
    n3.right = n5
    n6.left = n7
    n7.left = n8
    n7.right = n9
    n9.left = n10
    n10.left = n11
    n10.right = n12

    string = btc.encode(n1)
    expected_string = "(defun factorial (n) ?)`(cond ? ?)`(? ?)`(zerop n)`#`#`1`#`#`(t ?)`(* ? ?)`n`#`#`(factorial ?)`(- ? ?)`n`#`#`1`#`#`#`#`#"
    print(f'Encoded string: {string}')
    assert string == expected_string
    root = btc.decode(string)
    assert root.value == n1.value
    assert root.left.value == n2.value
    assert root.left.left.value == n3.value
    assert root.left.left.left.value == n4.value
    assert root.left.left.right.value == n5.value
    assert root.left.right.value == n6.value
    assert root.left.right.left.value == n7.value
    assert root.left.right.left.left.value == n8.value
    assert root.left.right.left.right.value == n9.value
    assert root.left.right.left.right.left.value == n10.value
    assert root.left.right.left.right.left.left.value == n11.value
    assert root.left.right.left.right.left.right.value == n12.value

    # Get LISP code
    s_expr = btc.get_lisp_expression(root)
    assert s_expr == '(defun factorial (n) (cond ((zerop n) 1) (t (* n (factorial (- n 1))))))'
    print(f'Lisp code: {s_expr}')
    eval_result = eval_sexpression(s_expr, add_function_call=True, f_name="factorial", input=4)
    print(f'Evaluation result: {eval_result}')
    assert int(eval_result) == 24
    print("[Test 3 end]")

    print("[Test 4 start]")
    # Interesting zerop statement
    # (defun factorial (n) ?)`(zerop n)`#`#`#
    n1 = Node("(defun factorial (n) ?)")
    n2 = Node("(zerop n)")
    n1.left = n2

    string = btc.encode(n1)
    expected_string = "(defun factorial (n) ?)`(zerop n)`#`#`#"
    print(f'Encoded string: {string}')
    assert string == expected_string

    root = btc.decode(string)
    assert root.value == n1.value
    assert root.left.value == n2.value

    # Get LISP code
    s_expr = btc.get_lisp_expression(root)
    assert s_expr == '(defun factorial (n) (zerop n))'
    print(f'Lisp code: {s_expr}')
    eval_result = eval_sexpression(s_expr, add_function_call=True, f_name="factorial", input=4)
    print(f'Evaluation result: {eval_result}')
    assert eval_result == 'NIL '
    print("[Test 4 end]")

    print("[Test 5 start]")
    # Infinite recursion
    # (defun factorial (n) ?)`(zerop n)`#`#`#
    n1 = Node("(defun factorial (n) ?)")
    n2 = Node("(factorial ?)")
    n3 = Node("n")
    n1.left = n2
    n2.left = n3

    string = btc.encode(n1)
    expected_string = "(defun factorial (n) ?)`(factorial ?)`n`#`#`#`#"
    print(f'Encoded string: {string}')
    assert string == expected_string

    root = btc.decode(string)
    assert root.value == n1.value
    assert root.left.value == n2.value
    assert root.left.left.value == n3.value

    # Get LISP code
    s_expr = btc.get_lisp_expression(root)
    assert s_expr == '(defun factorial (n) (factorial n))'
    print(f'Lisp code: {s_expr}')
    eval_result = eval_sexpression(s_expr, add_function_call=True, f_name="factorial", input=1)
    print(f'Evaluation result: {eval_result}')
    assert eval_result == 'Invalid: timeout exception.'
    print("[Test 5 end]")


if __name__ == '__main__':
    random.seed(1)
    run_tests()
