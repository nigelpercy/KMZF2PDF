   
# KMZF2PDF - Python Script to convert Sharp MZ-80K MZF files (BASIC SP5025) into PDFs
#
# https://github.com/nigelpercy/KMZF2PDF
 
import fpdf
import PIL
import sys
import os.path

def PrintKeyWord(keyword,pColNumber,pRowNumber):
  for x in range(0, len(keyword)):
    PrintCharacter(ord(keyword[x]),pColNumber,pRowNumber)
    pColNumber = colNumber

def PrintCharacter(character,pColNumber,pRowNumber):
  global colNumber
  singleChar = bytearray(CGROM[(character * 8) :(character * 8) + 8])
  for x in range(0, 8):
    singleChar[x] ^= 0xFF # Invert the bitmap so it is black on white
  pdf.image(PIL.Image.frombytes('1', (8, 8), bytes(singleChar)),pColNumber,pRowNumber)
  colNumber = pColNumber + COLUMNSPACING

# Dump of the MZ-80K CG-ROM in ASCII order
CGROM = bytes([
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0xFF, 0xF7, 0xF7, 0xF7, 0xD5, 0xE3, 0xF7, 0xFF,0xFF, 0xF7, 0xE3, 0xD5, 0xF7, 0xF7, 0xF7, 0xFF,
0xFF, 0xFF, 0xF7, 0xFB, 0x81, 0xFB, 0xF7, 0xFF,0xFF, 0xFF, 0xEF, 0xDF, 0x81, 0xDF, 0xEF, 0xFF,0xBD, 0xBD, 0xBD, 0x81, 0xBD, 0xBD, 0xBD, 0xFF,
0xE3, 0xDD, 0xBF, 0xBF, 0xBF, 0xDD, 0xE3, 0xFF,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x08, 0x08, 0x08, 0x08, 0x00, 0x00, 0x08, 0x00, 0x24, 0x24, 0x24, 0x00, 0x00, 0x00, 0x00, 0x00, 0x24, 0x24, 0x7E, 0x24, 0x7E, 0x24, 0x24, 0x00,
0x08, 0x1E, 0x28, 0x1C, 0x0A, 0x1C, 0x08, 0x00, 0x00, 0x62, 0x64, 0x08, 0x10, 0x26, 0x46, 0x00, 0x30, 0x48, 0x48, 0x30, 0x4A, 0x44, 0x3A, 0x00,
0x04, 0x08, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x08, 0x10, 0x10, 0x10, 0x08, 0x04, 0x00, 0x20, 0x10, 0x08, 0x08, 0x08, 0x10, 0x20, 0x00,
0x08, 0x2A, 0x1C, 0x3E, 0x1C, 0x2A, 0x08, 0x00, 0x00, 0x08, 0x08, 0x3E, 0x08, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08, 0x10,
0x00, 0x00, 0x00, 0x7E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x18, 0x00, 0x00, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x00,
0x3C, 0x42, 0x46, 0x5A, 0x62, 0x42, 0x3C, 0x00, 0x08, 0x18, 0x28, 0x08, 0x08, 0x08, 0x3E, 0x00, 0x3C, 0x42, 0x02, 0x0C, 0x30, 0x40, 0x7E, 0x00,
0x3C, 0x42, 0x02, 0x3C, 0x02, 0x42, 0x3C, 0x00, 0x04, 0x0C, 0x14, 0x24, 0x7E, 0x04, 0x04, 0x00, 0x7E, 0x40, 0x78, 0x04, 0x02, 0x44, 0x38, 0x00,
0x1C, 0x20, 0x40, 0x7C, 0x42, 0x42, 0x3C, 0x00, 0x7E, 0x42, 0x04, 0x08, 0x10, 0x10, 0x10, 0x00, 0x3C, 0x42, 0x42, 0x3C, 0x42, 0x42, 0x3C, 0x00,
0x3C, 0x42, 0x42, 0x3E, 0x02, 0x04, 0x38, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x08, 0x08, 0x10,
0x0E, 0x18, 0x30, 0x60, 0x30, 0x18, 0x0E, 0x00, 0x00, 0x00, 0x7E, 0x00, 0x7E, 0x00, 0x00, 0x00, 0x70, 0x18, 0x0C, 0x06, 0x0C, 0x18, 0x70, 0x00,
0x3C, 0x42, 0x02, 0x0C, 0x10, 0x00, 0x10, 0x00, 0x1C, 0x22, 0x4A, 0x56, 0x4C, 0x20, 0x1E, 0x00, 0x18, 0x24, 0x42, 0x7E, 0x42, 0x42, 0x42, 0x00,
0x7C, 0x22, 0x22, 0x3C, 0x22, 0x22, 0x7C, 0x00, 0x1C, 0x22, 0x40, 0x40, 0x40, 0x22, 0x1C, 0x00, 0x78, 0x24, 0x22, 0x22, 0x22, 0x24, 0x78, 0x00,
0x7E, 0x40, 0x40, 0x78, 0x40, 0x40, 0x7E, 0x00, 0x7E, 0x40, 0x40, 0x78, 0x40, 0x40, 0x40, 0x00, 0x1C, 0x22, 0x40, 0x4E, 0x42, 0x22, 0x1C, 0x00,
0x42, 0x42, 0x42, 0x7E, 0x42, 0x42, 0x42, 0x00, 0x1C, 0x08, 0x08, 0x08, 0x08, 0x08, 0x1C, 0x00, 0x0E, 0x04, 0x04, 0x04, 0x04, 0x44, 0x38, 0x00,
0x42, 0x44, 0x48, 0x70, 0x48, 0x44, 0x42, 0x00, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x7E, 0x00, 0x42, 0x66, 0x5A, 0x5A, 0x42, 0x42, 0x42, 0x00,
0x42, 0x62, 0x52, 0x4A, 0x46, 0x42, 0x42, 0x00, 0x18, 0x24, 0x42, 0x42, 0x42, 0x24, 0x18, 0x00, 0x7C, 0x42, 0x42, 0x7C, 0x40, 0x40, 0x40, 0x00,
0x18, 0x24, 0x42, 0x42, 0x4A, 0x24, 0x1A, 0x00, 0x7C, 0x42, 0x42, 0x7C, 0x48, 0x44, 0x42, 0x00, 0x3C, 0x42, 0x40, 0x3C, 0x02, 0x42, 0x3C, 0x00,
0x3E, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x00, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x3C, 0x00, 0x42, 0x42, 0x42, 0x24, 0x24, 0x18, 0x18, 0x00,
0x42, 0x42, 0x42, 0x5A, 0x5A, 0x66, 0x42, 0x00, 0x42, 0x42, 0x24, 0x18, 0x24, 0x42, 0x42, 0x00, 0x22, 0x22, 0x22, 0x1C, 0x08, 0x08, 0x08, 0x00,
0x7E, 0x02, 0x04, 0x18, 0x20, 0x40, 0x7E, 0x00, 0x3C, 0x20, 0x20, 0x20, 0x20, 0x20, 0x3C, 0x00, 0x00, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x00,
0x3C, 0x04, 0x04, 0x04, 0x04, 0x04, 0x3C, 0x00, 0x00, 0x08, 0x1C, 0x2A, 0x08, 0x08, 0x08, 0x00, 0x00, 0x00, 0x10, 0x20, 0x7F, 0x20, 0x10, 0x00,
0x18, 0x24, 0x7E, 0xFF, 0x5A, 0x24, 0x00, 0x00, 0xE0, 0x47, 0x42, 0x7E, 0x42, 0x47, 0xE0, 0x00, 0x22, 0x3E, 0x2A, 0x08, 0x08, 0x49, 0x7F, 0x41,
0x1C, 0x1C, 0x08, 0x3E, 0x08, 0x08, 0x14, 0x22, 0x00, 0x11, 0xD2, 0xFC, 0xD2, 0x11, 0x00, 0x00, 0x00, 0x88, 0x4B, 0x3F, 0x4B, 0x88, 0x00, 0x00,
0x22, 0x14, 0x08, 0x08, 0x3E, 0x08, 0x1C, 0x1C, 0x3C, 0x7E, 0xFF, 0xDB, 0xFF, 0x67, 0x7E, 0x3C, 0x3C, 0x42, 0x81, 0xA5, 0x81, 0x99, 0x42, 0x3C,
0x00, 0xC0, 0xC8, 0x54, 0x54, 0x55, 0x22, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xAA, 0x55, 0xAA, 0x55, 0xAA, 0x55, 0xAA, 0x55, 0x0A, 0x05, 0x0A, 0x05, 0x0A, 0x05, 0x0A, 0x05,
0xA0, 0x50, 0xA0, 0x50, 0xA0, 0x50, 0xA0, 0x50, 0xAA, 0x55, 0xAA, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xAA, 0x55, 0xAA, 0x55,
0xAA, 0x54, 0xA8, 0x50, 0xA0, 0x40, 0x80, 0x00, 0xAA, 0x55, 0x2A, 0x15, 0x0A, 0x05, 0x02, 0x01, 0x80, 0x40, 0xA0, 0x50, 0xA8, 0x54, 0xAA, 0x55,
0x00, 0x01, 0x02, 0x05, 0x0A, 0x15, 0x2A, 0x55, 0x80, 0x80, 0x40, 0x40, 0x20, 0x20, 0x10, 0x10, 0x08, 0x08, 0x04, 0x04, 0x02, 0x02, 0x01, 0x01,
0x38, 0x28, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x54, 0x2A, 0x54, 0x2A, 0x54, 0x2A, 0x00, 0x01, 0x01, 0x02, 0x02, 0x04, 0x04, 0x08, 0x08,
0x10, 0x10, 0x20, 0x20, 0x40, 0x40, 0x80, 0x80, 0x1C, 0x1C, 0x3E, 0x1C, 0x08, 0x00, 0x3E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x08, 0x08, 0x08, 0x08, 0xFF, 0x08, 0x08, 0x08, 0x03, 0x1C, 0x60, 0x80, 0x00, 0x00, 0x00, 0x00, 0x01, 0x06, 0x18, 0x20, 0x20, 0x40, 0x40, 0x80,
0x80, 0x40, 0x40, 0x20, 0x20, 0x18, 0x06, 0x01, 0x00, 0x00, 0x00, 0x00, 0x80, 0x60, 0x1C, 0x03, 0x80, 0x80, 0x40, 0x40, 0x40, 0x20, 0x20, 0x10,
0xC0, 0x38, 0x06, 0x01, 0x00, 0x00, 0x00, 0x00, 0x80, 0x60, 0x18, 0x04, 0x04, 0x02, 0x02, 0x01, 0x01, 0x02, 0x02, 0x04, 0x04, 0x18, 0x60, 0x80,
0x00, 0x00, 0x00, 0x00, 0x01, 0x06, 0x38, 0xC0, 0x24, 0x24, 0x24, 0x24, 0xC3, 0x81, 0x42, 0x3C, 0x00, 0x00, 0x00, 0x80, 0x40, 0x20, 0x10, 0x08,
0x08, 0x04, 0x04, 0x02, 0x02, 0x02, 0x01, 0x01, 0x01, 0x01, 0x02, 0x02, 0x02, 0x04, 0x04, 0x08, 0x08, 0x10, 0x20, 0x40, 0x80, 0x00, 0x00, 0x00,
0x00, 0x3C, 0x7A, 0xA9, 0xA9, 0x7A, 0x3C, 0x00, 0x44, 0xFF, 0x44, 0x44, 0x44, 0xFF, 0x44, 0x44, 0x00, 0x00, 0x3C, 0x42, 0x7E, 0x40, 0x3C, 0x00,
0x22, 0x44, 0x88, 0x11, 0x22, 0x44, 0x88, 0x11, 0x88, 0x44, 0x22, 0x11, 0x88, 0x44, 0x22, 0x11, 0xAA, 0x44, 0xAA, 0x11, 0xAA, 0x44, 0xAA, 0x11,
0x10, 0x10, 0x7C, 0x10, 0x10, 0x12, 0x0C, 0x00, 0x00, 0x00, 0x3A, 0x46, 0x46, 0x3A, 0x02, 0x3C, 0x40, 0x40, 0x5C, 0x62, 0x42, 0x42, 0x42, 0x00,
0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x40, 0x40, 0x5C, 0x62, 0x42, 0x62, 0x5C, 0x00, 0x00, 0x00, 0x44, 0x28, 0x10, 0x28, 0x44, 0x00,
0x02, 0x02, 0x3A, 0x46, 0x42, 0x46, 0x3A, 0x00, 0x00, 0x00, 0x5C, 0x62, 0x40, 0x40, 0x40, 0x00, 0x00, 0x00, 0x5C, 0x62, 0x62, 0x5C, 0x40, 0x40,
0x00, 0x00, 0x3C, 0x42, 0x40, 0x42, 0x3C, 0x00, 0x00, 0x00, 0x3A, 0x46, 0x46, 0x3A, 0x02, 0x02, 0x00, 0x00, 0x38, 0x04, 0x3C, 0x44, 0x3A, 0x00,
0x00, 0x00, 0x7E, 0x04, 0x18, 0x20, 0x7E, 0x00, 0x00, 0x00, 0x41, 0x49, 0x49, 0x49, 0x36, 0x00, 0x00, 0x00, 0x3E, 0x40, 0x3C, 0x02, 0x7C, 0x00,
0x00, 0x00, 0x42, 0x42, 0x42, 0x42, 0x3C, 0x00, 0x08, 0x00, 0x18, 0x08, 0x08, 0x08, 0x1C, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00,
0x42, 0x18, 0x24, 0x42, 0x42, 0x24, 0x18, 0x00, 0x40, 0x40, 0x44, 0x48, 0x50, 0x68, 0x44, 0x00, 0x0C, 0x12, 0x10, 0x7C, 0x10, 0x10, 0x10, 0x00,
0x00, 0x00, 0x42, 0x42, 0x42, 0x24, 0x18, 0x00, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x00, 0x22, 0x00, 0x22, 0x22, 0x22, 0x1C, 0x00,
0x38, 0x44, 0x44, 0x4A, 0x42, 0x52, 0x4C, 0x00, 0x04, 0x00, 0x0C, 0x04, 0x04, 0x04, 0x44, 0x38, 0x00, 0x00, 0x5C, 0x62, 0x42, 0x42, 0x42, 0x00,
0x10, 0x20, 0x20, 0x40, 0x40, 0x40, 0x80, 0x80, 0x42, 0x00, 0x42, 0x42, 0x42, 0x42, 0x3C, 0x00, 0x00, 0x00, 0x76, 0x49, 0x49, 0x49, 0x49, 0x00,
0x00, 0x00, 0x00, 0x00, 0x03, 0x0C, 0x30, 0xC0, 0x03, 0x0C, 0x30, 0xC0, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x30, 0x0C, 0x03, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x3C, 0x42, 0x42, 0x42, 0x3C, 0x00, 0x18, 0x08, 0x08, 0x08, 0x08, 0x08, 0x1C, 0x00, 0x42, 0x18, 0x24, 0x42, 0x7E, 0x42, 0x42, 0x00,
0x00, 0x22, 0x00, 0x1C, 0x22, 0x22, 0x1C, 0x00, 0x24, 0x00, 0x38, 0x04, 0x3C, 0x44, 0x3A, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x30, 0x0C, 0x03,
0x00, 0x00, 0x42, 0x42, 0x46, 0x3A, 0x02, 0x3C, 0x22, 0x14, 0x3E, 0x08, 0x3E, 0x08, 0x08, 0x00, 0x10, 0x08, 0x04, 0x02, 0x01, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,
0x00, 0x00, 0x04, 0x02, 0x7F, 0x02, 0x04, 0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0xFE, 0xFC, 0xF8, 0xF0, 0xE0, 0xC0, 0x80, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x08, 0x08, 0x08, 0x08, 0x0F, 0x08, 0x08, 0x08,
0xFF, 0xC3, 0x81, 0x81, 0x81, 0x81, 0xC3, 0xFF, 0x08, 0x08, 0x08, 0x08, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF8, 0x08, 0x08, 0x08,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0xFF, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0xFF, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0xF8, 0x08, 0x08, 0x08, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0,
0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0xFF,
0x00, 0x00, 0x00, 0x00, 0x03, 0x04, 0x08, 0x08, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x20, 0x10, 0x10, 0x08, 0x08, 0x08, 0x08, 0xF8, 0x00, 0x00, 0x00,
0x0F, 0x0F, 0x0F, 0x0F, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0x0F, 0x0F, 0x0F, 0x0F, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x00,
0x08, 0x1C, 0x3E, 0x7F, 0x7F, 0x1C, 0x3E, 0x00, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00,
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x80, 0xC0, 0xE0, 0xF0, 0xF8, 0xFC, 0xFE, 0xFF,
0x08, 0x08, 0x04, 0x03, 0x00, 0x00, 0x00, 0x00, 0x10, 0x10, 0x20, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0xFF,
0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0xFF, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80,
0xFF, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x3C, 0x7E, 0x7E, 0x7E, 0x7E, 0x3C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00,
0x36, 0x7F, 0x7F, 0x7F, 0x3E, 0x1C, 0x08, 0x00, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3F, 0x7F, 0xFF,
0x81, 0x42, 0x24, 0x18, 0x18, 0x24, 0x42, 0x81, 0x00, 0x3C, 0x42, 0x42, 0x42, 0x42, 0x3C, 0x00, 0x08, 0x1C, 0x2A, 0x7F, 0x2A, 0x08, 0x08, 0x00,
0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x08, 0x1C, 0x3E, 0x7F, 0x3E, 0x1C, 0x08, 0x00, 0x0C, 0x12, 0x10, 0x38, 0x10, 0x10, 0x3E, 0x00,
0x00, 0x08, 0x08, 0x08, 0x2A, 0x1C, 0x08, 0x00, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0xFF, 0x7F, 0x3F, 0x1F, 0x0F, 0x07, 0x03, 0x01,
0x00, 0x00, 0x01, 0x3E, 0x54, 0x14, 0x14, 0x00,
])

 

