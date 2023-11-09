import random

from TestCase import TestCase
from procedural import eval_sexpression

LENGTH_OF_GENE_LOWER_BOUND = 4
LENGTH_OF_GENE_UPPER_BOUND = 10

class GeneticAlgorithm:
    def __init__(self, num_generations, pool_size, num_parents_mating, mutation_chance, test_cases, tokens):
        self.num_generations = num_generations
        self.pool_size = pool_size
        self.num_parents_mating = num_parents_mating
        self.mutation_chance = mutation_chance
        self.test_cases = test_cases
        self.tokens = tokens
        self.tokens_list = list(tokens)

    def create_candidate(self, tokens):
        # Note: Must use all tokens in the form of a list for random.choice to work.
        tokens_list = list(tokens)

        # First randomly generate length of candidate
        length = random.randint(LENGTH_OF_GENE_LOWER_BOUND, LENGTH_OF_GENE_UPPER_BOUND)

        # Then, generate random tokens. Keep track of open and closed brackets.
        candidate = ['(']
        open_brackets_count = 0
        i = 1
        while i < length - 1:
            if length - i == open_brackets_count:
                break
            gene = random.choice(tokens_list)
            if gene == '(':
                open_brackets_count += 1
            elif gene == ')':
                if open_brackets_count == 0:
                    continue
                open_brackets_count -= 1
            candidate.append(gene)
            i += 1

        while open_brackets_count > 0:
            candidate.append(')')
            open_brackets_count -= 1

        candidate.append(')')

        return candidate

    def create_initial_pool(self, tokens):
        candidates_pool = []
        for _ in range(self.pool_size):
            candidates_pool.append(self.create_candidate(tokens))

        return candidates_pool

    def get_fitness(self, candidate):
        # First check whether the program is valid
        candidate_string = ' '.join([str(c) for c in candidate])
        result = eval_sexpression(candidate_string)
        if result.startswith("Invalid"):
            return -1

        # Then count how many test cases it passes
        passed_test_cases = 0
        for test_case in self.test_cases:
            inp = test_case.get_input()
            candidate_string += f" ( factorial {inp} )"
            try:
                output = eval_sexpression(candidate_string)
            except:
                # Broken program
                return -1
            if test_case.get_output() == output:
                passed_test_cases += 1

        # Return percentage of passed test cases
        return passed_test_cases / len(self.test_cases)

    def cross_over(self, parent1, parent2):
        length1, length2 = len(parent1), len(parent2)
        index1, index2 = 0, 0

        offspring = []
        while index1 < length1 and index2 < length2:
            if random.randint(0, 1) == 0:
                offspring.append(parent1[index1])
            else:
                offspring.append(parent2[index2])

            index1 += 1
            index2 += 1

        while index1 < length1:
            offspring.append(parent1[index1])
            index1 += 1

        while index2 < length2:
            offspring.append(parent2[index2])
            index2 += 1

        return offspring

    def mutate(self, candidate):
        should_mutate = random.random()
        if should_mutate > self.mutation_chance:
            return candidate

        gene_idx = random.randint(0, len(candidate) - 1)
        token_idx = random.randint(0, len(self.tokens) - 1)
        candidate[gene_idx] = self.tokens_list[token_idx]

        return candidate


    def run(self):
        print(f"[Algorithm start]")

        # Initialise candidates pool
        candidates_pool = self.create_initial_pool(self.tokens)

        for gen_id in range(self.num_generations):
            print(f"[Generation {gen_id}]")

            # Take candidates pool and compute their fitness
            fitness_scores = [(self.get_fitness(candidate), i) for i, candidate in enumerate(candidates_pool)]

            # Sort descending based on fitness
            fitness_scores_sorted = sorted(fitness_scores, key=lambda x: x[0], reverse=True)
            print(fitness_scores_sorted)

            new_candidates_pool = []

            # Cross-over
            for i in range(0, self.num_parents_mating, 2):
                parent1, parent2 = candidates_pool[fitness_scores[i][1]], candidates_pool[fitness_scores[i+1][1]]

                offspring = self.cross_over(parent1, parent2)

                # Mutate
                offspring = self.mutate(offspring)
                new_candidates_pool.append(offspring)

                if len(new_candidates_pool) == self.pool_size:
                    # Stop if new candidates pool is full
                    break

            # Add top parents to new_candidates_pool
            candidates_to_add = self.pool_size - len(new_candidates_pool)
            top_parents_next_generation = [candidates_pool[s[1]] for s in fitness_scores_sorted[:candidates_to_add]]
            new_candidates_pool += top_parents_next_generation

            old_candidates_pool = candidates_pool
            candidates_pool = new_candidates_pool
            random.shuffle(candidates_pool)

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
        TestCase(1, 1),
        TestCase(2, 2),
        TestCase(3, 6),
        TestCase(4, 24)
    ]

    # Start from reference program to extract tokens (or add them manually)
    tokens = {'factorial', 'cond', 1, '*', '-', 'zerop', 'n', '(', ')'}

    # Create Genetic Algorithm instance
    ga = GeneticAlgorithm(
        num_generations=100,
        pool_size=50,
        num_parents_mating=20,
        mutation_chance=0.3,
        test_cases=test_cases,
        tokens=tokens
    )
    ga.run()


if __name__ == "__main__":
    random.seed(0)
    main()
