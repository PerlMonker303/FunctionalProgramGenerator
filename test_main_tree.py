import random
from main_tree import GeneticAlgorithmTree


def test_cross_over(ga):
    # Test crossover of trees
    tree1 = "(defun factorial (n) ?)`(factorial ?)`(factorial ?)`(zerop n)`#`#`#`#`#"
    tree2 = "(defun factorial (n) ?)`1`#`#`#"
    root1, root2 = ga.btc.decode(tree1), ga.btc.decode(tree2)
    offspring = ga.cross_over(root1, root2)  # Test using these values
    offspring_string = ga.btc.encode(offspring)
    print(offspring_string)

    # (defun factorial (n) ?)`(factorial ?)`(factorial ?)`#`#`#`#
    # (defun factorial (n) ?)`(factorial ?)`(factorial ?)`#`#`#`#
    # (defun factorial (n) ?)`(factorial ?)`(factorial ?)`(zerop n)`#`#`#`#`#


def test_mutate_subtree(ga):
    string = "(defun factorial (n) ?)`(t ?)`n`#`#`#`#"
    root = ga.btc.decode(string)
    print(ga.btc.encode(root))
    mutation = ga.mutate_subtree(root)
    print(ga.btc.encode(mutation))


if __name__ == '__main__':
    random.seed(1)

    s_expressions = {#"(defun factorial (n) ?)",  # Start with hard-coded version here
        "(cond ? ?)",
        "(? ?)",
        "(zerop n)",
        "1",
        "(t ?)",
        "(* ? ?)",
        "n",
        "(factorial ?)",
        "(- ? ?)",
        "n",
        "1"}

    ga = GeneticAlgorithmTree(
        s_expressions=s_expressions
    )

    test_cross_over(ga)
    test_mutate_subtree(ga)







