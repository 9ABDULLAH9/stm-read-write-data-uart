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