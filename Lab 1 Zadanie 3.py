from scipy import *
from scipy.fftpack import fftshift
from pylab import *
x,y= meshgrid(r_[-3:3:100j], r_[-3:3:100j]);
z = 3*(1-x)**2*exp(-x**2-(y+1)**2) -10*(x/5-x**3-y**5)*exp(-x**2-
y**2) -(1/3)*exp(-(x+1)**2-y**2);
wav = ("wavdata")
#x1 = r_[1:wav.size+1]
subplot(2,2,1);contour(x,y,z,25);grid(True);title("Simple 2D Contour Plot");
subplot(2,2,2);contourf(x,y,z);title("Filled Contour");
subplot(2,2,3);h=specgram(wav);title("Spectrogram");
subplot(2,2,4);hist(randn(100));title("Histogram");
show();
 
