import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial.tools.list_ports
import serial
import csv

print("Programimiza hoş geldiniz\nMeyt9\n")





ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portlist = []

for onePort in ports:
	portlist.append(str(onePort))
	print(str(onePort))

val = input ('Port seçin: COM')
br = input ('\nBant genişliği seçin: ')
ser = None

while ser is None:
    try:
        ser = serial.Serial('COM' + val, br, timeout=1)
    except serial.serialutil.SerialException as e:
        print("\nBu com port şu anda kullanılamıyor, lütfen yeniden deneyin.")
        val = input ('Port seçin: COM')

x_vals = []
data1 = []
data2 = []

stat = -1

while ((stat != "1") & (stat != "2")):
	stat = input("\n1-Data okuma\n2-Data gonderme\nProgram modunu seçiniz: ")
