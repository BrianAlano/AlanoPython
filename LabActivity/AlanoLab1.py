# Define the sets based on the Venn diagram
A = {'a', 'b', 'c', 'd', 'e'}
B = {'c', 'd', 'e', 'f', 'g', 'h'}
C = {'e', 'f', 'g', 'h', 'i', 'j', 'k'}

# a. How many elements are there in set A and B
elements_in_A_and_B = len(A.union(B))
print(f"Number of elements in set A and B: {elements_in_A_and_B}")

# b. How many elements are there in B that is not part of A and C
elements_in_B_not_in_A_and_C = len(B - (A.union(C)))
print(f"Number of elements in B that are not part of A and C: {elements_in_B_not_in_A_and_C}")

# c. Show the following using set operations

# i. [h, i, j, k]
set_i = C - (A.union(B))
print(f"Set i: {set_i}")

# ii. [c, d, f]
set_ii = (A.intersection(B)) - C
print(f"Set ii: {set_ii}")

# iii. [b, c, h]
set_iii = (A - C).union(B - C)
print(f"Set iii: {set_iii}")

# iv. [d, f]
set_iv = (A.intersection(B)).intersection(C)
print(f"Set iv: {set_iv}")

# v. [c]
set_v = A.intersection(B) - C
print(f"Set v: {set_v}")

# vi. [l, m, o]
# Assuming these elements are in a universal set U
U = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'}
set_vi = U - (A.union(B).union(C))
print(f"Set vi: {set_vi}")