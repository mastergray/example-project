from pkg_x import ModA, ModB 
from pkg_y import MathFN, GraphFN

# Test mod_a from package:
instance = ModA.ClassA("whatever")
instance.sayHello()

# Test mod_b from package:
sumAllPrint = ModB.composeAll([
    lambda arr : ModB.fold(lambda acc, elem : acc + elem, arr, 0),
    ModB.logger()
])([1,2,3,4])

# Test pkg_y functions:
compareVectors = MathFN.CompareVectors([1,2,3], [4,5,6])
print(f"Dot Product: {compareVectors.dotProduct()}")
print(f"Euclidean Distance: {compareVectors.euclideanDistance()}")
print(f"Cosine Similarity: {compareVectors.cosineSimilarity()}")
print(f"Manhattan Distance: {compareVectors.manhattanDistance()}")
print(f"RBF Kernel: {compareVectors.RBFKernel()}")
print(f"Polynomial Kernel: {compareVectors.polyKernel()}")
print(f"Pearson Correlation:{compareVectors.pearsonCorrelation()}")
print(f"Spearman Rank Correlation:{compareVectors.spearmanRankCorrelation()}")

# Test a graph function:
GraphFN.lineGraph2D([
    [1,2], [3,4], [5,6], [7,8], [9,10]
])