CursorDict = {17: 10, 18: 11,19: 12,20: 13,21: 14,22: 15}
LowerCaseDict = {161: 1, 154: 1, 159: 1, 156: 1, 146: 1, 170: 1, 151: 1, 152: 1, 166: 1, 175: 1, 169: 1, 184: 1, 179: 1, 176: 1, 183: 1, 158: 1, 160: 1, 157: 1, 164: 1, 150: 1,
                 165: 1, 171: 1, 163: 1, 155: 1, 189: 1, 162: 1}
MathSymbolDict =  {176: '><', 177: '<>',178: '=<', 179: '<=', 180: '=>',181: '>=',182: '=',183: '>',184: '<',188: '+',189:  '-',190: '*',191: '/',255: 'π',207: '↑'}
KeywordDict =  {129: 'DATA', 130: 'LIST', 131: 'RUN', 132: 'NEW', 133: 'PRINT',134: 'LET', 135: 'FOR', 136: 'IF', 137: 'GOTO', 138: 'READ', 139: 'GOSUB', 140: 'RETURN',
                141: 'NEXT', 142: 'STOP', 143: 'END', 144: 'ON', 145: 'LOAD', 146: 'SAVE', 147: 'VERIFY', 148: 'POKE', 149: 'DIM', 150: 'DEF FN', 151: 'INPUT', 152: 'RESTORE',
                153: 'CLR', 154: 'MUSIC', 155: 'TEMPO',156: 'USR(', 157: 'WOPEN', 158: 'ROPEN', 159: 'CLOSE',160: 'BYE', 161: 'LIMIT', 162: 'CONT', 163: 'SET', 164: 'RESET', 
                165: 'GET', 166: 'INP#', 167: 'OUT#', 173: 'THEN', 174: 'TO', 175: 'STEP', 192: 'LEFT$(', 193: 'RIGHT$(', 194: 'MID$(', 195: 'LEN(', 195: 'LEN(', 196: 'CHR$(', 
                197: 'STR$(', 198: 'ASC(', 199: 'VAL(', 200: 'PEEK(', 201: 'TAB(', 202: 'SPC(', 203: 'SIZE', 208: 'RND(', 209: 'SIN(', 210: 'COS(', 211: 'TAN(', 212: 'ATN(', 
                213: 'EXP(', 214: 'INT(', 215: 'LOG(', 216: 'LN(', 217: 'ABS(', 218: 'SGN(', 219: 'SQR('}

