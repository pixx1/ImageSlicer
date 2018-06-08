# ImageSlicer
A small tool for slicing images into smaller pieces.

Example
---
<img src="example.jpg" width="315" title="original image">  

 
#### Function "bysize"

[main.py](main.py)  
```python
import ImageSlicer
ImageSlicer.bysize("example.jpg", 2000, 2000, output_folder="sliced_by_size", keep_end_sections=True)
```````

Function for slicing images by size
1. Input file  
2. width of the new images  
3. height of the new images  
4. output path (optional)  
5. If you want to keep the end section, which are normally smaller (optional)  

<img src="sliced_by_size/0001_example.jpg" width="200" height="200"> <img src="sliced_by_size/0002_example.jpg" width="115" height="200">  
<img src="sliced_by_size/0003_example.jpg" width="200" height="37"> <img src="sliced_by_size/0004_example.jpg" width="115" height="37">  


#### Function "bynumber"

```python
import ImageSlicer
ImageSlicer.bynumber("example.jpg", 2, 2, output_folder="sliced_by_number", keep_end_sections=True)
```````

Function to slice images by number of parts you want to have
so if the input is 10,10 you will get 100 images 
(depending if you want wo keep the smaller parts or not).

1. Input file  
2. number of images horizontal
3. number of images vertical
4. output path (optional)  
5. If you want to keep the end section, which are normally smaller (optional)  

<img src="sliced_by_number/0001_example.jpg" width="157" height="118"> <img src="sliced_by_number/0002_example.jpg" width="157" height="118">  
<img src="sliced_by_number/0003_example.jpg" width="157" height="118"> <img src="sliced_by_number/0004_example.jpg" width="157" height="118">  

---
Python 3.5+  
Tested: Linux

---  
  
   
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />These images are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
