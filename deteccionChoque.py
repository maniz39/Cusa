import Tkinter
import cv2
from datetime import date, datetime
import ftplib
import sqlite3


def diffImg(i0,i1,i2):
    d1 = cv2.absdiff(i2, i1)
    d2 = cv2.absdiff(i1, i0)
    return cv2.bitwise_and(d1, d2)
"""captura = cv2.VideoCapture(0)
def getImg():
    return cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)"""

   
def movimiento():
	captura = cv2.VideoCapture(0)
	cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)
	t1 = cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)
	t2 = cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)
	t3 = cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)

	movimientonivel = 0
	extension2 = 'tiff'
	con2 = 500000
	x= 0
	while True:
		
		diff = diffImg(t1, t2, t3)
		ret, diff = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
		nz = cv2.countNonZero(diff) * 1.
		height, width = diff.shape

		if movimientonivel < 40:
			movimientonivel+=nz/(height * width) * 2000
		if movimientonivel > 0:
			movimientonivel-=1;

		if movimientonivel > 10:
			#time.sleep(1)
			con2+= 1
			#x+=1
			print "Movimiento:", movimientonivel
			nombre2=''
			nombre2= str(con2)+"."+extension2
			cv2.imwrite(nombre2,diff)

		cv2.imshow('frame', diff)
		#Cuenta pixeles
		t1 = t2
		t2 = t3
		#t3 = getImg()
		t3 = cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)
   
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break;

	captura.release()
	cv2.destroyAllWindows()


menu = Tkinter.Tk()
menu.mainloop()

