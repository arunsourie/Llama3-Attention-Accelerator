import numpy as np

# ----------------------------------------------------
# Step 1: Create Query (Q), Key (K), and Value (V)
# ----------------------------------------------------
# Each row represents one token (word)
# Each column represents one feature

Q = np.array([
    [1, 0],
    [0, 1]
])

K = np.array([
    [1, 0],
    [0, 1]
])

V = np.array([
    [5, 10],
    [20, 30]
])

print("=" * 50)
print("Query Matrix (Q)")
print(Q)

print("\nKey Matrix (K)")
print(K)

print("\nValue Matrix (V)")
print(V)

# ----------------------------------------------------
# Step 2: Compute Similarity Scores
# Scores = Q × Kᵀ
# ----------------------------------------------------

scores = np.matmul(Q, K.T)

print("\n" + "=" * 50)
print("Similarity Scores (Q × Kᵀ)")
print(scores)

# ----------------------------------------------------
# Step 3: Scale the Scores
# Divide by √dk
# dk = Dimension of each Key vector
# ----------------------------------------------------

dk = K.shape[1]

scaled_scores = scores / np.sqrt(dk)

print("\n" + "=" * 50)
print("Scaled Scores")
print(scaled_scores)

# ----------------------------------------------------
# Step 4: Apply Softmax
# Softmax converts scores into probabilities
# ----------------------------------------------------

exp_scores = np.exp(scaled_scores)

attention_weights = exp_scores / np.sum(
    exp_scores,
    axis=1,
    keepdims=True
)

print("\n" + "=" * 50)
print("Attention Weights")
print(attention_weights)

# ----------------------------------------------------
# Step 5: Compute Final Attention Output
# Output = Attention Weights × Value Matrix
# ----------------------------------------------------

attention_output = np.matmul(attention_weights, V)

print("\n" + "=" * 50)
print("Final Attention Output")
print(attention_output)

print("\n" + "=" * 50)
print("Completed Scaled Dot-Product Attention")
