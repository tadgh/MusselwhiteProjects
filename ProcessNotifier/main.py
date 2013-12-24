from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import emailer
import procmon
import datetime
import time
import sys

root = Tk()
root.title("Process Notifier")
mainframe = ttk.Frame(root, padding="3 3 12 12 ")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

email_to_notify = StringVar()
program_to_monitor = StringVar()

resource_threshold = IntVar()
monitored_resource = StringVar()
monitored_resource.set("RAM Amount(MB)")
idle_time_threshold = IntVar()



def start_monitor():
	user = email_to_notify.get()
	process = program_to_monitor.get()
	resource_chosen = monitored_resource.get()
	try:
		resource_amount = int(resource_threshold.get())
		idle_max = int(idle_time_threshold.get())
	except ValueError:
		messagebox.showerror("Value Type Error", message="Oops! You've entered a non-number as a value in\none of the CPU/RAM/Idle boxes.")
		return
	if '@' not in  user:
		messagebox.showerror("Email Error", message="Oops! That does not appear to be a real E-mail address. ")
		return

	print(user)
	print(process)
	print(resource_chosen)
	print(resource_amount)
	print(idle_max)
	users = []
	users.append(user)
	process_to_monitor = process
	idle_time_max = idle_max
	resource_to_monitor = resource_chosen
	resource_minimum = resource_amount
	if resource_to_monitor == 'RAM Amount(MB)':
		print("ram to be monitored...")
	elif resource_to_monitor == 'CPU Percent':
		print("CPU to be monitored...")
	else:
		messagebox.showerror("What!?", message="You somehow managed to select an option\nthat wasn't available in the drop down. Call me because i'm confused.")
	try:
		monitor = procmon.Monitor(process_to_monitor, resource_to_monitor)
	except NameError:
		messagebox.showerror("No Such Process", message="Unable to find a process named" + process + ".\nCapitalization is important.")

	process_is_active = True
	process_idle_cycles = 0
	start_time = datetime.datetime.now()
	while process_is_active:
		resource_usage = monitor.get_resource_usage()
		if resource_usage < resource_minimum:
			process_idle_cycles += 1
			print("process idling...")
		else:
			process_idle_cycles = 0

		if process_idle_cycles > idle_time_max:
			process_is_active = False
		time.sleep(1)

	end_time = datetime.datetime.now()
	time_elapsed = end_time - start_time
	mail_object = emailer.Email(
		users, process_to_monitor,
		time_elapsed, idle_time_max, 10, "cpu")
	mail_object.send_email()




email_label = ttk.Label(mainframe, text="E-mail to notify:")
email_entry = ttk.Entry(mainframe, width=20, textvariable=email_to_notify)
email_label.grid(column=0, row=0)
email_entry.grid(column=1, row=0)


program_label = ttk.Label(mainframe, text="Monitored Process:")
program_entry = ttk.Entry(mainframe, width=20, textvariable=program_to_monitor)
program_label.grid(column=0, row=1)
program_entry.grid(column=1, row=1)


resource_option = ttk.OptionMenu(mainframe, monitored_resource, "","RAM Amount(MB)", "CPU Percent")
resource_entry = ttk.Entry(mainframe, width=20, textvariable=resource_threshold)
resource_option.grid(column=0, row=2)
resource_entry.grid(column=1, row=2)


idle_time_label = ttk.Label(mainframe, text="Max Idle Time:")
idle_time_entry = ttk.Entry(mainframe, width=20, textvariable=idle_time_threshold)
idle_time_label.grid(column=0, row=3)
idle_time_entry.grid(column=1, row=3)


idle_time_entry.delete(0, END)
idle_time_entry.insert(0, 120)


monitor_button = ttk.Button(mainframe, text="Start Monitoring", command=start_monitor)
monitor_button.grid(column=0, row=5, columnspan=2)
root.bind('<Return>', start_monitor)



root.mainloop()
