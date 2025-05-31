

########################################################
# Import
########################################################

from Proj4_utils import *
import math
import random



# Add your imports here if used

################################################################
# 1. Genetic Algorithm
################################################################


def genetic_algorithm(problem, f_thres, ngen=1000):
    population = problem.init_population()
    best = problem.fittest(population, f_thres)

    if best:
        return (-1, best)

    for i in range(ngen):
        population = problem.next_generation(population)
        best = problem.fittest(population, f_thres)
        if best:
            return (i, best)


    best = problem.fittest(population)
    return (ngen, best)


  

################################################################
# 2. NQueens Problem
################################################################


class NQueensProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        super().__init__(n, g_bases, g_len, m_prob)

    
    def init_population(self):
        Curr_Gen = []

        for x in range(self.n):
            Chromosome = []
            for y in range(self.g_len):
                Chromosome.append(random.choice(self.g_bases))

            Curr_Gen.append(tuple(Chromosome))
        return Curr_Gen

    def next_generation(self, population):
        Nxt_Gen = []

        for x in range(self.n):
            dad = random.choice(population)
            mom = random.choice(population)
            child = list(dad)

            self.crossover(child, mom)
            self.mutate(child)

            Nxt_Gen.append(tuple(child))

        return Nxt_Gen

    def mutate(self, chrom):
        if random.random() <= self.m_prob:
            Pos = random.randrange(self.g_len)
            mutation = random.choice(self.g_bases)

            front= tuple(chrom[:Pos])
            back = tuple(chrom[Pos + 1:])
            New_middle = (mutation,)

            chrom = front + New_middle + back
        return chrom


    def crossover(self, chrom1, chrom2):
        Pos = random.randrange(1, self.g_len)
        front = tuple(chrom1[:Pos])
        back = tuple(chrom2[Pos:])
        chrom = front + back
        return chrom

    def fitness_fn(self, chrom):
        maxNotSafe = math.comb(self.g_len, 2)
        NotSafe = 0

        for i in range(self.g_len):
            for j in range(i + 1, self.g_len):

                if chrom[i] == chrom[j]:
                    NotSafe = NotSafe + 1
                elif chrom[i] - i == chrom[j] - j:
                    NotSafe = NotSafe + 1
                elif chrom[i] + i == chrom[j] + j:
                    NotSafe = NotSafe + 1

        return  maxNotSafe - NotSafe



    def select(self, m, population):
        fitness_values = [self.fitness_fn(chrom) for chrom in population]
        selected_indices = random.choices(range(len(population)), weights=fitness_values, k=m)
        selected_population = [population[i] for i in selected_indices]
        return selected_population



    def fittest(self, population, f_thres=None):
        BestChrom = None
        BestFitness = -1

        for x in population:
            CurrFitness = self.fitness_fn(x)

            if CurrFitness > BestFitness:
                if f_thres is None or CurrFitness >= f_thres:
                    BestChrom = x
                    BestFitness = CurrFitness

        return BestChrom


p = NQueensProblem(10, (0, 1, 2, 3), 4, 0.2)
i, sol = genetic_algorithm(p, f_thres=6, ngen=1000)
print(i, sol)
print(p.fitness_fn(sol))

p = NQueensProblem(100, (0, 1, 2, 3, 4, 5, 6, 7), 8, 0.2)
i, sol = genetic_algorithm(p, f_thres=25, ngen=1000)
print(i, sol)
print(p.fitness_fn(sol))


p = NQueensProblem(100, (0, 1, 2, 3, 4, 5, 6, 7), 8, 0.2)
i, sol = genetic_algorithm(p, f_thres=28, ngen=1000)
print(i, sol)
print(p.fitness_fn(sol))






################################################################
# 3. Function Optimaization f(x,y) = x sin(4x) + 1.1 y sin(2y)
################################################################


class FunctionProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        super().__init__(n, g_bases, g_len, m_prob)

    def init_population(self):
        population = []
        maxX = self.g_bases[0]
        maxY =self.g_bases[1]
        for i in range(self.n):
            x = random.uniform(0,maxX)
            y = random.uniform(0, maxY)
            Chromo = (x, y)
            population.append(Chromo)
        return population


    def next_generation(self, population):

        fitnesses = list(map(self.fitness_fn, population))
        sorted_population = []

        for Pos1, chrom in enumerate(population):
            inserted = False
            for Pos2, other_chrom in enumerate(sorted_population):
                if fitnesses[Pos1] < fitnesses[Pos2]:
                    sorted_population.insert(Pos2, chrom)
                    inserted = True
                    break
            if not inserted:
                sorted_population.append(chrom)

        population = sorted_population
        Half = len(population) // 2
        Best = population[: Half]
        NextGen = Best.copy()

        while len(NextGen) < self.n:
            mom = random.choice(Best)
            dad = random.choice(Best)
            child = self.crossover(mom, dad)
            child = self.mutate(child)
            NextGen.append(child)

        return NextGen



        
    def mutate(self, chrom):

        P = random.random()
        if P <= self.m_prob:
            Choice = random.choice([0, 1])
            MutatedVal = random.uniform(0, self.g_bases[Choice])

            chrom = list(chrom)
            chrom[Choice] = MutatedVal
            chrom = tuple(chrom)
        return chrom



    def crossover(self, chrom1, chrom2):
        A = random.random()
        X = chrom1[0]+ A * (chrom2[0]- chrom1[0])
        Y = chrom1[1]+A * (chrom2[1] - chrom1[1])

        Choice = random.choice([0, 1])

        if Choice == 0:
            child = (X, chrom1[1])
        else:
            child = (chrom1[0], Y)

        return child



    def fitness_fn(self, chrom):
        x = chrom[0]
        y = chrom[1]
        fitness = x *math.sin(4*x) +1.1 * y * math.sin(2 * y)
        return fitness



    def select(self, m, population):
        if m == 0:
            return []

        population.sort(key=self.fitness_fn)

        Nchroms = len(population)
        Ranks = list(range(1, Nchroms + 1))
        Total = sum(Ranks)

        Probs = []
        for x in Ranks:
            probability = (Nchroms - x + 1) / Total
            Probs.append(probability)

        WeightedProbs = []
        SumProbs = 0
        for probability in Probs:
            SumProbs =SumProbs+ probability
            WeightedProbs.append(SumProbs)

        SelectedChroms = []
        for y in range(m):
            R = random.random()
            i = 0
            while R > WeightedProbs[i]:
                i += 1
            SelectedChroms.append(population[i])

        return SelectedChroms


    def fittest(self, population, f_thres=None):
        BestChrome = None
        F = float('inf')

        for x in population:
            fitness = self.fitness_fn(x)
            if fitness < F:
                if f_thres is None:
                    F = fitness
                    BestChrome = x
                elif fitness <= f_thres:
                    F = fitness
                    BestChrome = x

        return BestChrome






