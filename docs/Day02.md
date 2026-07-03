# Day 02 - Scaled Dot-Product Attention Implementation

**Date:** 03 July 2026

---

# Objective

Understand the complete Scaled Dot-Product Attention algorithm and implement a Python reference model that will later be used to validate the FPGA hardware accelerator.

---

# Topics Studied

- Matrix Multiplication
- Matrix Transpose
- Query (Q)
- Key (K)
- Value (V)
- Similarity Score Computation
- Scaling by √dk
- Softmax
- Attention Output
- Data Flow in Transformer Attention

---

# Concepts Learned

## Why Attention?

Attention enables a Transformer model to identify which input tokens are most relevant while processing the current token.

---

## Query (Q)

Represents what the current token is searching for.

---

## Key (K)

Represents the information available from every token.

---

## Value (V)

Contains the information that contributes to the final output after attention weights are calculated.

---

## Dot Product

The dot product measures similarity between Query and Key vectors.

Example:

Q = [2,3]

K = [4,5]

Result

2×4 + 3×5 = 23

Higher values indicate stronger similarity.

---

## Why Transpose K?

Transposing the Key matrix allows every Query vector to be compared against every Key vector during matrix multiplication.

This produces the similarity matrix.

---

## Scaling

Similarity scores are divided by √dk to prevent extremely large values before applying Softmax.

This improves numerical stability.

---

## Softmax

Softmax converts similarity scores into probabilities.

The output probabilities always sum to 1.

These probabilities represent attention weights.

---

## Final Attention Output

The attention weights are multiplied with the Value matrix to generate the final output vector.

---

# Data Flow

Words

↓

Embeddings

↓

Q, K, V

↓

Q × Kᵀ

↓

Scaling

↓

Softmax

↓

Attention Weights

↓

Multiply with V

↓

Final Attention Output

---

# Work Completed

- Studied the complete Scaled Dot-Product Attention algorithm.
- Understood the purpose of Q, K, and V.
- Learned matrix transpose and similarity computation.
- Learned why scaling is required.
- Studied Softmax and attention weights.
- Implemented the reference algorithm in Python.
- Printed intermediate computation results for verification.

---

# Challenges Faced

- Understanding why the Key matrix must be transposed.
- Understanding how Softmax converts similarity scores into probabilities.

---

# Outcome

Successfully understood and implemented the complete Scaled Dot-Product Attention pipeline.

This implementation will serve as the software reference model for validating the FPGA hardware accelerator in later phases.

---

# Next Steps

- Verify the Python implementation with multiple test cases.
- Begin studying the Zynq UltraScale+ architecture.
- Install and configure Vivado 2025.2.
