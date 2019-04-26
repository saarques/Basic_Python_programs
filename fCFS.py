		
class processes():
	arrival_time = 0 ; burst_time = 0 ; process_id = 0 ; completion_time = 0 ; waiting_time = 0 ; turn_around_time = 0
	def display_processes(self):
		print(str(self.process_id) + "			" + str(self.arrival_time) + "			" + str(self.burst_time) + " 			" 
			+ str(self.completion_time) + " 				" + str(self.waiting_time) + " 				" + str(self.turn_around_time))

def display(n):
	print("Process Id 		Arrival Time 		Burst Time 		Completion Time 		Waiting Time 		Turn Around Time")
	for i in range(n):
		process[i].display_processes()

def completion_time(i):
	global total_time
	if total_time < process[i].arrival_time:
		total_time = process[i].arrival_time
		total_time = total_time + process[i].burst_time
	else:
		total_time = total_time + process[i].burst_time
	process[i].completion_time = total_time

def turn_around_time_and_waiting_time(n):
	for i in range(n):
		process[i].turn_around_time = process[i].completion_time - process[i].arrival_time
		process[i].waiting_time = process[i].turn_around_time - process[i].burst_time


# Creating Processes
n = int(input("Enter no. of processes: "))
process = [processes() for i in range(n)]
for i in range(n):
	process[i].process_id = "P" + str(i)
	process[i].arrival_time = int(input("Enter arrival time of the process P" + str(i) + "(in seconds): "))
	process[i].burst_time = int(input("Enter burst time of the process P" + str(i) + "(in seconds): "))
	print("\n")

# print(process[1].arrival_time)

display(n)

process.sort(key = lambda x: x.arrival_time)
print("\n")
display(n)

# Create variable for total time

total_time = 0
for i in range(n):
	completion_time(i)
turn_around_time_and_waiting_time(n)
print("\n")
display(n)