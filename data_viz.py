import matplotlib
import matplotlib.pyplot as plt
import math_lib
matplotlib.use('Agg')


def boxplot(L, out_file_name):
    """plot boxplot for an input array and save the result as a png file
    """
    plt.boxplot(L)
    plt.ylabel('Distribution')
    plt.xlabel('Box')
    plt.title('mean: ' + str(math_lib.list_mean(L)) + ' ' +
              'stdev: ' + str(math_lib.list_stdev(L)))
    plt.savefig(out_file_name)
    pass


def histogram(L, out_file_name):
    """plot boxplot for an input array and save the result as a png file
    """
    plt.hist(L, bins=30)
    plt.ylabel('Frequency')
    plt.xlabel('Value')
    plt.title('mean: ' + str(math_lib.list_mean(L)) + ' ' +
              'stdev: ' + str(math_lib.list_stdev(L)))
    plt.savefig(out_file_name)
    pass


def combo(L, out_file_name):
    """plot boxplot for an input array and save the result as a png file
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))
    axs[0].hist(L, bins=30)
    axs[1].boxplot(L)
    fig.suptitle('mean: ' + str(math_lib.list_mean(L)) + ' ' +
                 'stdev: ' + str(math_lib.list_stdev(L)))
    fig.savefig(out_file_name)
    pass
