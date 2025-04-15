import tkinter as tk
from olympe import Drone
import olympe
import numpy as np

#Olympe drone object
drone = Drone("10.202.0.1")  #Replace with your drone's actual IP address

#GUI functions
def connect_to_drone():
    if drone.connect(): #guarantees that the drone is connected, error in connection might skip the Exception
        status_label.config(text="Connected to Parrot Anafi", fg="green")
        print('[ControllerGUI] Connected to the drone!')
    else:
        status_label.config(text=f"Failed to connect!", fg="red")

def takeoff():
    try:
        drone(olympe.messages.ardrone3.Piloting.TakeOff()).wait().success()
        status_label.config(text="Parrot Anafi is taking off", fg="green")
    except Exception as e:
        status_label.config(text=f"Takeoff failed: {str(e)}", fg="red")

def land():
    try:
        drone(olympe.messages.ardrone3.Piloting.Landing()).wait().success()
        status_label.config(text="Parrot Anafi is landing", fg="green")
    except Exception as e:
        status_label.config(text=f"Landing failed: {str(e)}", fg="red")

def emergency():
    try:
        drone(olympe.messages.ardrone3.Piloting.Emergency()).wait().success()
        status_label.config(text="Emergency stop!", fg="red")
    except Exception as e:
        status_label.config(text=f"Emergency failed: {str(e)}", fg="red")

def move():
    try:
        d_axis = np.array([dx_entry.get(), dy_entry.get(), dz_entry.get(), psi_entry.get()]) #list all the text entries
        drone(olympe.messages.ardrone3.Piloting.moveBy(float(d_axis[0]),
                                                        float(d_axis[1]),
                                                        float(d_axis[2]),
                                                        np.deg2rad(float(d_axis[3]))
                                                        )).wait().success()  # Forward on the x-axis
        status_label.config(text=f"Drone moving by: x = {float(d_axis[0])}, "
                                  f"y = {float(d_axis[1])}, "
                                  f"z = {float(d_axis[2])}, "
                                  f"psi = {float(d_axis[3])}", fg="green")
    except Exception as e:
        status_label.config(text=f"Move failed: {str(e)}", fg="red")

def disconnect():
    drone.disconnect()
    status_label.config(text="Disconnected from Parrot Anafi", fg="red")
    print('[ControllerGUI] Disconnected from the drone!')

#Define the controller object
controller = tk.Tk() #creates the tkinter interface
controller.title("[TEST] SPADE Drone Control")

#Create the widgets
status_label = tk.Label(controller, text="Disconnected from Parrot Anafi", fg="red")
status_label.grid(column=1, row=0, pady=20)

#Handle Connections
conn_label = tk.Label(controller, text="Connection commands:")
conn_label.grid(column=0, row=1, pady=10)
connect_button = tk.Button(controller, text="Connect to Parrot Anafi", command=connect_to_drone)
connect_button.grid(column=0,row=2, pady=10)
disconnect_button = tk.Button(controller, text="Disconnect", command=disconnect)
disconnect_button.grid(column=1, row=2, pady=20)

#Handle piloting
pilot_label = tk.Label(controller, text="Piloting commands:")
pilot_label.grid(column=0, row=3, pady=10)
takeoff_button = tk.Button(controller, text="Takeoff", command=takeoff)
takeoff_button.grid(column=0, row=4, pady=10)
land_button = tk.Button(controller, text="Land", command=land)
land_button.grid(column=1, row=4, pady=10)
emergency_button = tk.Button(controller, text="Emergency Stop", command=emergency)
emergency_button.grid(column=2, row=4, pady=10)

#Handle drone movement
move_label = tk.Label(controller, text="Movement commands:")
move_label.grid(column=0, row=5, pady=10)
dx_label = tk.Label(controller, text="x-axis:")
dx_label.grid(column=0, row=6)
dx_entry = tk.Entry(textvariable=tk.StringVar(value='0'))
dx_entry.grid(column=1, row=6)
dx2_label = tk.Label(controller, text="units")
dx2_label.grid(column=2, row=6)
dy_label = tk.Label(controller, text="y-axis:")
dy_label.grid(column=0, row=7)
dy_entry = tk.Entry(textvariable=tk.StringVar(value='0'))
dy_entry.grid(column=1, row=7)
dy2_label = tk.Label(controller, text="units")
dy2_label.grid(column=2, row=7)
dz_label = tk.Label(controller, text="z-axis:")
dz_label.grid(column=0, row=8)
dz_entry = tk.Entry(textvariable=tk.StringVar(value='0'))
dz_entry.grid(column=1, row=8)
dz2_label = tk.Label(controller, text="units")
dz2_label.grid(column=2, row=8)
psi_label = tk.Label(controller, text="rotation:")
psi_label.grid(column=0, row=9)
psi_entry = tk.Entry(textvariable=tk.StringVar(value='0'))
psi_entry.grid(column=1, row=9)
psi2_label = tk.Label(controller, text="degrees")
psi2_label.grid(column=2, row=9)
move_button = tk.Button(controller, text="Move drone", command=move)
move_button.grid(column=1, row=10, pady=10)

#Run the Tkinter event loop
controller.mainloop()
