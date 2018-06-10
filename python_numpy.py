Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> baseball= [180, 215, 210, 188, 176, 209, 200]
>>> import numpy as np
np
>>> np_baseball=np.array([180, 215, 210, 188, 176, 209, 200])
>>> print(type(np_baseball))
<class 'numpy.ndarray'>
>>> import numpy as np
>>> np_height = np.array(height)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    np_height = np.array(height)
NameError: name 'height' is not defined
>>> height=[1.45, 1.47, 1.58]
>>> import numpy as np
>>> np_height=np.array(height)
>>> print(np_height)
[1.45 1.47 1.58]
>>> np_height_m = np_height * 0.0254
>>> print(np_height_m)
[0.03683  0.037338 0.040132]
>>> weight=[24, 50, 47]
>>> import numpy as np
>>> np_height_m=np.array(height) * 0.0254
>>> np_weight_kg = np.array(weight) * 0.453592
>>> bmi=np_weight_kg / np_height_m**2
>>> print(bmi)
[ 8025.52016519 16267.96719279 13236.75824727]
>>> light = bmi < 21
>>> print(light)
[False False False]
>>> print(bmi[light])
[]
>>> print(np_weight[50])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(np_weight[50])
NameError: name 'np_weight' is not defined
>>> np_weight = np.array(weight)
np_height = np.array(height)
SyntaxError: multiple statements found while compiling a single statement
>>> np_weight = np.array(weight)
>>> np_height=np.array(height)
>>> print(np_weight[50])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(np_weight[50])
IndexError: index 50 is out of bounds for axis 0 with size 3
>>> print(np_weight[5])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(np_weight[5])
IndexError: index 5 is out of bounds for axis 0 with size 3
>>> IndexError: index 5 is out of bounds for axis 0 with size 3
SyntaxError: invalid syntax
>>> print(np_weight[2])
47
>>> 
