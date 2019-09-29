import unittest
import random
import math
import statistics
import data_viz
import random
import plot_gtex
import numpy as np
import os


class TestPlotGtex(unittest.TestCase):
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

    def test_linear_search(self):
        L = [1, 2, 3, 4, 5, 6]

        r = plot_gtex.linear_search(3, L)
        self.assertEqual(r, 2)

        r = plot_gtex.linear_search(10, L)
        self.assertEqual(r, -1)

    def test_binary_search(self):
        L = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5]]

        r = plot_gtex.binary_search(3, L)
        self.assertEqual(r, 2)

        r = plot_gtex.binary_search(10, L)
        self.assertEqual(r, -1)

    def test_linear_search_hit(self):
        L = ['a', 'b', 'a', 'b', 'c', 'a']

        r = plot_gtex.linear_search_all_hits('a', L)
        self.assertEqual(r, [0, 2, 5])

        r = plot_gtex.linear_search_all_hits('b', L)
        self.assertEqual(r, [1, 3])

        r = plot_gtex.linear_search_all_hits('d', L)
        self.assertEqual(r, [])


if __name__ == '__main__':
    unittest.main()
