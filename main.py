import random


class GeneticAlgorithm:
    def __init__(self, num_generations, initial_pool_size, num_parents_mating):
        self.num_generations = num_generations
        self.initial_pool_size = initial_pool_size
        self.num_parents_mating = num_parents_mating

    def create_candidate(self, tokens):
        # Must use all tokens
        return None

    def create_initial_pool(self, tokens):
        candidates_pool = []
        for _ in range(self.initial_pool_size):
            candidates_pool.append(self.create_candidate(tokens))

        return candidates_pool

    def run(self):
        print(f"[Algorithm start]")

        # Start from reference program to extract tokens (or add them manually)
        tokens = set({'+', 1, 2})

        # Initialise candidates pool
        candidates_pool = self.create_initial_pool(tokens)

        for gen_id in range(self.num_generations):
            print(f"[Generation {gen_id}]")
            pass

        # TODO add more

        print(f"[Algorithm end]")


def main():
    ga = GeneticAlgorithm(
        num_generations=1000,
        initial_pool_size=1000,
        num_parents_mating=100,
    )
    ga.run()


if __name__ == "__main__":
    main()
