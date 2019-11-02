# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:19:28 2019

@author: ZUISA
"""

import scipy
from pylab import *
x=r_[0:101]
y01=sin(2*pi*x/100)
y02=cos(2*pi*x/100)
plot(x,y01,linewidth=5.0)
#hold(True)
plot(x,y02,linewidth=5.0)
xlabel('x');
ylabel('y');
title('Plottingsin(x) & cos(x)');
legend(('sin(x','cos(x)'));
grid(True)
show()
