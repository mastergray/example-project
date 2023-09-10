import numpy as np
from scipy.stats import pearsonr, spearmanr

# Calculates similarity between two stored vectors:
class CompareVectors:

    # CONSTRUCTOR :: [NUMBER|NUMPY], [NUMBER|NUMPY] -> self
    # NOTE: Will try to cast given values as numpy arrays:
    # NOTE: Will throw an exception if vectors aren't the same size:
    def __init__(self, vector1, vector2):
        self.vector1 = vector1 if isinstance(vector1, np.ndarray) else np.array(vector1)
        self.vector2 = vector2 if isinstance(vector2, np.ndarray) else np.array(vector2)
        if len(self.vector1) != len(self.vector2):
            raise ValueError("Vectors must be the same size")

    # :: VOID -> NUMBER 
    # Returns the dot product between the stored vectors
    def dotProduct(self):
        return np.dot(self.vector1, self.vector2)
    
    # :: VOID -> NUMBER 
    # Calculates the Euclidean Distance between the stored vectors:
    def euclideanDistance(self):
        return np.linalg.norm(self.vector1 - self.vector2)
 
    # :: VOID -> NUMBER
    # Calculates the cosine similairty between the stored vectors:
    def cosineSimilarity(self):
        norm_vector1 = np.linalg.norm(self.vector1)
        norm_vector2 = np.linalg.norm(self.vector2)
        return  self.dotProduct() / (norm_vector1 * norm_vector2)

    # :: VOID -> NUMBER
    # Measures the distance between two points as the sum of the absolute differences of their coordinates:
    def manhattanDistance(self):
        return sum(abs(p1 - p2) for p1, p2 in zip(self.vector1, self.vector2))

    # Generalizes both Euclidean distance (L2 distance) and Manhattan distance (L1 distance):
    # NOTE: The Minkowski distance formula includes a parameter "p" that controls the order of the distance metric - When p=2 it becomes the Euclidean distance; when p=1, it becomes the Manhattan distance
    def minkowskiDistance(self, p=2):
        return np.power(np.sum(np.abs(np.array(self.vector1) - np.array(self.vector2))**p), 1/p)

    # :: NUMBER -> NUMBER 
    # Calculates similairty between the stored vectors using the Gaussian Radial Basis Function kernel:
    # NOTE: Larger values of sigma result in smoother kernels with broader support, while smaller values make the kernel more sensitive to small differences.
    def RBFKernel(self, sigma=1):
        distance = self.euclideanDistance();
        return np.exp(-distance**2 / (2 * sigma**2))
    
    # :: NUMBER, NUMBER|VOID -> NUMBER 
    # NOTE: Adjust the degree parameter to control the kernel's sensitivity to features in your specific application - higher degrees make the kernel more sensitive to high-order features in the data
    def polyKernel(self, degree=2, bias=1):
       return (self.dotProduct() + bias) ** degree
    
    # :: NUMBER|VOID -> correlation_coefficient
    # Measures the linear correlation between two datasets:
    # NOTE: A correlation_coefficient close to 1 indicates a strong positive linear correlation, close to -1 indicates a strong negative linear correlation, and close to 0 indicates no significant linear correlation
    # NOTE: Alpha is a predetermined probability threshold to determine the criteria for rejecting the null hypothesis 
    # NOTE: An alpha of 0.05 (5%) is the most commonly used - It indicates that you are willing to accept a 5% chance rejecting a true null hypothesis.  In other words, you want to be at least 95% confident in your decision to reject the null hypothesis before you actually reject it
    # NOTE: An alpha of 0.01 (1%) is typically used in situations where the consequences of a false positive are particularly severe or when strong evidence is required
    # NOTE: An alpha of 0.10 (10%) is a less stringent alpha level and used in exploratory data analysis or in situations where researchers want to be more inclusive in their initial analysi
    # NOTE: If p_value > alpha, throws an exception
    def pearsonCorrelation(self, alpha=0.5):
        correlation_coefficient, p_value = pearsonr(self.vector1, self.vector2)
        if p_value < alpha:
            return correlation_coefficient
        raise ValueError(f"Pearson correlation is not statistically significant: {p_value}") 

    # :: NUMER|VOID -> correlation_coefficient
    # Measures the strength and direction of the monotonic relationship between two datasets.
    # NOTE: The value can range from -1 to 1, where -1 indicates a perfect negative monotonic correlation, 1 indicates a perfect positive monotonic correlation, and 0 indicates no monotonic correlation
    # NOTE: Monotonic correlation refers to the relationship between two variables where their values tend to consistently increase or decrease together, but not necessarily at a constant rate
    # NOTE: In a positive monotonic correlation, as the values of one variable increase, the values of the other variable also increase
    # NOTE: In a negative monotonic correlation, as the values of one variable increase, the values of the other variable decrease.
    # NOTE:  It's important to note that monotonic correlation measures the strength and direction of this non-linear relationship, whereas linear correlation (e.g., Pearson correlation) specifically measures the linear relationship between variables.
    # NOTE: If p_value > alpha, throws an exception
    def spearmanRankCorrelation(self, alpha=0.05):
        correlation_coefficient, p_value = spearmanr(self.vector1, self.vector2)
        if p_value < alpha:
            return correlation_coefficient
        raise ValueError(f"Spearman rank correlation is not statistically significant: {p_value}") 