import tkinter.ttk
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from time import sleep


Data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
         'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
         }

df1 = DataFrame(Data1, columns=['Country', 'GDP_Per_Capita'])
df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()

root = tk.Tk()

notebook = tkinter.ttk.Notebook(root, width=600, height=500)
notebook.pack()

frame1 = tkinter.Frame(root)
notebook.add(frame1, text="페이지1")

frame2 = tkinter.Frame(root)
notebook.add(frame2, text="페이지2")
notebook_page_switch = 1


'''
## fullscreen mode 
root.attributes("-fullscreen", True)
'''

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)

bar1 = FigureCanvasTkAgg(figure1, frame1)
#bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')


figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)

canvas2 = FigureCanvasTkAgg(figure2, frame2)
#canvas2 = FigureCanvasTkAgg(figure2, root)

canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax2.set_title('Year Vs. Unemployment Rate')


def move_cursor(event):
    print("mouse ")
    switchUI()


def switchUI():
    print("Switch UI Bt")
    global notebook_page_switch
    notebook.select(notebook_page_switch)
    notebook_page_switch += 1
    if notebook_page_switch > 1:
        notebook_page_switch = 0



figure1.canvas.mpl_connect("button_press_event", move_cursor)
figure2.canvas.mpl_connect("button_press_event", move_cursor)
#cid = plt.connect("motion_notify_event", move_cursor)

button1 = tk.Button(root, overrelief="solid",text="test", width=15, command=switchUI, repeatdelay=1000, repeatinterval=100)
button1.pack()

def data_gen(t=0):
    cnt = 0
    #fb = open('/run/shm/vital_data.txt', 'r')
    fb = open('test.txt', 'r')
    while cnt < 100000:
        sleep(0.01)
        fb.seek(0)
        sbuf = fb.readline()
        split_str = sbuf.split(",", 1)
        #print(split_str[0])
        #print(split_str[1])
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

root.mainloop()
