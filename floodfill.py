#%%
import numpy as np
import PIL


def get_neighbors(x, y, width, height):
    '''
    Returns the neighbors of the selected pixel (x,y) as a set.
    width and height correspond to the dimensions of the image.

    If it is an edge or corner pixel, it only has 3 or 2 neighbors
    respectively instead of 4.
    '''

    neighbors = set({})
    if x>0:
        neighbors.add((x-1, y))
    if x<width-1:
        neighbors.add((x+1,y))
    if y>0:
        neighbors.add((x,y-1))
    if y<height-1:
        neighbors.add((x,y+1))

    return neighbors

def floodfill(image, u, v, color):
    '''
    This is basically a modification of the stack-based
    DF-Traversal algorithm we were taught in class. 

    Image is an numpy tensor WidthxHeightxChannels.
    (u,v) is the starting point for the floodfill operation.
    color is a triplet of [R, G, B] for the desired resulting color.
    '''

    #Get the dimensions of the image
    width, height, channels = (image.shape)
    
    # Check that the input parameters are reasonable: (u,v) is part of the
    # image and that the image and the chosen color have the same number 
    # of channels
    assert(u<=width), 'Selected point out of image in x-dir!'
    assert(v<=height), 'Selected point out of image in y-dir!'
    assert(len(color)==channels), 'Selected color has different number of channels than the image.'
    
    #Check that the RGB input is within 0 and 255
    assert(all(ch >= 0 and ch <=255 for ch in color)), "The RGB values of input color must be between 0 and 255!"

    # Save the color of the root node
    root_col = np.array(image[u, v, :])   
    
    # Start the stack with the coordinates of the root node
    stack = {(u, v)}

    # Iterate until the stack is empty
    while len(stack) is not 0:
        # Remove the last item from the stack and save it to V
        V = stack.pop()

        # Get the neighbors of V as a set.
        neighbors = get_neighbors(V[0], V[1], width, height)

        # Change the color of the image at the coordinates of V
        image[V[0], V[1], :] = color

        # Iterate through all the neighbors of V
        for neighbor in neighbors:
            # Get the color of each neighbor
            n_col = image[neighbor[0], neighbor[1], :]

            # If the color of the neighbor matches the color of the root
            # node, then it needs to be added to the stack.
            # To avoid the problem of minor noise present in .jpg images
            # we add a small tolerance value.
            colors_equal = np.allclose(n_col, root_col, atol=5)
            if colors_equal:
                stack.add(neighbor)

    return image
            
            
# Used for internal debugging           
col = [20, 20, 20]
u = 0
v = 0
img = PIL.Image.open('imgs/10x10_U.jpg')
img = np.asarray(img).copy()
floodfill(img, u, v, col)
