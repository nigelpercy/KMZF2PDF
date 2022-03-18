# KMZF2PDF

This is a first attempt at a python script which will enable the creation of the program listing in PDF format from a Sharp MZ-80K MZF file.
The mzf file needs to be a basic program and use SP-5025 Basic. I may look at further enhancing it to include other versions.

Dependencies

Pillow 9.0.1
pip install Pillow

fpdf2 2.5.1
pip install fpdf2

Overview

I have used the image from MZ-80K CG-ROM (Character Generator) to create 8x8 bitmaps of the characters these are then used
by a routine which reads the MZF file and then outputs each character as a image onto a PDF page.
