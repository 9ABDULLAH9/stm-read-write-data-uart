import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial.tools.list_ports
import serial
import csv

def read_and_process_data():
    line = ser.readline().decode('utf-8').strip()
    values = line.split(', ')

    x_vals.append(float(values[0]))
    data1.append(int(values[1]))
    data2.append(int(values[2]))

    print(f'time: {values[0]}, data1: {values[1]}, data2: {values[2]}')

def update_plot(frame):
    read_and_process_data()
    plt.cla()
    plt.plot(x_vals, data1, label='data1')
    plt.plot(x_vals, data2, label='data2')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()

def on_close(event):
    with open(str(filename) + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Data1', 'Data2'])
        for d1, d2 in zip(data1, data2):
            writer.writerow([d1, d2])




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

if (stat == "1"):
	filename = input('Kaydedilecek dosya ismi: ')
	fig, ax = plt.subplots()
	fig.canvas.mpl_connect('close_event', on_close)
	ani = FuncAnimation(fig, update_plot, interval=5)
	plt.show()

if (stat == "2"):
	filename = input('\nGonderilecek dosya ismi: ')
	lp_s ="a"
	while ((lp_s != "y") & (lp_s != "n")):
		lp_s = str(input ("Veri gönderme islemi surekli olsun mu (y/n) "))
	lp_s.lower()

if ((stat == "2") & (lp_s == "n")):
	while True:
		try:
			with open(str(filename) + '.csv', mode= 'r', newline='') as csvfile:
				csv_reader = csv.reader(csvfile, delimiter = ',')

				headline = next(csv_reader)
				print(headline)

				for wrd in csv_reader:
					data = int(wrd[1])
					ser.write(data.to_bytes(1,'little'))
					print(data)
				break
		except FileNotFoundError:
			print("\nboyle bir dosya mevcut degil yeniden deneyiniz")
			filename = input('Gonderilecek dosya ismi: ')
			continue

if ((stat == "2") & (lp_s == "y")):
	while True:
		try:
			with open(str(filename) + '.csv', mode= 'r', newline='') as csvfile:
				csv_reader = csv.reader(csvfile, delimiter = ',')

				headline = next(csv_reader)
				print(headline)

				for wrd in csv_reader:
					data = int(wrd[1])
					ser.write(data.to_bytes(1,'little'))
					print(data)
		except FileNotFoundError:
			print("\nboyle bir dosya mevcut degil yeniden deneyiniz")
			filename = input('Gonderilecek dosya ismi: ')
			continue
