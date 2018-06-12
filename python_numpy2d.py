Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
>>> import numpy as np
>>> np_baseball=np.array(baseball)
>>> print(type(np_baseball))
<class 'numpy.ndarray'>
>>> print(np_baseball.shape)
(4, 2)
>>> print(np_baseball[49,:])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(np_baseball[49,:])
IndexError: index 49 is out of bounds for axis 0 with size 4
>>> print(np_baseball[3,:])
[188.   75.2]
>>> 
