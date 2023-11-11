import copy
import random

from test_case import TestCase
from binary_tree import BinaryTreeCoder, Node
from procedural import eval_sexpression
from candidate import Candidate, compute_nr_nodes

GENE_DEPTH = 11
INSERT_IDEAL_CANDIDATE_IN_INITIAL_POOL = False
USE_SHRINK_MUTATION = False
USE_SWAP_MUTATION = True


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
        self.next_id = 0

        # Compute parameter counts
        for i in range(len(self.s_expressions_list)):
            self.parameter_counts[i] = self.s_expressions_list[i].count("?")

        self.s_expressions_terminals_indices = self.get_terminals(s_expressions)

    def get_next_id(self):
        self.next_id += 1
        return self.next_id - 1

    def get_terminals(self, s_expressions):
        s_expressions_terminals_indices = []
        for i in range(len(s_expressions)):
            if self.parameter_counts[i] == 0:
                s_expressions_terminals_indices.append(i)
        return s_expressions_terminals_indices

    def create_candidate(self):

        # First randomly generate length of candidate (maximum tree depth)
        max_depth = random.randint(4, GENE_DEPTH)

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

        encoding = '`'.join(candidate)
        root = self.btc.decode(encoding)
        s_expr = self.btc.get_lisp_expression(root)
        candidate = Candidate(self.get_next_id(), encoding, root, s_expr)
        return candidate

    def create_initial_pool(self):
        candidates_pool = []
        for _ in range(self.pool_size):
            candidates_pool.append(self.create_candidate())
        if INSERT_IDEAL_CANDIDATE_IN_INITIAL_POOL:
            candidates_pool = candidates_pool[:-1]
            ideal_candidate_encoding = "(defun factorial (n) ?)`(cond ? ?)`(? ?)`(zerop n)`#`#`1`#`#`(t ?)`(* ? ?)`n`#`#`(factorial ?)`(- ? ?)`n`#`#`1`#`#`#`#`#"
            root = self.btc.decode(ideal_candidate_encoding)
            s_expr = self.btc.get_lisp_expression(root)
            candidates_pool.append(
                Candidate(
                    self.get_next_id(),
                    ideal_candidate_encoding,
                    root,
                    s_expr)
                )
        print("[Initial pool]")
        for c in candidates_pool:
            print(c)
        return candidates_pool

    def get_fitness(self, candidate):

        score = 0

        # Compare tree sizes
        ideal_nr_nodes = 12
        numerator = abs(candidate.get_nr_nodes() - ideal_nr_nodes)
        if numerator == 0:
            score += 1
        else:
            score += 1 / numerator

        # Count number of passed test cases
        passed_test_cases = 0
        for test_case in self.test_cases:
            inp = test_case.get_input()
            try:
                output = eval_sexpression(candidate.get_s_expr(), add_function_call=True, f_name="factorial", input=inp)
                output = int(output)  # Convert to int to match expected outputs. If not possible, broken program.
                # print(output, '-----', s_expr)
            except:
                # Broken program
                return score - 1
            if test_case.get_output() == output:
                passed_test_cases += 1

        # Return percentage of passed test cases
        percentage_tc_passed = passed_test_cases / len(self.test_cases)
        score += percentage_tc_passed
        if percentage_tc_passed > 0.0:
            print("!!!!!!!", candidate.get_s_expr())

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

    def mutate_shrink(self, root, threshold_select):
        should_shrink = [True]
        return self.mutate_shrink_recursive(root, threshold_select, should_shrink)

    def mutate_shrink_recursive(self, node, threshold_select, should_shrink):
        # Shrink mutation
        # input: root node and threshold_select needed for fair chance of shrinking computation
        # Parse tree: at each node decide whether to replace the subtree starting at this node or not.
        # If not, decide randomly which way to go (if possible).

        if not node or node.value == '#' or should_shrink[0] == False:
            return node

        nr_children = node.get_nr_children()
        if node.get_is_root_node() == False and (random.random() < threshold_select or nr_children == 0):
            # Replace with random terminal
            gene = node.value
            while gene == node.value:  # Avoid using the same node.value
                gene_i = random.randint(0, len(self.s_expressions_terminals_indices) - 1)
                gene = str(self.s_expressions_list[self.s_expressions_terminals_indices[gene_i]])
            should_shrink[0] = False
            return Node(gene)

        # ISSUE: too many shrinks, ensure it's done once
        if nr_children == 1:
            node.left = self.mutate_shrink_recursive(node.left, threshold_select, should_shrink)
        else:
            choose_direction = random.randint(0, 1)
            if choose_direction == 0:
                node.left = self.mutate_shrink_recursive(node.left, threshold_select, should_shrink)
            else:
                node.right = self.mutate_shrink_recursive(node.right, threshold_select, should_shrink)
        return node

    def mutate_subtree(self, root, threshold_select):
        # Create a random subtree and replace it with a random node
        candidate = self.create_candidate()
        new_root = candidate.get_root()
        subtree = [new_root.left]  # always has a left
        # print("SUBTREE:", self.btc.encode(subtree[0]))

        # Find random location to replace this with
        return self.mutate_subtree_recursive(root, subtree, threshold_select)

    def mutate_subtree_recursive(self, node, subtree, threshold_select):
        if subtree[0] == None:
            return node

        nr_children = node.get_nr_children()
        if node.get_is_root_node() == False and random.random() < threshold_select and nr_children == 1:
            # Node must not be root node, must be selected and have exactly one child
            node.left = subtree[0]
            subtree[0] = None
            return node

        if nr_children == 1:
            node.left = self.mutate_subtree_recursive(node.left, subtree, threshold_select)
        elif nr_children == 2:
            choose_direction = random.randint(0, 1)
            if choose_direction == 0:
                node.left = self.mutate_subtree_recursive(node.left, subtree, threshold_select)
            else:
                node.right = self.mutate_subtree_recursive(node.right, subtree, threshold_select)

        return node

    def mutate_swap(self, node, threshold_select):
        swapped = [False]
        return self.mutate_swap_recursive(node, None, None, threshold_select, swapped)

    def mutate_swap_recursive(self, node, parent, direction, threshold_select, swapped):
        # direction = 0 (left) or 1 (right)
        # Use a 50-50 percent chance initially
        if not node or node.value == '#' or swapped[0] == True:
            return node

        if parent and random.random() < threshold_select:
            nr_children = node.get_nr_children()
            right_node = node.right
            left_node = node.left
            if right_node and nr_children == right_node.get_nr_children():
                right_node_child_left = right_node.left
                right_node_child_right = right_node.right
                # swap
                if direction == 0:
                    parent.left = right_node
                else:
                    parent.right = right_node
                node.left = right_node_child_left
                node.right = right_node_child_right
                right_node.right = node
                right_node.left = left_node
                swapped[0] = True
                return node

            if left_node and nr_children == left_node.get_nr_children():
                left_node_child_left = left_node.left
                left_node_child_right = left_node.right
                if direction == 0:
                    parent.left = left_node
                else:
                    parent.right = left_node
                node.left = left_node_child_left
                node.right = left_node_child_right
                left_node.left = node
                left_node.right = right_node
                # swap
                swapped[0] = True
                return node

        node.left = self.mutate_swap_recursive(node.left, node, 0, threshold_select, swapped)
        node.right = self.mutate_swap_recursive(node.right, node, 1, threshold_select, swapped)
        return node




    def create_candidates_pool_map(self, candidates_pool):
        # Map candidate id to location in candidates pool
        mp = {}
        for i in range(len(candidates_pool)):
            mp[candidates_pool[i].get_id()] = i
        return mp

    def run(self):
        print(f"[Algorithm start]")

        # Initialise candidates pool
        candidates_pool = self.create_initial_pool()
        cache_fitness_scores = {}

        for gen_id in range(self.num_generations):
            print(f"[Generation {gen_id}]")
            candidates_pool_map = self.create_candidates_pool_map(candidates_pool)

            # Clean cache if too large
            if len(cache_fitness_scores) > 10000:
                cache_fitness_scores = {}

            print("[Computing fitness]")
            fitness_scores = []
            for candidate in candidates_pool:
                candidate_id = candidate.get_id()
                if candidate_id not in cache_fitness_scores:
                    cache_fitness_scores[candidate_id] = self.get_fitness(candidate)
                fitness_scores.append((cache_fitness_scores[candidate_id], candidate_id))

            # Take candidates pool and compute their fitness
            # fitness_scores = [(self.get_fitness(candidate), i) for i, candidate in enumerate(candidates_pool)]

            # Sort descending based on fitness
            fitness_scores_sorted = sorted(fitness_scores, key=lambda x: x[0], reverse=True)
            print(fitness_scores_sorted)

            new_candidates_pool = []

            # Cross-over
            print("[Cross-over]")
            for i in range(0, self.num_parents_mating, 2):
                pos1, pos2 = candidates_pool_map[fitness_scores_sorted[i][1]], candidates_pool_map[fitness_scores_sorted[i+1][1]]
                parent1, parent2 = candidates_pool[pos1], candidates_pool[pos2]
                # parent1, parent2 = candidates_pool[fitness_scores[i][1]], candidates_pool[fitness_scores[i+1][1]]
                offspring = self.cross_over(parent1.get_root(), parent2.get_root())

                # Mutate
                should_mutate = random.random()
                if should_mutate > self.mutation_chance:
                    # Compute number of nodes for fair mutation chance. This way, shrinking can occur at any node more
                    # fair than using a 50% chance.
                    nr_nodes = compute_nr_nodes(self.btc.encode(offspring))
                    threshold_select = 1 / (nr_nodes - 1)

                    # print(f'Offspring before mutation: {self.btc.encode(offspring)}')
                    offspring = self.mutate_subtree(offspring, threshold_select)
                    # print(f'Offspring in between mutations: {self.btc.encode(offspring)}')
                    if USE_SHRINK_MUTATION:
                        offspring = self.mutate_shrink(offspring, threshold_select)

                    if USE_SWAP_MUTATION:
                        offspring = self.mutate_swap(offspring, threshold_select)

                    # print(f'Offspring after mutation: {self.btc.encode(offspring)}')

                offspring_string = self.btc.encode(offspring)

                # Create candidate based on this offspring
                offspring_root = self.btc.decode(offspring_string)
                offspring_s_expr = self.btc.get_lisp_expression(offspring_root)
                offspring_candidate = Candidate(self.get_next_id(), offspring_string, offspring_root, offspring_s_expr)
                new_candidates_pool.append(offspring_candidate)

                if len(new_candidates_pool) == self.pool_size:
                    # Stop if new candidates pool is full
                    break

            # Add top parents to new_candidates_pool
            candidates_to_add = self.pool_size - len(new_candidates_pool)
            top_parents_next_generation = [candidates_pool[candidates_pool_map[s[1]]] for s in fitness_scores_sorted[:candidates_to_add]]
            new_candidates_pool += top_parents_next_generation

            old_candidates_pool = candidates_pool
            candidates_pool = new_candidates_pool
            random.shuffle(candidates_pool)  # Shuffle to break order of candidates

            # Print the top 5 candidates
            self.print_top_n_candidates(5, old_candidates_pool, candidates_pool_map, fitness_scores_sorted)

        # At the end, print the top 5 candidates
        # self.print_top_n_candidates(5, old_candidates_pool, candidates_pool_map, fitness_scores_sorted)
        print(f"[Algorithm end]")

    def print_top_n_candidates(self, n, candidates_pool, candidates_pool_map, fitness_scores_sorted):
        print(f"Top {n} candidates: ")
        for i in range(n):
            candidate = candidates_pool[candidates_pool_map[fitness_scores_sorted[i][1]]]
            print(candidate)


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
        pool_size=1000,
        num_parents_mating=500,
        mutation_chance=0.5,
        test_cases=test_cases,
        s_expressions=s_expressions
    )
    ga.run()


if __name__ == "__main__":
    random.seed(0)
    main()
