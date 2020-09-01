import numpy as np
from scipy.stats import binom

def calc_list_probabilidades_testadas(qnt_pontos):
    lis_prob_uniform = np.arange(0, 1, 1/qnt_pontos)
    return lis_prob_uniform

def cal_prior_uni(qnt_pontos):
    prior = np.array([0.05 for x in range(qnt_pontos) ]) #np.random.uniform()
    return prior


# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html

# Probability mass function
def calc_prob_mass_funcion(k,n):
    def binomial(p):
        s = binom.pmf(k, n, p)
        return s 
    return binomial


def calc_likehood_bino(k,n, list_prob):
    likelihood = list(map(calc_prob_mass_funcion(k,n),list_prob))
    return likelihood


def calc_post_bayes(likelihood, prior):
    post = likelihood * prior
    # normalizando para a soma ser 1
    post = post/ sum(post)
    return post