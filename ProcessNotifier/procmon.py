import psutil


class Monitor():
	"""Monitors CPU percent and alerts if below a threshold for a certain amount of time. """

	def get_cpu_usage(self):
		return float(self.process.get_cpu_percent())

	def get_ram_usage_in_mb(self):
		ram_in_bytes = self.process.get_memory_info()[0]
		ram_in_megabytes = ram_in_bytes / 1000000.0
		return ram_in_megabytes

	def __init__(self, proc_name, resource):
		self.process = None
		self.get_resource_usage = None
		for proc in psutil.process_iter():
			if proc.name == proc_name:
				self.process = proc

		if self.process is None:
			print(
				"Sorry, we could not find a process with that name! Please start the process before running this script. ")
			raise NameError('No Such Program')
		else:
			print("Found PID " + str(self.process.pid) +
				  " for process named: " + self.process.name)

		#using function assignment to change the monitored resource at runtime.
		if resource == "RAM Amount(MB)":
			self.get_resource_usage = self.get_ram_usage_in_mb
			print(self.get_resource_usage)
		elif resource == "CPU Percent":
			self.get_resource_usage = self.get_cpu_usage
			print(self.get_resource_usage)
		else:
			print(
				"You must enter either CPU or RAM as the resource to be monitored!")
			raise SystemExit(0)
