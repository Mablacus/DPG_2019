# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:42:44 2019

@author: Martin
"""

import numpy as np
import matplotlib.pyplot as plt

def cooperativity(x):
    return 2*x/(2*x+1.0)

x = np.linspace(0.0,5,1000)

plt.xlabel('Cooperativity')
plt.ylabel('Probability')
plt.plot(x,cooperativity(x))
