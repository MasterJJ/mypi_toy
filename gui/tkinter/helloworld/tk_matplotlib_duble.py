import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from PIL import ImageTk, Image
from tkinter import Label
from tkinter import ttk
from tkinter import StringVar
from time import sleep

root = tk.Tk()
#notebook = tkinter.ttk.Notebook(root, width=600, height=500)
#notebook.pack()

#frame1 = tkinter.Frame(root)
#notebook.add(frame1, text="page1")

notebook_page_switch = 1
__grid_tick_x_count_p1 = 0
__grid_tick_x_count_p2 = 0


'''
## fullscreen mode 
root.attributes("-fullscreen", True)
'''

root.geometry('700x500')
root.config(background='white', cursor='none')
figure1 = plt.Figure(figsize=(6, 5), dpi=100)
figure2 = plt.Figure(figsize=(2, 5), dpi=100)
ax5 = figure2.add_subplot(311)
ax1 = figure1.add_subplot(211)

canvas1 = FigureCanvasTkAgg(figure1, root)

canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax1.set_title('rate1')

## image
img = ImageTk.PhotoImage(Image.open("img.png"))
label_1 = Label(root, image = img)
label_1.pack(side = "top", fill = "both", expand = "yes")
#label_1.place(x = 5, y = 5)
label_1.place(relx = 0.8, rely = 0.1)


## firgure 2
#canvas2 = FigureCanvasTkAgg(figure2, root)
#canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)


## textbox 1
rateText1 = StringVar()
rateText1_box = ttk.Entry(root, width = 4, justify=tk.CENTER, font =("Helvetica", 40), textvariable = rateText1)
rateText1_box.pack()
#rateText1_box.place(x = 100, y = 200)
rateText1_box.place(relx = 0.8, rely = 0.35)

## textbox  2
rateText2 = StringVar()
rateText2_box = ttk.Entry(root, width = 4, justify=tk.CENTER, font =("Helvetica", 40), textvariable = rateText2)
rateText2_box.pack()
rateText2_box.place(relx = 0.8, rely = 0.7)

ax2 = figure1.add_subplot(212)
ax2.set_title('rate2')


def move_cursor(event):
    print("mouse ")
    switchUI()


def switchUI():
    print("Switch UI Bt")
    global notebook_page_switch
    global __grid_tick_x_count_p1
    global __grid_tick_x_count_p2

    __grid_tick_x_count_p1 = 0
    __grid_tick_x_count_p2 = 0

    if notebook_page_switch == 1:
        #ani.event_source.stop()
        ani.running = False
        #ani_hreatraw.event_source.start()
        ani_hreatraw.running = True

        print("Switch UI Bt    1 go page 2")
    else:
        print("Switch UI Bt    2 go page 1")
        notebook_page_switch = 0
        #ani_hreatraw.event_source.stop()
        #ani.event_source.start()
        ani.running = True
        ani_hreatraw.running = False

    del xdata_hr[:]
    del ydata_hr[:]
    del xdata[:]
    del ydata[:]
    plt.clf()
    notebook_page_switch += 1

figure1.canvas.mpl_connect("button_press_event", move_cursor)

#button1 = tk.Button(root, overrelief="solid", text="test", width=15, command=switchUI, repeatdelay=1000, repeatinterval=100)
#button1.pack()



def data_gen_heartraw():
    global __grid_tick_x_count_p1
    #fb = open('/run/shm/vital_data.txt', 'r')
    fb = open('test.txt', 'r')
    while True:
        #sleep(0.01)
        fb.seek(0)
        sbuf = fb.readline()
        split_str = sbuf.split(",", 1)
        #print(split_str[0])
        #print(split_str[1])
        __grid_tick_x_count_p1 += 0.1
        if __grid_tick_x_count_p1 > 10:
            __grid_tick_x_count_p1 = 0
            init_heartraw()

        rateText1.set("dd")
        #rateText1_box.insert(tk.END, "dd")
        yield __grid_tick_x_count_p1, int(split_str[0])
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



ani_hreatraw = animation.FuncAnimation(figure1, run_heartraw, data_gen_heartraw, blit=False, interval=100,
                              repeat=False, init_func=init_heartraw)

def data_gen():
    global __grid_tick_x_count_p2
    #fb = open('/run/shm/vital_data.txt', 'r')
    fb = open('test.txt', 'r')
    while True:
        fb.seek(0)
        sbuf = fb.readline()
        split_str = sbuf.split(",", 1)
        #print(split_str[0])
        #print(split_str[1])
        __grid_tick_x_count_p2 += 0.1
        if __grid_tick_x_count_p2 > 10:
            __grid_tick_x_count_p2 = 0
            init()

        yield __grid_tick_x_count_p2, int(split_str[0])
        #yield t, int(split_str[0]) * 0.01

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


ani = animation.FuncAnimation(figure1, run, data_gen, blit=False, interval=100,
                              repeat=False, init_func=init)

root.mainloop()
