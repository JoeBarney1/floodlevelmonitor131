import matplotlib.pyplot as plt
#task 2E
def plot_water_levels(station, dates, levels):

    t =dates
    level = levels
    # Plot
    plt.plot(t, level)
    


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station {}".format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    if station.typical_range != None:
            plt.axhline(station.typical_range[0], color='r') # lower level
            plt.axhline(station.typical_range[1], color='r') # upper level
    plt.show()