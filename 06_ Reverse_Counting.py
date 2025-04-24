'''
learn new about sys.setrecursionlimit(1100) and how to handel recursion depth 
'''
import sys
# Increase the recursion depth limit (use when known task size)
sys.setrecursionlimit(1100)

def reverse_count(n):
    if n < 1:
        return
    print(n)
    reverse_count(n - 1)

reverse_count(1000)
