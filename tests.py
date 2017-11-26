# ## Tests fonctionnels
# 
# Spécification minimale pour les classes Rule,
# 
# - self.unrank(n, k) == self.list(n)[k]
# - self.count(n) == len(self.list(n))
# - self.unrank(n, k) must fail for all k >= n
# 

from binarytree import BinaryTree, Leaf
from rules import UnionRule, ProductRule, EpsilonRule, SingletonRule, init_grammar
from examplegrammars import grammarDict
from random import randint

def runTest(gram,max_size=15):

    def testRank(size, n_samples=10):
        """
        Run tests on the rank methods using n_samples random samples from a random size set.
        """

        setsize = gram.count(size)

        if setsize==0:
            return

        n_samples = min(n_samples, setsize)

        samples = [randint(0,setsize-1) for _ in range(n_samples)]

        assert(all((gram.rank(gram.unrank(size,x)) == x for x in samples)))

    def testUnrank(size, n_samples=5):
        """
        Run tests on the unrank methods using n_samples random samples from a random size set.
        """
        
        
        # gram.unrank(n, gram.count(m)) must fail for all m >= n
        setsize = gram.count(size)
        
        if setsize==0:
            #This rule yields no elements for n={}, skipping test
            return
        
        try:
            gram.unrank(size, setsize)
            assert(False)
        except ValueError:
            assert(True)
            
        # gram.unrank(n, k) == gram.list(n)[k]
        
        n_samples = min(n_samples,size)
        
        samples = [randint(0,setsize-1) for _ in range(n_samples)] #tire des élements de la grammaire
                                                                   #de manière aléatoire
        gramlist = gram.list(size)
        
        for sample in samples:
            assert(gram.unrank(size, sample) == gramlist[sample])
            
    def testCountList(size):
        """
        Same as above but run test on count and list
        """
        
        assert(gram.count(size) == len(gram.list(size)))
        

    
    for n in range(max_size):
        testUnrank(n)
    print("testUnrank: passed")
    for n in range(max_size):
        testCountList(n)
    print("testCountList: passed")
    if gram.rankImplemented():
        for n in range(max_size):
                testRank(n)
        print("testRank: passed")

    else:
        print("Rank is not implemented for this grammar. Skip test.")

print("Starting tests...")

for gramName, gram in grammarDict.items():

    print("Testing {}".format(gramName))


    gramDef, gramStartingRule = gram
    runTest(gramDef[gramStartingRule])