COLUMNSPACING = 3.10
ROWSPACING = 4
LINEWRAPINDENT = 12.3
STARTROW = 5
STARTCOL = 5
MAXIMUMROWS = 290 # Seems to be OK for A4
MAXROWLENGTH = 195
fileName = ''

if len(sys.argv) >= 2:
  fileName = sys.argv[1] 
if os.path.exists(fileName):
  fileHandler = open(fileName, 'rb')

  pdf = fpdf.FPDF()
  pdf.add_page()
  colNumber = STARTCOL
  rowNumber = STARTROW
  openQuote = 0

  programType = fileHandler.read(1).hex()
  # Print the program name
  programName = fileHandler.read(17).hex()
  for x in range(0, 17 ,2):
    hexCode = programName[x:x + 2]
    if hexCode == '0d':
      break
    PrintCharacter(int(hexCode, 16),colNumber,rowNumber)

  rowNumber = rowNumber + ROWSPACING * 2
  colNumber = STARTCOL
  dataByte = fileHandler.read(110).hex()

  while dataByte:
    numberOfBytes = int(fileHandler.read(1).hex(), base=16) # Length of line
    zeroByte = int(fileHandler.read(1).hex(), base=16)
    if numberOfBytes == 0 and zeroByte == 0: # Double 00 00 bytes == EOF
      break
    PrintKeyWord(str(int(fileHandler.read(1).hex(), base=16) + (int(fileHandler.read(1).hex(), base=16) * 256)) + ' ',colNumber,rowNumber) # Line number high/low bytes

    # Read each byte in the line
    for x in range(0, numberOfBytes - 4):
      dataByte = int(fileHandler.read(1).hex(), base=16)
      # Check for open/closing quotes
      if dataByte == 34 and openQuote == 1:
        openQuote = 0
      elif dataByte == 34 and openQuote == 0:
        openQuote = 1

      # Replace CR with Space
      if dataByte == 13:
        PrintCharacter(32,colNumber,rowNumber)

      # Cursor chars
      elif  openQuote == 1 and dataByte >= 17 and dataByte <= 22:
        PrintCharacter(CursorDict[dataByte],colNumber,rowNumber)

      # Math symbols
      elif openQuote == 0 and MathSymbolDict.get(dataByte):
        PrintKeyWord(MathSymbolDict.get(dataByte),colNumber,rowNumber)

      # Lowercase Letters
      elif openQuote == 1 and LowerCaseDict.get(dataByte):
        PrintCharacter(dataByte,colNumber,rowNumber)

      elif openQuote == 1:
        PrintCharacter(dataByte,colNumber,rowNumber)

      # Special case for REM (Treat REM as a quoted string, ignore keyword byte codes)
      elif dataByte == 128:
        PrintKeyWord('REM',colNumber,rowNumber)
        openQuote = 1

      elif KeywordDict.get(dataByte):
        PrintKeyWord(KeywordDict.get(dataByte),colNumber,rowNumber)    
      else:
        PrintCharacter(dataByte,colNumber,rowNumber)

      # Handle line wrap
      if colNumber >= MAXROWLENGTH:
        colNumber = STARTCOL + LINEWRAPINDENT
        rowNumber = rowNumber + ROWSPACING

    colNumber = STARTCOL
    rowNumber = rowNumber + ROWSPACING
    openQuote = 0

    if rowNumber >= MAXIMUMROWS:
      pdf.add_page()
      rowNumber = STARTROW

  rowNumber = rowNumber + ROWSPACING
  PrintKeyWord('*** END OF LISTING ***',colNumber + 60,rowNumber)
  # Save and open PDF
  pdfFileName = os.path.splitext(fileName)[0] + '.pdf'
  pdf.output(pdfFileName)
  os.startfile(pdfFileName)

elif len(sys.argv) < 2:
  print('Usage:- KMZF2PDF filename.mzf')
else:
  print(fileName + ' cannot be found. Please check path & name.')
