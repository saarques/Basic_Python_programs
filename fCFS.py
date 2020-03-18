		
class processes():
	arrival_time = 0 ; burst_time = 0 ; process_id = 0 ; completion_time = 0 ; waiting_time = 0 ; turn_around_time = 0
	def display_processes(self):
		print(str(self.process_id) + "			" + str(self.arrival_time) + "			" + str(self.burst_time) + " 			" 
			+ str(self.completion_time) + " 				" + str(self.waiting_time) + " 				" + str(self.turn_around_time))

def display(n):
	print("Process Id 		Arrival Time 		Burst Time 		Completion Time 		Waiting Time 		Turn Around Time")
	for i in range(n):
		process[i].display_processes()

def completion_time_fcfs(i):
	global total_time
	if total_time < process[i].arrival_time:
		total_time = process[i].arrival_time
		total_time = total_time + process[i].burst_time
	else:
		total_time = total_time + process[i].burst_time
	process[i].completion_time = total_time

def completion_time_sjf(i):
	array = []
	global count, total_time, n
	if total_time < process[i].arrival_time:
		total_time = process[i].arrival_time
	for index in range(count, n):
		if process[index].arrival_time <= total_time:
			array.append(process[index].process_id)
		else:
			break

	# for index in range(n):
	# 	if process[index].process_id == array[0]:
	ultima = count
			# break
	if len(array) == 1:
		total_time += process[ultima].burst_time
		process[ultima].completion_time = total_time
		count += 1
	else:
		for index in range(ultima, ultima + len(array) - 1):
			for iterator in range(ultima, ultima + len(array) - 1):
				if process[iterator].burst_time > process[iterator + 1].burst_time:
					# temp = processes()
					# temp = process[index].burst_time
					# process[index].burst_time = process[index + 1].burst_time
					# process[index + 1].burst_time = temp
					process[iterator].burst_time, process[iterator + 1].burst_time = process[iterator + 1].burst_time, process[iterator].burst_time
		for index in range(ultima, ultima + len(array)):
			total_time += process[index].burst_time
			process[index].completion_time = total_time
			count += 1




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

display(n)
print("\n")
total_time = 0
process.sort(key = lambda x: x.arrival_time)
count = 0


def fcfs(n):
	for i in range(n):
		completion_time_fcfs(i)
	turn_around_time_and_waiting_time(n)
	print("\n")
	display(n)


def sjf(n):
	for index in range(n):
		completion_time_sjf(index)
	turn_around_time_and_waiting_time(n)
	display(n)

# print("*"*40 + "FIRST COME FIRST SERVICE"+ "*"*40)
# fcfs(n)

total_time = 0

print("*"*40 + "SHORTEST JOB FIRST"+ "*"*40)
sjf(n)