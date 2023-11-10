import copy
import random

from test_case import TestCase
from binary_tree import BinaryTreeCoder, Node
from procedural import eval_sexpression

GENE_DEPTH = 7
INSERT_IDEAL_CANDIDATE_IN_INITIAL_POOL = True

class GeneticAlgorithmTree:
    def __init__(self, num_generations=100, pool_size=50, num_parents_mating=20, mutation_chance=0.3, test_cases=[],
                 s_expressions=[]):
        self.num_generations = num_generations
        self.pool_size = pool_size
        self.num_parents_mating = num_parents_mating
        self.mutation_chance = mutation_chance
        self.test_cases = test_cases
        self.s_expressions = s_expressions
        self.s_expressions_list = list(s_expressions)
        self.parameter_counts = {}
        self.btc = BinaryTreeCoder()

        # Compute parameter counts
        for i in range(len(self.s_expressions_list)):
            self.parameter_counts[i] = self.s_expressions_list[i].count("?")

        self.s_expressions_terminals_indices = self.get_terminals(s_expressions)

    def get_terminals(self, s_expressions):
        s_expressions_terminals_indices = []
        for i in range(len(s_expressions)):
            if self.parameter_counts[i] == 0:
                s_expressions_terminals_indices.append(i)
        return s_expressions_terminals_indices

    def create_candidate(self):

        # First randomly generate length of candidate (maximum tree depth)
        max_depth = random.randint(1, GENE_DEPTH)

        # Then, generate random tokens. Keep track of open and closed brackets.
        candidate = []
        st = [("(defun factorial (n) ?)", 0)]  # tuple (value, depth)
        while len(st) > 0:
            gene_i, depth = st.pop()
            if depth > max_depth:
                continue

            if len(candidate) == 0:
                candidate.append(gene_i)  # Exception: gene_i is the value in this case
                parameter_count = 1
            elif gene_i == '#':
                candidate.append(gene_i)
                continue
            else:
                candidate.append(self.s_expressions_list[gene_i])
                parameter_count = self.parameter_counts[gene_i]

            if parameter_count == 0:
                st.append(("#", depth))
                st.append(("#", depth))

            elif parameter_count == 1:
                if depth == max_depth - 1:  # Add terminal at the end level
                    gene_i = random.randint(0, len(self.s_expressions_terminals_indices) - 1)
                    gene_i = self.s_expressions_terminals_indices[gene_i]
                else:
                    gene_i = random.randint(0, len(self.s_expressions_list) - 1)
                st.append(("#", depth))
                st.append((gene_i, depth+1))

            elif parameter_count == 2:
                if depth == max_depth - 1:  # Add terminal at the end level
                    gene_i = random.randint(0, len(self.s_expressions_terminals_indices) - 1)
                    gene_i = self.s_expressions_terminals_indices[gene_i]
                else:
                    gene_i = random.randint(0, len(self.s_expressions_list) - 1)
                st.append((gene_i, depth+1))
                if depth == max_depth - 1:  # Add terminal at the end level
                    gene_i = random.randint(0, len(self.s_expressions_terminals_indices) - 1)
                    gene_i = self.s_expressions_terminals_indices[gene_i]
                else:
                    gene_i = random.randint(0, len(self.s_expressions_list) - 1)
                st.append((gene_i, depth+1))

        return '`'.join(candidate)

    def create_initial_pool(self):
        candidates_pool = []
        for _ in range(self.pool_size):
            candidates_pool.append(self.create_candidate())
        if INSERT_IDEAL_CANDIDATE_IN_INITIAL_POOL:
            candidates_pool = candidates_pool[:-1]
            candidates_pool.append("(defun factorial (n) ?)`(cond ? ?)`(? ?)`(zerop n)`#`#`1`#`#`(t ?)`(* ? ?)`n`#`#`(factorial ?)`(- ? ?)`n`#`#`1`#`#`#`#`#")
        print("[Initial pool]")
        for c in candidates_pool:
            print(c)
        return candidates_pool

    def get_fitness(self, candidate):
        candidate_node = self.btc.decode(candidate)
        s_expr = self.btc.get_lisp_expression(candidate_node)

        # Then count how many test cases it passes
        passed_test_cases = 0
        for test_case in self.test_cases:
            inp = test_case.get_input()
            try:
                output = eval_sexpression(s_expr, add_function_call=True, f_name="factorial", input=inp)
                output = int(output)  # Convert to int to match expected outputs. If not possible, broken program.
                # print(output, '-----', s_expr)
            except:
                # Broken program
                return -1
            if test_case.get_output() == output:
                passed_test_cases += 1

        # Return percentage of passed test cases
        score = passed_test_cases / len(self.test_cases)
        if score > 0.0:
            print("!!!!!!!", s_expr)
        return score

    def cross_over(self, root1, root2):
        # Perform uniform cross-over: go with an index through both trees on the similar nodes (same structure).
        # Then flip a coin and select one node to add to your tree

        if root1 == None and root2 == None:
            return None

        if root1 == None or root1.value == '#':
            return copy.deepcopy(root2)
        if root2 == None or root2.value == '#':
            return copy.deepcopy(root1)

        choose_node = random.randint(0, 1)
        new_node = Node()
        if choose_node == 0:
            new_node.set_value(root1.value)
            new_node.set_is_root_node(root1.get_is_root_node())
            nr_children = root1.get_nr_children()
        else:
            new_node.set_value(root2.value)
            new_node.set_is_root_node(root2.get_is_root_node())
            nr_children = root2.get_nr_children()

        # Add children such that tree remains valid
        if nr_children == 2:
            new_node.right = self.cross_over(root1.right, root2.right)
        if nr_children >= 1:
            new_node.left = self.cross_over(root1.left, root2.left)

        return new_node

    def mutate_shrink(self, node):
        # Shrink mutation
        # input: root node
        # Parse tree: at each node decide whether to replace the subtree starting at this node or not.
        # If not, decide randomly which way to go (if possible).

        if not node or node.value == '#':
            return node

        nr_children = node.get_nr_children()
        select_node = random.randint(0, 1)
        if node.get_is_root_node() == False and (select_node == 1 or nr_children == 0):
            # Replace with random terminal
            gene = node.value
            while gene == node.value:  # Avoid using the same node.value
                gene_i = random.randint(0, len(self.s_expressions_terminals_indices) - 1)
                gene = str(self.s_expressions_list[self.s_expressions_terminals_indices[gene_i]])
            return Node(gene)

        if nr_children == 1:
            node.left = self.mutate_shrink(node.left)
        else:
            choose_direction = random.randint(0, 1)
            if choose_direction == 0:
                node.left = self.mutate_shrink(node.left)
            else:
                node.right = self.mutate_shrink(node.right)
        return node

    def mutate_subtree(self, node):
        # Create a random subtree
        candidate = self.create_candidate()
        root = self.btc.decode(candidate)
        subtree = [root.left]  # always has a left
        # print("SUBTREE:", self.btc.encode(subtree[0]))

        # Find random location to replace this with
        return self.mutate_subtree_recursive(node, subtree)

    def mutate_subtree_recursive(self, node, subtree):
        if subtree[0] == None:
            return node

        nr_children = node.get_nr_children()
        select_node = random.randint(0, 1)
        if node.get_is_root_node() == False and select_node == 1 and nr_children == 1:
            # Node must not be root node, must be selected and have exactly one child
            node.left = subtree[0]
            subtree[0] = None
            return node

        if nr_children == 1:
            node.left = self.mutate_subtree_recursive(node.left, subtree)
        elif nr_children == 2:
            choose_direction = random.randint(0, 1)
            if choose_direction == 0:
                node.left = self.mutate_subtree_recursive(node.left, subtree)
            else:
                node.right = self.mutate_subtree_recursive(node.right, subtree)

        return node


    def run(self):
        print(f"[Algorithm start]")

        # Initialise candidates pool
        candidates_pool = self.create_initial_pool()
        # cache_fitness_scores = {}

        for gen_id in range(self.num_generations):
            print(f"[Generation {gen_id}]")

            # Clean cache if too large
            # if len(cache_fitness_scores) > 10000:
            #     cache_fitness_scores = {}

            # print("[Computing fitness]")
            # fitness_scores = []
            # for i, candidate in enumerate(candidates_pool):
            #     if i not in cache_fitness_scores:
            #         cache_fitness_scores[i] = self.get_fitness(candidate)
            #     fitness_scores.append((cache_fitness_scores[i], i))

            # Take candidates pool and compute their fitness
            fitness_scores = [(self.get_fitness(candidate), i) for i, candidate in enumerate(candidates_pool)]

            # Sort descending based on fitness
            fitness_scores_sorted = sorted(fitness_scores, key=lambda x: x[0], reverse=True)
            print(fitness_scores_sorted)

            new_candidates_pool = []

            # Cross-over
            print("[Cross-over]")
            for i in range(0, self.num_parents_mating, 2):
                parent1, parent2 = candidates_pool[fitness_scores[i][1]], candidates_pool[fitness_scores[i+1][1]]
                root1, root2 = self.btc.decode(parent1), self.btc.decode(parent2)
                offspring = self.cross_over(root1, root2)

                # Mutate
                should_mutate = random.random()
                if should_mutate > self.mutation_chance:
                    # print(f'Offspring before mutation: {self.btc.encode(offspring)}')
                    offspring = self.mutate_subtree(offspring)
                    # print(f'Offspring in between mutations: {self.btc.encode(offspring)}')
                    offspring = self.mutate_shrink(offspring)
                    # print(f'Offspring after mutation: {self.btc.encode(offspring)}')

                offspring_string = self.btc.encode(offspring)
                new_candidates_pool.append(offspring_string)

                if len(new_candidates_pool) == self.pool_size:
                    # Stop if new candidates pool is full
                    break

            # Add top parents to new_candidates_pool
            candidates_to_add = self.pool_size - len(new_candidates_pool)
            top_parents_next_generation = [candidates_pool[s[1]] for s in fitness_scores_sorted[:candidates_to_add]]
            new_candidates_pool += top_parents_next_generation

            old_candidates_pool = candidates_pool
            candidates_pool = new_candidates_pool
            random.shuffle(candidates_pool)  # Shuffle to break order of candidates

        # At the end, print the top 5 candidates
        nr_top_candidates_to_print = 5
        print(f"Top {nr_top_candidates_to_print} candidates: ")
        for i in range(nr_top_candidates_to_print):
            print(old_candidates_pool[fitness_scores_sorted[i][1]])
            self.get_fitness(old_candidates_pool[fitness_scores_sorted[i][1]])
        print(f"[Algorithm end]")


def main():
    # Specify test cases
    test_cases = [
        # TestCase(1, 1),
        # TestCase(2, 2),
        TestCase(3, 6),
        TestCase(4, 24),
        TestCase(5, 120),
        TestCase(6, 720)
    ]

    # Start from predefined s_expressions to use
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

    # Create Genetic Algorithm instance
    ga = GeneticAlgorithmTree(
        num_generations=100,
        pool_size=200,
        num_parents_mating=80,
        mutation_chance=0.5,
        test_cases=test_cases,
        s_expressions=s_expressions
    )
    ga.run()


if __name__ == "__main__":
    random.seed(0)
    main()
