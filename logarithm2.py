import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider

# Function to display log base b of x
def plot_log(base):
    x = np.linspace(1, 32, 200)
    y = np.log(x) / np.log(base)  # Change of base formula

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"log base {base} of x", color='blue')
    plt.scatter([base**i for i in range(1, 6)], [i for i in range(1, 6)], color='red', label='Key Points')
    for i in range(1, 6):
        plt.text(base**i, i + 0.2, f"log{base}({base**i}) = {i}", fontsize=9, ha='center')

    plt.title(f"Understanding log base {base}")
    plt.xlabel("x")
    plt.ylabel(f"log base {base} of x")
    plt.grid(True)
    plt.legend()
    plt.ylim(0, 6)
    plt.show()

# Interactive slider for the base
interact(plot_log, base=IntSlider(min=2, max=10, step=1, value=2));
