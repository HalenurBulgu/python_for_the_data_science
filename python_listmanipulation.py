Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
>>> areas[9]=10.50
>>> areas[4]= "chill zone"
>>> print(areas)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5]
>>> areas_1=areas + ["poolhouse", 24.5]
>>> print(areas_1)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5]
>>> areas_2= areas_1 + ["garage", 15.45]
>>> print(areas_2)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5, 'garage', 15.45]
>>> del(areas[-4:-2])
>>> print(areas)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bathroom', 10.5]
>>> # Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
>>> areas_copy = areas[:]
>>> areas_copy[0] = 5.0
>>> #print areas
>>> print(areas)
[11.25, 18.0, 20.0, 10.75, 9.5]
>>> print(areas[:])
[11.25, 18.0, 20.0, 10.75, 9.5]
>>> print(areas_copy)
[5.0, 18.0, 20.0, 10.75, 9.5]
>>> print(areas[:])
[11.25, 18.0, 20.0, 10.75, 9.5]
>>> 
