import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Set page options including a title with your name
ui.page_opts(title="Bin's Interactive Histogram App", fillable=True)

# Sidebar with an interactive slider to control the histogram's bin count
with ui.sidebar():
    ui.input_slider(
        id="selected_number_of_bins",      # Unique ID for the slider
        label="Select Number of Bins",     # Label for user-friendly interaction
        min=1,                             # Minimum value for bins
        max=100,                           # Maximum value for bins
        value=20                           # Default starting value for bins
    )

# Define the reactive plot output with a description
@render.plot(alt="A dynamic histogram showing random data distribution")
def histogram():
    # Generate random data for histogram
    np.random.seed(19680801)
    data_array = 100 + 15 * np.random.randn(437)
    
    # Create a histogram with the number of bins set by the slider
    plt.hist(data_array, bins=input.selected_number_of_bins(), density=True)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.title("Distribution of Random Data")
