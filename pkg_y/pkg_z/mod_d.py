import matplotlib.pyplot as plt

# :: [NUMBER], STRING|VOID, STRING|VOID, STRING|VOID -> VOID
# Creates a scatter plot from a list of 2D vectors:
def scatterPlot2D(vectors, title="2D Scatter Plot", xlabel="X Coordinates", ylabel="Y Coordinates"):
    
    # Separate the x and y coordinates into separate lists
    x_coords, y_coords = zip(*vectors)

    # Create a scatter plot
    plt.scatter(x_coords, y_coords, label=title)

    # Add labels and a legend
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    # Show the plot
    plt.show()


# :: [NUMBER], STRING|VOID, STRING|VOID, STRING|VOID -> VOID
# Creates a line graph from a list of 2D vectors:
def lineGraph2D(vectors, title="2D Line Graph", xlabel="X Coordinates", ylabel="Y Coordinates"):
    
    # Separate the x and y coordinates into separate lists
    x_coords, y_coords = zip(*vectors)

    # Create a line plot
    plt.plot(x_coords, y_coords)

    # Add labels and a title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Show the plot
    plt.grid()
    plt.show()

#  Plot a list of sets of points on the same scatter or line plot:
def graphVectors(point_sets, labels=None, colors=None, markers=None, title="Plot", xlabel="X Coordinates", ylabel="Y Coordinates", use_line=False):
   
    if labels is None:
        labels = [f"Set {i+1}" for i in range(len(point_sets))]
    if colors is None:
        colors = ['blue', 'red', 'green', 'orange', 'purple', 'cyan', 'magenta']
    if markers is None:
        markers = ['o', 'x', 's', '^', 'D', 'v', 'p']

    plt.figure(figsize=(8, 6))

    for i, points in enumerate(point_sets):
        x_coords, y_coords = zip(*points)
        if use_line:
            plt.plot(x_coords, y_coords, label=labels[i], color=colors[i], marker=markers[i])
        else:
            plt.scatter(x_coords, y_coords, label=labels[i], color=colors[i], marker=markers[i])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.grid()
    plt.show()