
#   in its original contents.
#


import math


class GeneticProblem:
    def __init__(self, n, g_bases, g_len, m_prob):
        """
        Initializes attributes of the class
        Arguments:
        - n       : number of chromosomes in the population
        - g_bases : gene bases
        - g_len   : length of a chromosome
        - m_prob  : mutation probability
        """
        self.n = n
        self.g_bases = g_bases
        self.g_len = g_len
        self.m_prob = m_prob
    

    def init_population(self):
        """
        Returns an initial population. Initial population is a list
        that contains n randomly generated chromosomes. Each chromosome
        is a tuple of g_len items selected from g_bases
        """
        pass

    
    def next_generation(self, population):
        """
        Returns the next generation of population containing n chromosomes
        obtained by applying crossover and mutation to the given population.
        """
        pass


    def mutate(self, chrom):
        """
        Returns a chromosome after mutating the given chrom at a 
        random position with the probability of m_prob
        """
        pass

    
    def crossover(self, chrom1, chrom2):
        """
        Returns an offspring obtained by applying crossover to the 
        two given chromosomes, chrom1 and chrom2. If the crossover
        occurs at a random index i, then the offspring is created 
        by combining chrom1[:i] with chrom2[i:]
        """
        pass


    def fitness_fn(self, chrom):
        """Returns the fitness value of the given chrom"""
        pass


    def select(self, m, population):
        """
        Returns a list of m chromosomes randomly selected from the
        given population using fitness proportionate selection.
        """
        pass


    def fittest(self, population, f_thres=None):
        """
        If f_thres is None, return the best chromosome in the given population.
        If f_thres is not None, return the best chromosome if its fitness value
        is better than f_thres. Otherwise, return None.
        """
        pass

