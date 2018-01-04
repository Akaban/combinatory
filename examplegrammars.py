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



No3ConsecutiveGram = {
"Vide" : EpsilonRule("") ,
"A" : SingletonRule("A"),
"B" : SingletonRule("B"),
"S" : UnionRule("Vide","2letterleft"),
"2letterleft" : UnionRule("a_2aleft","b_2bleft"),

"a_2aleft" : ProductRule("A", "1aleft",stringsum),
"b_2bleft" : ProductRule("B", "1bleft",stringsum),

"a_1aleft" : ProductRule("A", "b_2bleft",stringsum),
"b_1aleft" : ProductRule("B","1bleft",stringsum),
"1aleft" : UnionRule("a_1aleft","eps_1aleft"),
"eps_1aleft" : UnionRule("b_1aleft","Vide"),

"a_1bleft" : ProductRule("A", "1aleft",stringsum),
"b_1bleft" : ProductRule("B","a_2aleft",stringsum),
"1bleft" : UnionRule("a_1bleft","eps_1bleft"),
"eps_1bleft" : UnionRule("b_1bleft","Vide")
}
init_grammar(No3ConsecutiveGram)


palinABGram = {
 "A" : SingletonRule("A"),
 "B" : SingletonRule("B"),
 "Vide" : EpsilonRule(''),
 "Axiom" : UnionRule("PalinA", "Palin_e_b"),
 "Palin_e_b" : UnionRule("PalinB","Vide"),
 "PalinA" : ProductRule("A","PalinA_suite",stringsum),
 "PalinA_suite" : ProductRule("Axiom","A",stringsum),
 "PalinB" : ProductRule("B","PalinB_suite",stringsum),
 "PalinB_suite" : ProductRule("Axiom","B",stringsum)
}
init_grammar(palinABGram)


palinABCGram = {
 "A" : SingletonRule("A"),
 "B" : SingletonRule("B"),
 "C" : SingletonRule("C"),
 "Vide" : EpsilonRule(''),
 "Axiom" : UnionRule("PalinA", "Palin_e_b"),
 "Palin_e_b" : UnionRule("PalinB_C","Vide"),
 "PalinB_C" : UnionRule("PalinB", "PalinC"),
 "PalinA" : ProductRule("A","PalinA_suite",stringsum),
 "PalinA_suite" : ProductRule("Axiom","A",stringsum),
 "PalinB" : ProductRule("B","PalinB_suite",stringsum),
 "PalinB_suite" : ProductRule("Axiom","B",stringsum),
 "PalinC" : ProductRule("C","PalinC_suite",stringsum),
 "PalinC_suite" : ProductRule("Axiom","C",stringsum)
}
init_grammar(palinABCGram)

autantABGram = {
"lettre_A" : SingletonRule("A"),
"lettre_B" : SingletonRule("B"),
"Axiom" : UnionRule("aB", "bA"),

"aB" : ProductRule("lettre_A", "B", stringsum),
"bA" : ProductRule("lettre_B","A", stringsum),
"A" : UnionRule("lettre_A", "A_suite"),
"A_suite" : UnionRule("aS", "bAA"),
"aS" : ProductRule("lettre_A","Axiom",stringsum),
"bAA" : ProductRule("lettre_B", "AA", stringsum),
"AA" : ProductRule("A","A",stringsum),

"bA" : ProductRule("lettre_B", "A", stringsum),
"aB" : ProductRule("lettre_A","B", stringsum),
"B" : UnionRule("lettre_B", "B_suite"),
"B_suite" : UnionRule("bS", "aBB"),
"bS" : ProductRule("lettre_B","Axiom",stringsum),
"aBB" : ProductRule("lettre_A", "BB", stringsum),
"BB" : ProductRule("B","B",stringsum)
}
init_grammar(autantABGram)

grammarDict = {
        "allABwordsGram" : (allABwordsGram, "Axiom"),
        "dyckGram" : (dyckGram, "Axiom"),
        "fiboGram" : (fiboGram, "Fib"),
        "treeGram" : (treeGram, "Tree"),
        "No3ConsecutiveGram" : (No3ConsecutiveGram, "S"),
        "palinABGram" : (palinABGram, "Axiom"),
        "palinABCGram" : (palinABCGram, "Axiom"),
        "autantABGram" : (autantABGram, "Axiom") }

