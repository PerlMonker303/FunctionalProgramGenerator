bac_functions = {
    1: {  # fail
        "natural_form": "f(x, y) = (x-3)*(y-3) + 3",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(* ? ?)`(- ? ?)`x`#`#`3`#`#`(- ? ?)`y`#`#`3`#`#`3`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2024/2024_E_c_Matematica_SM_M_mate-info_Model_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3",
            "x", "y",
            "(- ? ?)", "(* ? ?)", "(+ ? ?)"
        },
        "test_cases": [
            ((0, 0), 3),
            ((1, 1), 7),
            ((1, 0), 9),
            ((0, 1), 9),
            ((2, 2), 4),
            ((2, 1), 5),
            ((1, 2), 5),
            ((2, 3), 3),
            ((3, 2), 3),
            ((3, 5), 3),
            ((5, 3), 3),
            ((4, 4), 4)
        ]
    },
    2: {  # fail
        #        *
        #   *       +
        # x   y   x   -
        #           y   *
        #              x  y
        "natural_form": "f(x, y) = xy(x+y-xy)",
        "ideal_form": "(defun my_func (x y) ?)`(* ? ?)`(* ? ?)`x`#`#`y`#`#`(+ ? ?)`x`#`#`(- ? ?)`y`#`#`(* ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2024/2024_E_c_Matematica_SM_M_tehnologic_Model_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "x", "y",
            "(- ? ?)", "(* ? ?)", "(+ ? ?)"
        },
        "test_cases": [
            ((1, 3), 3),
            ((0, 0), 0),
            ((1, 1), 1),
            ((1, 2), 2),
            ((2, 1), 2),
            ((2, 2), 0),
            ((3, 3), -27)
        ]
    },
    3: { # fail
        #    +
        # 1      -
        #    *      *
        #   2  *   3  +
        #     x y    x y
        "natural_form": "f(x, y) = 2xy - 3(x+y) + 1",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`1`#`#`(- ? ?)`(* ? ?)`2`#`#`(* ? ?)`x`#`#`y`#`#`(* ? ?)`3`#`#`(+ ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 14,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2024/2024_E_c_Matematica_SM_M_pedagogic_Model_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1", "2", "3",
            "x", "y",
            "(- ? ?)", "(* ? ?)", "(+ ? ?)"
        },
        "test_cases": [
            ((0, 0), 1),
            ((1, 1), -3),
            ((0, 1), -2),
            ((1, 0), -2),
            ((2, 2), -3),
            ((1, 2), -4),
            ((2, 1), -4)
        ]
    },
    4: { # fail
        #      +
        # xy           -
        #            -   1
        #         2x  y
        "natural_form": "f(x, y) = xy + 2x - y - 1",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`(- ? ?)`(- ? ?)`(* ? ?)`2`#`#`x`#`#`y`#`#`1`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_S2_M_tehnologic_Subiect_07_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1", "2",
            "x", "y",
            "(- ? ?)", "(* ? ?)", "(+ ? ?)"
        },
        "test_cases": [
            ((0, 0), -1),
            ((1, 0), 1),
            ((0, 1), -2),
            ((1, 1), 1),
            ((2, 2), 5),
            ((2, 1), 4),
            ((1, 2), 1),
            ((3, 3), 11)
        ]
    },
    5: { # fail
        "natural_form": "f(x, y) = 3(4-x-y) + xy",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`(* ? ?)`3`#`#`(- ? ?)`(- ? ?)`4`#`#`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_S2_M_pedagogic_Subiect_07_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3", "4",
            "x", "y",
            "(- ? ?)", "(* ? ?)", "(+ ? ?)"
        },
        "test_cases": [
            ((0, 0), 12),
            ((1, 0), 9),
            ((0, 1), 9),
            ((1, 1), 7),
            ((2, 1), 5),
            ((1, 2), 5),
            ((2, 2), 4),
            ((3, 3), 3)
        ]
    },
    6: { # fail
        "natural_form": "f(x, y) = x*x - 4xy + 3y*y",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(- ? ?)`(* ? ?)`x`#`#`x`#`#`(* ? ?)`4`#`#`(* ? ?)`x`#`#`y`#`#`(* ? ?)`3`#`#`(* ? ?)`y`#`#`y`#`#`#",
        "ideal_nr_nodes": 16,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_S1_M_st-nat_Subiect_01_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3", "4",
            "x", "y",
            "(- ? ?)", "(* ? ?)", "(+ ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 1),
            ((0, 1), 3),
            ((1, 1), 0),
            ((2, 1), -1),
            ((1, 2), 5),
            ((2, 2), 0),
            ((3, 3), 0)
        ]
    },
    7: { # fail
        "natural_form": "f(x, y) = (x-4)(y-4) + 4",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(* ? ?)`(- ? ?)`x`#`#`4`#`#`(- ? ?)`y`#`#`4`#`#`4`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_S1_M_tehnologic_Subiect_01_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "4",
            "x", "y",
            "(- ? ?)", "(* ? ?)", "(+ ? ?)"
        },
        "test_cases": [
            ((0, 0), 20),
            ((1, 0), 16),
            ((0, 1), 16),
            ((1, 1), 13),
            ((2, 1), 10),
            ((1, 2), 10),
            ((2, 2), 8),
            ((3, 3), 5)
        ]
    },
    8: {  # FOUND IN 1 generations (pool size 300, parents mating 150, mutation 0.7)
        "natural_form": "f(x, y) = x + y - 4",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`4`#`#`#",
        "ideal_nr_nodes": 6,
        "gene_depth": 4,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_S1_M_pedagogic_Subiect_01_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "4",
            "x", "y",
            "(- ? ?)", "(+ ? ?)"
        },
        "test_cases": [
            ((0, 0), -4),
            ((1, 0), -3),
            ((0, 1), -3),
            ((1, 1), -2),
            ((2, 1), -1),
            ((1, 2), -1),
            ((2, 2), 0),
            ((3, 3), 2)
        ]
    },
    9: {  # FOUND IN 15 generations (pool size 400, parents mating 150, mutation 0.7)
        #    +
        # 4        -
        #        -  y
        #    x*y  x
        "natural_form": "f(x, y) = x * y - x - y + 4",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`4`#`#`(- ? ?)`(- ? ?)`(* ? ?)`x`#`#`y`#`#`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_SS_M_st-nat_Subiect_06_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "4",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 4),
            ((1, 0), 3),
            ((0, 1), 3),
            ((1, 1), 3),
            ((2, 1), 3),
            ((1, 2), 3),
            ((2, 2), 4),
            ((3, 3), 7)
        ]
    },
    10: { # FOUND IN 14 generations (pool size 400, parents mating 150, mutation 0.7)
        "natural_form": "f(x, y) = x*y + x + y - 1",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_SM_M_st-nat_Simulare_XII_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), -1),
            ((1, 0), 0),
            ((0, 1), 0),
            ((1, 1), 2),
            ((2, 1), 4),
            ((1, 2), 4),
            ((2, 2), 7),
            ((3, 3), 14)
        ]
    },
    11: { # fail
        #            -
        #        +      1
        #     -    2y
        #  4xy 3x
        "natural_form": "f(x, y) = 4*x*y - 3*x + 2*y - 1",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`(- ? ?)`(* ? ?)`4`#`#`(* ? ?)`x`#`#`y`#`#`(* ? ?)`3`#`#`x`#`#`x`#`#`(* ? ?)`2`#`#`y`#`#`1`#`#`#",
        "ideal_nr_nodes": 17,
        "gene_depth": 8,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_SM_M_tehnologic_Simulare_XII_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1", "2", "3", "4",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), -1),
            ((1, 0), -4),
            ((0, 1), 1),
            ((1, 1), 2),
            ((2, 1), 3),
            ((1, 2), 8),
            ((2, 2), 13),
            ((3, 3), 32)
        ]
    },
    12: { # FOUND IN 14 generations (pool size 400, parents mating 150, mutation 0.7)
        "natural_form": "f(x, y) = x * y + x + y + 6",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`(+ ? ?)`x`#`#`(+ ? ?)`y`#`#`6`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_SM_M_pedagogic_Simulare_XII_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "6",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 6),
            ((1, 0), 7),
            ((0, 1), 7),
            ((1, 1), 9),
            ((2, 1), 11),
            ((1, 2), 11),
            ((2, 2), 14),
            ((3, 3), 21)
        ]
    },
    13: { # fail
        #       +
        #     +   56
        #   *    *
        #  + 8  x  y
        # x y
        "natural_form": "f(x, y) = x * y + 8 * (x + y) + 56",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`(+ ? ?)`x`#`#`y`#`#`8`#`#`(* ? ?)`x`#`#`y`#`#`56`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 8,
        "source": "https://www.pro-matematica.ro/bacalaureat/2023/2023_E_c_Matematica_SM_M_pedagogic_Model_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "8", "56",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 56),
            ((1, 0), 64),
            ((0, 1), 64),
            ((1, 1), 73),
            ((2, 1), 82),
            ((1, 2), 82),
            ((2, 2), 92),
            ((3, 3), 113)
        ]
    },
    14: { # fail
        #           -
        #      *         *
        #   4     +    3   +
        #       *   1     x y
        #      x y
        "natural_form": "f(x, y) = 4 * (x * y + 1) - 3 * (x + y)",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(* ? ?)`4`#`#`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`1`#`#`(* ? ?)`3`#`#`(+ ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 14,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_S2_M_st-nat_Subiect_07_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1", "3", "4",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 4),
            ((1, 0), 1),
            ((0, 1), 1),
            ((1, 1), 2),
            ((2, 1), 2),
            ((1, 2), 3),
            ((2, 2), 8),
            ((3, 3), 22)
        ]
    },
    15: { # fail
        #           *
        #      x         *
        #              y     -
        #                 +    4
        #                x y
        "natural_form": "f(x, y) = x * y * (x + y - 4)",
        "ideal_form": "(defun my_func (x y) ?)`(* ? ?)`x`#`#`(* ? ?)`y`#`#`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`4`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_S2_M_tehnologic_Subiect_07_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "4",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 0),
            ((0, 1), 0),
            ((1, 1), -2),
            ((2, 1), -2),
            ((1, 2), -2),
            ((2, 2), 0),
            ((3, 3), 18)
        ]
    },
    16: {  # fail
        #          +
        #      *        +
        #     x y     7    *
        #                5    +
        #                   x   y
        "natural_form": "f(x, y) = x * y + 5 * (x + y) + 7",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`(+ ? ?)`7`#`#`(* ? ?)`5`#`#`(+ ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_S2_M_pedagogic_Subiect_07_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "5", "7",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 7),
            ((1, 0), 12),
            ((0, 1), 12),
            ((1, 1), 18),
            ((2, 1), 24),
            ((1, 2), 24),
            ((2, 2), 31),
            ((3, 3), 46)
        ]
    },
    17: { # fail
        #     +
        #   1      -
        #       -     y
        #     *   x
        #   2  *
        #     x y
        "natural_form": "f(x, y) = 2 * x * y - x - y + 1",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`1`#`#`(- ? ?)`(- ? ?)`(* ? ?)`2`#`#`(* ? ?)`x`#`#`y`#`#`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_SM_M_pedagogic_Model_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1", "2",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 1),
            ((1, 0), 0),
            ((0, 1), 0),
            ((1, 1), 1),
            ((2, 1), 2),
            ((1, 2), 2),
            ((2, 2), 5),
            ((3, 3), 13)
        ]
    },
    18: { # FOUND IN 18 generations (pool size 300, parents mating 150, mutation 0.7)
        "natural_form": "f(x, y) = (x + 2*y) * (y + 2*x)",
        "ideal_form": "(defun my_func (x y) ?)`(* ? ?)`(+ ? ?)`x`#`#`(* ? ?)`2`#`#`y`#`#`(+ ? ?)`y`#`#`(* ? ?)`2`#`#`x`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_S1_M_tehnologic_Subiect_01_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "2",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 2),
            ((0, 1), 2),
            ((1, 1), 9),
            ((2, 1), 20),
            ((1, 2), 20),
            ((2, 2), 36),
            ((3, 3), 81)
        ]
    },
    19: { # fail
        "natural_form": "f(x, y) = 5 * x * y + 10 * x + 10 * y + 18",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`18`#`#`(+ ? ?)`(* ? ?)`10`#`#`y`#`#`(+ ? ?)`(* ? ?)`10`#`#`x`#`#`(* ? ?)`5`#`#`(* ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 16,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_SS_M_st-nat_Subiect_03_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "5", "10", "18",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 18),
            ((1, 0), 28),
            ((0, 1), 28),
            ((1, 1), 43),
            ((2, 1), 58),
            ((1, 2), 58),
            ((2, 2), 78),
            ((3, 3), 123)
        ]
    },
    20: {  # FOUND IN 11 generations (pool size 300, parents mating 150, mutation 0.7)
        "natural_form": "f(x, y) = x + y - 6 * x * y",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`(* ? ?)`6`#`#`(* ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_SS_M_tehnologic_Subiect_03_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "6",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 1),
            ((0, 1), 1),
            ((1, 1), -4),
            ((2, 1), -9),
            ((1, 2), -9),
            ((2, 2), -20),
            ((3, 3), -48)
        ]
    },
    21: { # fail
        "natural_form": "f(x, y) = x * y - (x - 1) * (y - 1)",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(* ? ?)`x`#`#`y`#`#`(* ? ?)`(- ? ?)`x`#`#`1`#`#`(- ? ?)`y`#`#`1`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_SS_M_tehnologic_Subiect_03_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), -1),
            ((1, 0), 0),
            ((0, 1), 0),
            ((1, 1), 1),
            ((2, 1), 2),
            ((1, 2), 2),
            ((2, 2), 3),
            ((3, 3), 5)
        ]
    },
    22: {  # FOUND IN 24 generations (pool size 300, parents mating 150, mutation 0.7)
        "natural_form": "f(x, y) = (x + y)(x - 1)(y - 1)",
        "ideal_form": "(defun my_func (x y) ?)`(* ? ?)`(+ ? ?)`x`#`#`y`#`#`(* ? ?)`(- ? ?)`x`#`#`1`#`#`(- ? ?)`y`#`#`1`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_SM_M_tehnologic_Simulare_XII_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 0),
            ((0, 1), 0),
            ((1, 1), 0),
            ((2, 1), 0),
            ((1, 2), 0),
            ((2, 2), 4),
            ((3, 3), 24)
        ]
    },
    23: { # fail
        "natural_form": "f(x, y) = x * y + 2 - (x + y)",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`(+ ? ?)`2`#`#`(* ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 4,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_SM_M_st-nat_Model_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "2",
            "x", "y",
            "(- ? ?)", "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 2),
            ((1, 0), 1),
            ((0, 1), 1),
            ((1, 1), 1),
            ((2, 1), 1),
            ((1, 2), 1),
            ((2, 2), 2),
            ((3, 3), 5)
        ]
    },
    24: {  # FOUND IN 13 generations (pool size 300, parents mating 150, mutation 0.7)
        "natural_form": "f(x, y) = (x * y + 1) * (x + y)",
        "ideal_form": "(defun my_func (x y) ?)`(* ? ?)`(+ ? ?)`x`#`#`y`#`#`(+ ? ?)`1`#`#`(* ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2022/2022_E_c_Matematica_SM_M_tehnologic_Model_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 1),
            ((0, 1), 1),
            ((1, 1), 4),
            ((2, 1), 9),
            ((1, 2), 9),
            ((2, 2), 20),
            ((3, 3), 60)
        ]
    },
    25: {  # FOUND IN 11 generations (pool size 300, parents mating 150, mutation 0.7)
        "natural_form": "f(x, y) = 4 - (1 + x + y)",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`4`#`#`(+ ? ?)`1`#`#`(+ ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 8,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2021/2021_E_c_Matematica_S2_M_st-nat_Subiect_04_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1","4",
            "x", "y",
            "(+ ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), 3),
            ((1, 0), 2),
            ((0, 1), 2),
            ((1, 1), 1),
            ((2, 1), 0),
            ((1, 2), 0),
            ((2, 2), -1),
            ((3, 3), -3)
        ]
    },
    26: { # fail
        "natural_form": "f(x, y) = 3 * x + 4 * y - 25",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`(* ? ?)`3`#`#`x`#`#(* ? ?)`4`#`#`y`#`#`25`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2021/2021_E_c_Matematica_S2_M_tehnologic_Subiect_04_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3","4","25",
            "x", "y",
            "(+ ? ?)", "(- ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), -25),
            ((1, 0), -22),
            ((0, 1), -21),
            ((1, 1), -18),
            ((2, 1), -15),
            ((1, 2), -14),
            ((2, 2), -11),
            ((3, 3), -4)
        ]
    },
    27: { # fail
        #         -
        #     +        3
        #  *     *
        # 4 x   4 y
        "natural_form": "f(x, y) = 4 * x + 4 * y - 3",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`(* ? ?)`4`#`#`x`#`#(* ? ?)`4`#`#`y`#`#`3`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2021/2021_E_c_Matematica_S2_M_pedagogic_Subiect_04_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3","4",
            "x", "y",
            "(+ ? ?)", "(- ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), -3),
            ((1, 0), 1),
            ((0, 1), 1),
            ((1, 1), 5),
            ((2, 1), 9),
            ((1, 2), 9),
            ((2, 2), 13),
            ((3, 3), 21)
        ]
    },
    28: { # fail
        #         +
        #     +        12
        #  *      +
        # 4 x   *   *
        #      4 y x y
        "natural_form": "f(x, y) = x*y + 4*x + 4*y + 12",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`4`#`#`x`#`#`(+ ? ?)`(* ? ?)`4`#`#`y`#`#`(* ? ?)`x`#`#`y`#`#`12`#`#`#",
        "ideal_nr_nodes": 14,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2021/2021_E_c_Matematica_S2_M_pedagogic_Subiect_04_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "4","12",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 12),
            ((1, 0), 16),
            ((0, 1), 16),
            ((1, 1), 21),
            ((2, 1), 26),
            ((1, 2), 26),
            ((2, 2), 32),
            ((3, 3), 45)
        ]
    },
    29: { # FOUND IN 11 generations (pool size 400, parents mating 150, mutation 0.7)
        #         +
        #     +        1
        #  *      x
        # 2 y
        "natural_form": "f(x, y) = x + 2*y + 1",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`2`#`#`y`#`#`x`#`#`12`#`#`#",
        "ideal_nr_nodes": 14,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_Matematica_SS_M_tehnologic_Subiect_01_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1", "2",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 1),
            ((1, 0), 4),
            ((0, 1), 1),
            ((1, 1), 4),
            ((2, 1), 7),
            ((1, 2), 4),
            ((2, 2), 7),
            ((3, 3), 10)
        ]
    },
    30: { # FOUND IN 21 generations (pool size 400, parents mating 150, mutation 0.7)
        #    +
        # 4     +
        #     x    +
        #        y   *
        #           x y
        "natural_form": "f(x, y) = x*y + x + y + 4",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`4`#`#`(+ ? ?)`x`#`#`(+ ? ?)`y`(* ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_tehnologic_Test_20.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "4",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 4),
            ((1, 0), 5),
            ((0, 1), 5),
            ((1, 1), 7),
            ((2, 1), 9),
            ((1, 2), 9),
            ((2, 2), 12),
            ((3, 3), 19)
        ]
    },
    31: { # FOUND IN 1 generations (pool size 400, parents mating 150, mutation 0.7)
        #    +
        # x     -
        #     y    20
        "natural_form": "f(x, y) = x + y - 20",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`x`#`#`(- ? ?)`y`#`#`20`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_20.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "20",
            "x", "y",
            "(+ ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), -20),
            ((1, 0), -19),
            ((0, 1), -19),
            ((1, 1), -18),
            ((2, 1), -17),
            ((1, 2), -17),
            ((2, 2), -16),
            ((3, 3), -14)
        ]
    },
    32: { # fail
        #    +
        # 6      +
        #     *     *
        #    3 x   3 y
        "natural_form": "f(x, y) = 3*x + 3*y + 6",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`6`#`#`(+ ? ?)`(* ? ?)`3`#`#`x`#`#`(* ? ?)`3`#`#`y`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_19.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3", "6",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 6),
            ((1, 0), 9),
            ((0, 1), 9),
            ((1, 1), 12),
            ((2, 1), 15),
            ((1, 2), 15),
            ((2, 2), 18),
            ((3, 3), 24)
        ]
    },
    33: { # FOUND IN 1 generations (pool size 400, parents mating 150, mutation 0.7)
        #         -
        #      +      5
        #    +    y
        #  *  x
        # x y
        "natural_form": "f(x, y) = x*y + x + y - 5",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`x`#`#`y`#`#`5`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_tehnologic_Test_18.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "5",
            "x", "y",
            "(+ ? ?)", "(* ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), -5),
            ((1, 0), -4),
            ((0, 1), -4),
            ((1, 1), -2),
            ((2, 1), 0),
            ((1, 2), 0),
            ((2, 2), 3),
            ((3, 3), 10)
        ]
    },
    34: { # FOUND IN 3 generations (pool size 400, parents mating 150, mutation 0.7)
        #         -
        #      +      90
        #    x    y
        "natural_form": "f(x, y) = x + y - 90",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`90`#`#`#",
        "ideal_nr_nodes": 6,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_tehnologic_Test_17.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "45", "90",
            "x", "y",
            "(+ ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), -90),
            ((1, 0), -89),
            ((0, 1), -89),
            ((1, 1), -88),
            ((2, 1), -87),
            ((1, 2), -87),
            ((2, 2), -86),
            ((3, 3), -84)
        ]
    },
    35: {  # FOUND IN 1 generations (pool size 400, parents mating 150, mutation 0.7)
        #         +
        #      +      x
        #    +    y
        #   x y
        "natural_form": "f(x, y) = x + y + x*y",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(+ ? ?)`x`#`#`y`#`#`y`#`#`x`#`#`#",
        "ideal_nr_nodes": 6,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_17.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 1),
            ((0, 1), 1),
            ((1, 1), 3),
            ((2, 1), 5),
            ((1, 2), 5),
            ((2, 2), 8),
            ((3, 3), 15)
        ]
    },
    36: {  # FOUND IN 1 generations (pool size 400, parents mating 150, mutation 0.7)
        #         -
        #      +      9
        #    x    y
        "natural_form": "f(x, y) = x + y - 9",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`9`#`#`#",
        "ideal_nr_nodes": 6,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_16.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "9",
            "x", "y",
            "(+ ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), -9),
            ((1, 0), -8),
            ((0, 1), -8),
            ((1, 1), -7),
            ((2, 1), -6),
            ((1, 2), -6),
            ((2, 2), -5),
            ((3, 3), -3)
        ]
    },
    37: {  # FOUND IN 9 generations (pool size 400, parents mating 150, mutation 0.7)
        #         +
        #      +      y
        #    *    x
        #   * y
        #  3 x
        "natural_form": "f(x, y) = 3 * x * y + x + y",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`(* ? ?)`3`#`#`x`#`#`y`#`#`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 9,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_tehnologic_Test_13.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 1),
            ((0, 1), 1),
            ((1, 1), 5),
            ((2, 1), 9),
            ((1, 2), 9),
            ((2, 2), 16),
            ((3, 3), 33)
        ]
    },
    38: {  # FOUND IN 4 generations (pool size 400, parents mating 150, mutation 0.7)
        #         +
        #      +      x
        #    *    1
        #   5 y
        "natural_form": "f(x, y) = x + 5*y + 1",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`5`#`#`y`#`#`1`#`#`x`#`#`#",
        "ideal_nr_nodes": 8,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_tehnologic_Test_14.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1", "5",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 1),
            ((1, 0), 2),
            ((0, 1), 6),
            ((1, 1), 7),
            ((2, 1), 8),
            ((1, 2), 12),
            ((2, 2), 13),
            ((3, 3), 19)
        ]
    },
    39: {  # FOUND IN 21 generations (pool size 400, parents mating 150, mutation 0.7)
        #           +
        #        +      x
        #     +    y
        #   *  2
        #  x y
        "natural_form": "f(x, y) = x * y + x + y + 2",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`2`#`#`y`#`#`x`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 7,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_tehnologic_Test_15.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "2",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 2),
            ((1, 0), 3),
            ((0, 1), 3),
            ((1, 1), 5),
            ((2, 1), 7),
            ((1, 2), 7),
            ((2, 2), 10),
            ((3, 3), 17)
        ]
    },
    40: {  # FOUND IN 11 generations (pool size 400, parents mating 150, mutation 0.7)
        #           +
        #        -      2020
        #     x    y
        "natural_form": "f(x, y) = x - y + 2020",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(- ? ?)`x`#`#`y`#`#`2020`#`#`#",
        "ideal_nr_nodes": 6,
        "gene_depth": 4,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_tehnologic_Test_11.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "2020", "1010",
            "x", "y",
            "(+ ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), 2020),
            ((1, 0), 2021),
            ((0, 1), 2019),
            ((1, 1), 2020),
            ((2, 1), 2021),
            ((1, 2), 2019),
            ((2, 2), 2020),
            ((3, 3), 2020)
        ]
    },
    41: { # fail
        #           +
        #        +      x
        #     50    y
        "natural_form": "f(x, y) = x + y + 50",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`x`#`#`y`#`#`2`#`#`#",
        "ideal_nr_nodes": 6,
        "gene_depth": 4,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_13.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "2", "25", "25"
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 50),
            ((1, 0), 51),
            ((0, 1), 51),
            ((1, 1), 52),
            ((2, 1), 53),
            ((1, 2), 53),
            ((2, 2), 54),
            ((3, 3), 56)
        ]
    },
    42: {  # FOUND IN 15 generations (pool size 400, parents mating 150, mutation 0.7)
        #             +
        #         -       1
        #     *      +
        #   x   y   x y
        "natural_form": "f(x, y) = x * y - (x + y) + 1",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(- ? ?)`(* ? ?)`x`#`#`y`#`#`(+ ? ?)`x`#`#`y`#`#`1`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_14.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1",
            "x", "y",
            "(+ ? ?)", "(* ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), 1),
            ((1, 0), 0),
            ((0, 1), 0),
            ((1, 1), 0),
            ((2, 1), 0),
            ((1, 2), 0),
            ((2, 2), 1),
            ((3, 3), 4)
        ]
    },
    43: {  # FOUND IN 1 generations (pool size 400, parents mating 150, mutation 0.7)
        #             -
        #         +       *
        #     x      y   x y
        "natural_form": "f(x, y) = x + y - x*y",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`(* ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 8,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_tehnologic_Test_08.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "x", "y",
            "(+ ? ?)", "(* ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 1),
            ((0, 1), 1),
            ((1, 1), 1),
            ((2, 1), 1),
            ((1, 2), 1),
            ((2, 2), 0),
            ((3, 3), -3)
        ]
    },
    44: {  # FOUND IN 1 generations (pool size 400, parents mating 150, mutation 0.7)
        #             -
        #         +       3
        #     x      y
        "natural_form": "f(x, y) = x + y - 3",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`3`#`#`#",
        "ideal_nr_nodes": 6,
        "gene_depth": 4,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_10.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3",
            "x", "y",
            "(+ ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), -3),
            ((1, 0), -2),
            ((0, 1), -2),
            ((1, 1), -1),
            ((2, 1), 0),
            ((1, 2), 0),
            ((2, 2), 1),
            ((3, 3), 3)
        ]
    },
    45: {  # FOUND IN 1 generations (pool size 400, parents mating 150, mutation 0.7)
        #             -
        #         +       10
        #     x      y
        "natural_form": "f(x, y) = x + y - 10",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`x`#`#`y`#`#`10`#`#`#",
        "ideal_nr_nodes": 6,
        "gene_depth": 4,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_03.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "10",
            "x", "y",
            "(+ ? ?)", "(- ? ?)"
        },
        "test_cases": [
            ((0, 0), -10),
            ((1, 0), -9),
            ((0, 1), -9),
            ((1, 1), -8),
            ((2, 1), -7),
            ((1, 2), -7),
            ((2, 2), -6),
            ((3, 3), -4)
        ]
    },
    46: { # fail
        #             -
        #         +       *
        #       *   y    * y
        #     2  x      3 x
        "natural_form": "f(x, y) = 2 * x + y - 3 * x * y",
        "ideal_form": "(defun my_func (x y) ?)`(- ? ?)`(+ ? ?)`(* ? ?)`2`#`#`x`#`#`y`(* ? ?)`(* ? ?)`3`#`#`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_05.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "2", "3",
            "x", "y",
            "(+ ? ?)", "(- ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 2),
            ((0, 1), 1),
            ((1, 1), 0),
            ((2, 1), -1),
            ((1, 2), -2),
            ((2, 2), -6),
            ((3, 3), -18)
        ]
    },
    47: {  # FOUND IN 5 generations (pool size 400, parents mating 150, mutation 0.7)
        #             +
        #         +       *
        #       *   *    3 y
        #     x  y 3 x
        "natural_form": "f(x, y) = x * y + 3 * x + 3 * y",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`(* ? ?)`3`#`#`x`#`#`(* ? ?)`3`#`#`y`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2020/2020_E_c_matematica_M_pedagogic_Test_05.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "3",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 3),
            ((0, 1), 3),
            ((1, 1), 7),
            ((2, 1), 11),
            ((1, 2), 11),
            ((2, 2), 16),
            ((3, 3), 27)
        ]
    },
    48: {  # FOUND IN 9 generations (pool size 400, parents mating 150, mutation 0.7)
        #             +
        #         +       *
        #       *   x    x y
        #     2  y
        "natural_form": "f(x, y) = x * y + x + 2 * y",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`2`#`#`y`#`#`x`#`#`(* ? ?)`x`#`#`y`#`#`#",
        "ideal_nr_nodes": 10,
        "gene_depth": 6,
        "source": "https://www.pro-matematica.ro/bacalaureat/2019/2019_E_c_Matematica_S2_M_pedagogic_Subiect_07_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "2",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 0),
            ((1, 0), 1),
            ((0, 1), 2),
            ((1, 1), 4),
            ((2, 1), 6),
            ((1, 2), 7),
            ((2, 2), 10),
            ((3, 3), 18)
        ]
    },
    49: { # fail
        #             +
        #         *       1
        #       +   2
        #     +  y
        #    * x
        #   x y
        "natural_form": "f(x, y) = 2 * (x * y + x + y) + 1",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(* ? ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`x`#`#`y`#`#`x`#`#`y`#`#`2`#`#`1`#`#`#",
        "ideal_nr_nodes": 12,
        "gene_depth": 8,
        "source": "https://www.pro-matematica.ro/bacalaureat/2019/2019_E_c_Matematica_S1_M_pedagogic_Subiect_06_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "1", "2",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 1),
            ((1, 0), 3),
            ((0, 1), 3),
            ((1, 1), 7),
            ((2, 1), 11),
            ((1, 2), 11),
            ((2, 2), 17),
            ((3, 3), 31)
        ]
    },
    50: { # FOUND IN 5 generations (pool size 400, parents mating 150, mutation 0.7)
        #             +
        #         +       3
        #       *   x
        #     2  y
        "natural_form": "f(x, y) = x + 2*y + 3",
        "ideal_form": "(defun my_func (x y) ?)`(+ ? ?)`(+ ? ?)`(* ? ?)`2`#`#`y`#`#`x`#`#`3`#`#`#",
        "ideal_nr_nodes": 8,
        "gene_depth": 5,
        "source": "https://www.pro-matematica.ro/bacalaureat/2019/2019_E_c_Matematica_SM_M_tehnologic_Simulare_XII_Subiect_LRO.pdf",
        "first_node": "(defun my_func (x y) ?)",
        "s_expressions": {
            "2", "3",
            "x", "y",
            "(+ ? ?)", "(* ? ?)"
        },
        "test_cases": [
            ((0, 0), 3),
            ((1, 0), 4),
            ((0, 1), 5),
            ((1, 1), 6),
            ((2, 1), 7),
            ((1, 2), 8),
            ((2, 2), 9),
            ((3, 3), 12)
        ]
    },
}