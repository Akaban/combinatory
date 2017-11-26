from binarytree import BinaryTree, Leaf
from rules import UnionRule, ProductRule, EpsilonRule, SingletonRule, init_grammar

stringsum = lambda a,b : a + b
sizestr = lambda s : len(s)

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
fiboGram = {    "Fib"    : UnionRule("Vide", "Cas1", lambda w : 0 if w=="" else 1, sizestr),
                "Cas1"   : UnionRule("CasAu", "Cas2", lambda w : 0 if w[0] == 'A' else 1, sizestr),
                "Cas2"   : UnionRule("AtomB", "CasBAu", lambda w : 0 if w == "B" else 1, sizestr),
                "Vide"   : EpsilonRule(""),
                "CasAu"  : ProductRule("AtomA", "Fib", stringsum, lambda w : ("A", w[1:]), sizestr),
                "AtomA"  : SingletonRule("A"),
                "AtomB"  : SingletonRule("B"),
                "CasBAu" : ProductRule("AtomB", "CasAu", stringsum, lambda w : ("B", w[1:]), sizestr)}
init_grammar(fiboGram)

#Grammaire des arbres binaires
unconsTree = lambda t : (t.left(), t.right())
sizeTree = lambda t : 1 if t.is_leaf() else sizeTree(t.left()) + sizeTree(t.right())
treeGram = {
    "Tree": UnionRule("Node", "Leaf", lambda t : 1 if t.is_leaf() else 0, sizeTree ),
    "Node": ProductRule("Tree", "Tree", lambda a, b: BinaryTree([a, b]), unconsTree, sizeTree),
    "Leaf": SingletonRule(Leaf)
}
init_grammar(treeGram)

#Grammaire des mots de dyck
def dyckUncons(w):
    assert(w[0] == '(')
    count=0
    ind=0

    for c in w:
        if c=='(':
            count+=1
        else:
            count-=1
        ind+=1
        if count==0:
            u,v = w[0:ind],w[ind:]
            #print(f"Returning u={u} v={v}")
            return u, v

    raise ValueError("Not a dyck word.")

dyckGram = {
"Axiom": UnionRule("dyck","enddyck",lambda w: 1 if w=="" else 0, sizestr),
"dyck": ProductRule("dyck2","Axiom",stringsum, dyckUncons, sizestr),
"dyck2" : ProductRule("parleft","intermdyck",stringsum, lambda w: ("(", w[1:]), sizestr),
"enddyck" : EpsilonRule(""),
"parleft" : SingletonRule("("),
"parright" : SingletonRule(")"),
"intermdyck": ProductRule("Axiom","parright",stringsum, lambda w: (w[0:-1], w[-1]), sizestr)}
init_grammar(dyckGram)

allABwordsGram = {
    "Axiom": UnionRule("Axiom2","vide",lambda w: 1 if w=="" else 0, sizestr),
    "Axiom2": ProductRule("Axiom","letter",stringsum,lambda w: (w[0:-1],w[-1]), sizestr),
    "vide": EpsilonRule(""),
    "letter": UnionRule("a","b",lambda w : 1 if w=="b" else 0,sizestr),
    "a": SingletonRule("a"),
    "b": SingletonRule("b")
}
init_grammar(allABwordsGram)


grammarDict = {
        "allABwordsGram" : (allABwordsGram, "Axiom"),
        "dyckGram" : (dyckGram, "Axiom"),
        "fiboGram" : (fiboGram, "Fib"),
        "treeGram" : (treeGram, "Tree") }

