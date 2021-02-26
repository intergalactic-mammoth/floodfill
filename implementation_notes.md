My implementation is a modification of the graph traversal algorithms we were taught in the lecture. 



Implementation notes:

- Because we need only elements of the same color as the "clicked" pixel (root node) to change, I store the original color of the root to be used when comparing.
- Because Python's `pop()` function of the `set` data structure returns an arbitrary element, the implementation is neither breadth nor depth first, but rather a mix between the two. 
- There is no need for marking nodes as we have done in the lecture, since I use the set data structure, that only allows unique elements in the set. 
- The "visit" action corresponds to the recoloring of the active pixel. 
- Because .jpeg images are compressed data they are noisy, therefore I added a small tolerance amount when comparing colors, to overcome the noise problem.
- The time to solution increases linearly to the number of pixels in the image, as indicated in the assignment.  