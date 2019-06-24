import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import numpy as np
from time import sleep



Data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
         'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
         }

df1 = DataFrame(Data1, columns=['Country', 'GDP_Per_Capita'])
df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()



root = tk.Tk()
'''
## fullscreen mode 
root.attributes("-fullscreen", True)
'''
figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
canvas2 = FigureCanvasTkAgg(figure2, root)
canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax2.set_title('Year Vs. Unemployment Rate')

def data_gen(t=0):
    cnt = 0
    fb = open('/run/shm/vital_data.txt', 'r')
    #fb = open('test.txt', 'r')
    while cnt < 100000:
        sleep(0.01)
        fb.seek(0)
        sbuf = fb.readline()
        split_str = sbuf.split(",", 1)
        print(split_str[0])
        print(split_str[1])
        cnt += 1
        t += 0.1
        yield t, int(split_str[0])
        #yield t, int(split_str[0]) * 0.01
        '''
        cnt += 1
        t += 0.1
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
        # yield t, 1
        '''

    fb.close()

def init():
    #ax2.set_ylim(-1.1, 1.1)
    ax2.set_ylim(0, 150)
    ax2.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

#ax = plt.subplots()
line, = ax2.plot([], [], lw=2)
ax2.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax2.get_xlim()

    if t >= xmax:
        ax2.set_xlim(xmin, 2*xmax)
        ax2.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(figure2, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
#plt.show()

root.mainloop()
