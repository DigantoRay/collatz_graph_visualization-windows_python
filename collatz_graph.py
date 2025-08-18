#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 21:06:14 2025.

@author: Gumbit
"""

import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg
import sys


def collatz(n) -> list:
    """
    Return a list of output numbers from the Collatz algorithm.

    Parameters
    ----------
    n : int
        The starting number for the algorithm.

    Returns
    -------
    collatz_list : list
        A list of numbers in the Collatz sequence.

    """
    collatz_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        collatz_list.append(n)
    return collatz_list


plt.rcParams["backend"] = 'tkagg'
while True:
    try:
        n = input('Enter an integer (or enter q to exit):\n> ')
        if n == 'q':
            sys.exit('Exiting program.')
        n = int(n)
        if n < 1:
            raise ValueError
        y_values = []
        x_values = []
        plt.xlabel('Iteration')
        plt.ylabel('Collatz Numbers')
        plt.title('Collatz Graph')
        plt.ion()
        plt.show()
        plt.rcParams["figure.raise_window"] = False
        for i, num in enumerate(collatz(n)):
            y_values.append(num)
            x_values.append(i)
            plt.plot(x_values, y_values)
            plt.pause(0.1)
        plt.ioff()
        plt.show()
    except ValueError:
        print('Please enter an integer greater than 1.')
