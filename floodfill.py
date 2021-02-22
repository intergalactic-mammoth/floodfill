#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio
import numpy as np
import PIL


def get_neighbors(x, y, width, height):
    '''
    Returns the neighbors of the selected pixel (x,y).
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

    # Save the color of the root pixel
    root_col = np.array(image[u, v, :])   
    
    stack = {(u, v)}

    while len(stack) is not 0:
        V = stack.pop()
        neighbors = get_neighbors(V[0], V[1], width, height)

        image[V[0], V[1], :] = color        #"visit" pixel

        for neighbor in neighbors:
            n_col = image[neighbor[0], neighbor[1], :]

            #colors_equal = np.array_equal(n_col, root_col)
            colors_equal = np.allclose(n_col, root_col, atol=5)
            if colors_equal:
                stack.add(neighbor)

    return image
            
            
            
col = [20, 20, 20]
u = 0
v = 0
img = PIL.Image.open('10pix_U.jpg')
img = np.asarray(img).copy()
floodfill(img, u, v, col)
