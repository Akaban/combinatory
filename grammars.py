from binarytree import BinaryTree, Leaf
from rules import UnionRule, ProductRule, EpsilonRule, SingletonRule, init_grammar

stringsum = lambda a,b : a + b

#Grammaire de a^n . b^n pour n pair
grammarTest = {
    "Axiom" : UnionRule("Vide","Axiom1"),
    "Axiom1" : ProductRule("SingA","IntermSingB",stringsum),
    "Vide" : EpsilonRule(""),
    "SingA" : SingletonRule("A"),
    "SingB" : SingletonRule("B"),
    "IntermSingB" : ProductRule("Axiom","SingB",stringsum)
}
init_grammar(grammarTest)

#Grammaire des mots de fibonnaci
fiboGram = {    "Fib"    : UnionRule("Vide", "Cas1"),
                "Cas1"   : UnionRule("CasAu", "Cas2"),
                "Cas2"   : UnionRule("AtomB", "CasBAu"),
                "Vide"   : EpsilonRule(""),
                "CasAu"  : ProductRule("AtomA", "Fib", stringsum),
                "AtomA"  : SingletonRule("A"),
                "AtomB"  : SingletonRule("B"),
                "CasBAu" : ProductRule("AtomB", "CasAu", stringsum)}
init_grammar(fiboGram)

#Grammaire des arbres binaires
treeGram = {
    "Tree": UnionRule("Node", "Leaf"),
    "Node": ProductRule("Tree", "Tree", lambda a, b: BinaryTree([a, b])),
    "Leaf": SingletonRule(Leaf)
}
init_grammar(treeGram)

#Grammaire des mots de dyck
dyckGrammar = {
"Axiom": UnionRule("dyck","enddyck"),
"dyck": ProductRule("dyck2","Axiom",stringsum),
"dyck2" : ProductRule("parleft","intermdyck",stringsum),
"enddyck" : EpsilonRule(""),
"parleft" : SingletonRule("("),
"parright" : SingletonRule(")"),
"intermdyck": ProductRule("Axiom","parright",stringsum)}
init_grammar(dyckGrammar)

allABwords = {
    "Axiom": UnionRule("Axiom2","vide"),
    "Axiom2": ProductRule("Axiom","letter",stringsum),
    "vide": EpsilonRule(""),
    "letter": UnionRule("a","b"),
    "a": SingletonRule("a"),
    "b": SingletonRule("b")
}
init_grammar(allABwords)
