from barcode import EAN13
from barcode.writer import ImageWriter

#generacion de codigo#
with open('barcode.png', 'wb') as f:
    EAN13('123456789102', writer=ImageWriter()).write(f)
