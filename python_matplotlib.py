Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> year=[1950, 1970, 1990, 2010]
>>> pop=[2.519, 3.692, 5.263, 6.972]
>>> plt.plot(year,pop)
[<matplotlib.lines.Line2D object at 0x000001547E9FC160>]
>>> plt.plot(year, pop)
[<matplotlib.lines.Line2D object at 0x0000015473F9DA58>]
>>> plt.show()
