import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    s = 1/(1 + np.exp((-x)))
    ds = 1/(1 + np.exp(x)) * (1 - 1/(1 + np.exp(x)))
    return s, ds


def sigmoid_derivative(x):
    return 1/(1 + np.exp(x)) * (1 - 1/(1 + np.exp(x)))


def visualize():
    x = np.arange(-6, 6, 0.01)
    sigmoid(x)

    # Setup centered axes
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Create and show plot
    ax.plot(x, sigmoid(x)[0], color="#307EC7", linewidth=3, label="sigmoid")
    ax.plot(x, sigmoid(x)[1], color="#9621E2", linewidth=3, label="derivative")
    ax.legend(loc="upper right", frameon=False)
    fig.suptitle('Sigmoid (σ)')
    fig.show()
