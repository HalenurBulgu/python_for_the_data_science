Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> hall = 11.25
>>> kit = 18.0
>>> liv = 20.0
>>> bed = 10.75
>>> bath = 9.50
>>> areas = [11.25, 18.0, 20.0, 10.75, 9.50]
>>> print(areas)
[11.25, 18.0, 20.0, 10.75, 9.5]
>>> 
areas = [hall, kit, "living room", liv, bed, "bathroom", bath]
>>> print(areas)
[11.25, 18.0, 'living room', 20.0, 10.75, 'bathroom', 9.5]
>>> areas = ["hallway", hall, "livingroom", liv]
>>> print(areas)
['hallway', 11.25, 'livingroom', 20.0]
>>> house = [["hallway", hall],["kitchen", kit],["living room", liv],["bedroom", bed], ["bathroom", bath]
	 print(house)
	 
SyntaxError: invalid syntax
>>> print(house)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(house)
NameError: name 'house' is not defined
>>> house = [["hallway", hall],["kitchen", kit],["living room", liv],["bedroom", bed], ["bathroom", bath]]house = [["hallway", hall],["kitchen", kit],["living room", liv],["bedroom", bed], ["bathroom", bath]
													       
SyntaxError: invalid syntax
>>> house = [["hallway", hall],["kitchen", kit],["living room", liv],["bedroom", bed], ["bathroom", bath]]
>>> print(house)
[['hallway', 11.25], ['kitchen', 18.0], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5]]
>>> print(type(house))
<class 'list'>
>>> areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
>>> print(areas[1])
11.25
>>> print(areas[9])
9.5
>>> print(areas[5])
20.0
>>> 
