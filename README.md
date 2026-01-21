## OX-String-Operation-Tree-Discovery

This Python project reconstructs the hierarchical sequence of operations performed on binary strings (composed of 'o' and 'x') to form an n-ary tree. Developed for the CENG 111 course at METU.

- Rebuilds a valid parent-child hierarchy from an unordered list where each child represents a single "o" to "x" transformation.

- Implements the tree using a nested list format: [datum, child1, child2, ...].

- Uses character-wise difference checks (onediff) and adjacency validation (child) to map string lineages.

- Employs a recursive helper function to transform discovered subtrees into a final unified data structure.

