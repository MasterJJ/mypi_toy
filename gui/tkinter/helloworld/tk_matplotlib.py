import tkinter.ttk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from time import sleep


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
canvas1 = FigureCanvasTkAgg(figure1, frame1)
#bar1 = FigureCanvasTkAgg(figure1, root)
canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax1.set_title('rate1')


figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
canvas2 = FigureCanvasTkAgg(figure2, frame2)
#canvas2 = FigureCanvasTkAgg(figure2, root)
canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax2.set_title('rate2')


def move_cursor(event):
    print("mouse ")
    switchUI()


def switchUI():
    print("Switch UI Bt")
    global notebook_page_switch
    if notebook_page_switch == 1:
        #ani.event_source.stop()
        ani.running = False
        #ani_hreatraw.event_source.start()
        ani_hreatraw.running = True

        notebook.select(notebook_page_switch)
        print("Switch UI Bt    1 go page 2")
    else:
        print("Switch UI Bt    2 go page 1")
        notebook_page_switch = 0
        #ani_hreatraw.event_source.stop()
        #ani.event_source.start()
        notebook.select(notebook_page_switch)
        ani.running = True
        ani_hreatraw.running = False
    plt.draw()
    notebook_page_switch += 1

figure1.canvas.mpl_connect("button_press_event", move_cursor)
figure2.canvas.mpl_connect("button_press_event", move_cursor)

button1 = tk.Button(root, overrelief="solid", text="test", width=15, command=switchUI, repeatdelay=1000, repeatinterval=100)
button1.pack()



def data_gen_heartraw(tick=0):
    cnt = 0
    #fb = open('/run/shm/vital_data.txt', 'r')
    fb = open('test.txt', 'r')
    while cnt < 100000:
        #sleep(0.01)
        fb.seek(0)
        sbuf = fb.readline()
        split_str = sbuf.split(",", 1)
        #print(split_str[0])
        #print(split_str[1])
        cnt += 1
        tick += 0.01
        yield tick, int(split_str[0])
    fb.close()

def init_heartraw():
    #ax2.set_ylim(-1.1, 1.1)
    ax1.set_ylim(0, 150)
    ax1.set_xlim(0, 10)
    del xdata_hr[:]
    del ydata_hr[:]
    line_hr.set_data(xdata_hr, ydata_hr)
    return line_hr,

#ax = plt.subplots()
line_hr, = ax1.plot([], [], lw=2)
ax1.grid()
xdata_hr, ydata_hr = [], []


def run_heartraw(data):
    # update the data
    t, y = data
    xdata_hr.append(t)
    ydata_hr.append(y)
    xmin, xmax = ax1.get_xlim()

    if t >= xmax:
        ax1.set_xlim(xmin, 2*xmax)
        ax1.figure.canvas.draw()
    line_hr.set_data(xdata_hr, ydata_hr)

    return line_hr,



ani_hreatraw = animation.FuncAnimation(figure1, run_heartraw, data_gen_heartraw, blit=False, interval=10,
                              repeat=False, init_func=init_heartraw)

def data_gen(t=0):
    cnt = 0
    #fb = open('/run/shm/vital_data.txt', 'r')
    fb = open('test.txt', 'r')
    while cnt < 100000:
        #sleep(0.01)
        fb.seek(0)
        sbuf = fb.readline()
        split_str = sbuf.split(",", 1)
        #print(split_str[0])
        #print(split_str[1])
        cnt += 1
        t += 0.01
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
