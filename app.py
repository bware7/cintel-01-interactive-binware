import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from shiny.express import ui, input, render
from palmerpenguins import load_penguins

ui.page_opts(title="Bin's Enhanced Interactive Data App", fillable=True)

# Sidebar with inputs for histogram and scatter plot
with ui.sidebar():
    ui.input_slider(
        id="selected_number_of_bins",
        label="Select Number of Bins",
        min=1,
        max=100,
        value=20
    )
    ui.input_select(
        id="selected_species",
        label="Choose Penguin Species",
        choices=["Adelie", "Gentoo", "Chinstrap"],
        selected="Adelie"
    )

# Define the reactive histogram plot output
@render.plot(alt="A dynamic histogram showing random data distribution")
def histogram():
    # Generate random data for histogram
    np.random.seed(19680801)
    data_array = 100 + 15 * np.random.randn(437)
    
    # Plot histogram with selected bin count
    plt.hist(data_array, bins=input.selected_number_of_bins(), density=True)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.title("Distribution of Random Data")

# Define the reactive scatter plot for Palmer Penguins
@render.plot(alt="Scatter plot of penguin data")
def penguin_plot():
    penguins = load_penguins()
    selected_penguins = penguins[penguins["species"] == input.selected_species()]
    sns.scatterplot(
        x=selected_penguins["flipper_length_mm"],
        y=selected_penguins["body_mass_g"],
        hue=selected_penguins["species"],
        palette=["#FF8C00", "#159090", "#A034F0"]
    )
    plt.xlabel("Flipper Length (mm)")
    plt.ylabel("Body Mass (g)")
    plt.title(f"{input.selected_species()} Penguins: Flipper Length vs. Body Mass")
