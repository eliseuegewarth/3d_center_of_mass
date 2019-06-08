# 3d Center Of Mass
Calculate the [Center of mass](https://en.wikipedia.org/wiki/Center_of_mass) of all objects in 3d matrix.

## Problem
[Center of mass](https://en.wikipedia.org/wiki/Center_of_mass) (C.O.M.) is a very important information when you need to calculate the trajectory of a body receiving a force.
How can we calculate a C.O.M. of any 3D projection? How much computing is necessary?

### Solution strategy
The problem can be done by follow this steps:
- [ ] Model the pixels as nodes of the graph  
- [ ] Model the neighboring pixels with the same characteristic (Ex: density) as edges
- [ ] Use [Graph.BFS](https://en.wikipedia.org/wiki/Breadth-first_search) to find the components (objects) of the graph
- [ ] Use the strategy of, divide to conquer, to divide the three-dimensional object into lines (make recursively until a 1x1xN matrix remains)
- [ ] Calculate C.O.M. of any line found in the previous step
- [ ] Calculate C.O.M. of any C.O.M. found in the previous step (repeat until close all recursions)

## Requirements
This project only need `python3` to run.
If new libs came to be used, they will be stored in `requirements.txt` file. 

### Dev Requirements
Dev requirements are stored on dev-requirements.txt file.
Use `pip install -r dev-requirements.txt` if you are using pip or a equivalent command in your package manager.
