import pyqrcode

#from pyqrcode import QRCode

s = "https://www.youtube.com/watch?v=vh9rBp_4eHU"

url = pyqrcode.create(s)
url.png('myqr.png', scale = 6)
url.show()
  

  