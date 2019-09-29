import unittest
import random
import math
import statistics
import data_viz
import random
import numpy as np
import os


class TestMathLib(unittest.TestCase):
    def test_boxplot(self):
        random_dists = ['Normal', ' Lognormal', 'Exp', 'Gumbel',
                        'Triangular']
        N = 500

        norm = np.random.normal(1, 1, N)
        logn = np.random.lognormal(1, 1, N)
        expo = np.random.exponential(1, N)
        gumb = np.random.gumbel(6, 4, N)
        tria = np.random.triangular(2, 9, 11, N)

        # Generate 2d array
        data = [norm, logn, expo, gumb, tria]
        data_viz.boxplot(data, random_dists, 'Distribution',
                         'Value', 'Comparison', 'test_box_plot.png')
        # check the result is generated successfully or not
        self.assertTrue(os.path.exists('test_box_plot.png'))
        os.remove('test_box_plot.png')


if __name__ == '__main__':
    unittest.main()
