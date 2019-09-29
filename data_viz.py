import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def boxplot(par, meta, x_label, y_label, title, out_file):
    """plot boxplot for an input array and save the result as a png file
    """
    plt.boxplot(par)
    plt.ylabel('Distribution')
    plt.xlabel('Box')
    plt.savefig(out_file)
    pass
