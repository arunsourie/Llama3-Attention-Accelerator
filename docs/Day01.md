### Day 01 - Attention Mathematics Fundamentals
**Data:** 02 July 2026

## Objective

Understand the Scaled Dot Product Attention and prepare a software reference implementation.

---

## Topics Covered
- What is an LLM
- Why Attention is important
- Vectors
- Dot Product
- Query (Q)
- Key (K)
- Value (V)
- Scaled Dot product Attention
- Softmax
- Quantization (Introduction)

---
## Concepts Learned
### Why Attention?
Attention allows a transformer model to determine which input tokens are most relevant when processing the current token.

## Vector
A vector is an ordered list of numerical values used to represent information.
ex: A=[1,3,6] or 1i +3j +6k

## Dot Product 
The dot product measures similarity between two vectors. A larger dot product usually means the vectors are more closely aligned
ex : A=[1,2,5] B=[3,2,4]
      result=1x3 + 2x2 + 5x4
 Result = 27
 
## Query, Key, Value
- Query represents what the current token is looking for.
- Key represents the information available from each token.
- Value  represents the information that will be passed to the output.

## Attention Formula 

Attention(Q,K,V) = Softmax((Q × Kᵀ)/√dk) x V
---

## Next Steps

- Implement Scaled Dot-Product Attention in Python.
- Verify results using sample vectors.
- Compare outputs with manual calculations.

