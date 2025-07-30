#  Range Search in an AVL Tree (Balanced BST)

This project implements a recursive function `range_search` that returns all values within a specified range `[low, high]` in an AVL Tree (or any Binary Search Tree).

---

##  Problem Statement

Implement a function that performs a **range search** on an AVL tree. Given a `low` and `high` value, return all node values between them (inclusive).

## Algorithm Explanation

At each node:
	•	Recurse left if there’s a chance to find values ≥ low
	•	Append current node value if it’s in the range [low, high]
	•	Recurse right if there’s a chance to find values ≤ high
