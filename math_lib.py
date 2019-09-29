import math
import argparse
import sys


def list_mean(V):
    # verify the input is a list containing only numbers
    if (isinstance(V, list)):
        for i in V:
            if not (isinstance(i, int) or isinstance(i, float)):
                print('Please input a list containing numbers')
                return None
    # if it is an empty list, return None
    if (len(V) == 0):
        print('Empty list')
        return None
    # return mean
    return float(sum(V)) / float(len(V))


def list_stdev(V):
    # verify the input is a list containing only numbers
    if (isinstance(V, list)):
        for i in V:
            if not (isinstance(i, int) or isinstance(i, float)):
                print('Please input a list containing numbers')
                return None
    # if it is an empty list, return None
    if (len(V) < 2):
        print('List too short')
        return None
    # if mean is None, return None
    mean = list_mean(V)
    if mean is None:
        return None
    _sum = float(sum([(float(mean)-float(x))**2 for x in V]))
    return math.sqrt(_sum / float(len(V)-1))
