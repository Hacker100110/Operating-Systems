def calculate_waiting_time(start_times, arrival_times):
    return [start - arrival for start, arrival in zip(start_times, arrival_times)]

def calculate_turnaround_time(finish_times, arrival_times):
    return [finish - arrival for finish, arrival in zip(finish_times, arrival_times)]

def calculate_average(values):
    return sum(values) / len(values)

def display_results(processes, burst_times, start_times, finish_times, waiting_times, turnaround_times, arrival_times):
    print("Process\tBurst Time\tArrival Time\tStart Time\tFinish Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{burst_times[i]}\t\t{arrival_times[i]}\t\t{start_times[i]}\t\t{finish_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
    
    print("\nGantt Chart:")
    print("-" * 50)
    print("|", end="")
    for i in range(len(processes)):
        print(f"   {processes[i]}   |", end="")
    print("\n" + "-" * 50)
    print("0", end=" " * 9)
    for time in finish_times:
        print(f"{time}", end=" " * (9 - len(str(time))))
    print()

    print(f"\nAverage Waiting Time: {calculate_average(waiting_times)}")
    print(f"Average Turnaround Time: {calculate_average(turnaround_times)}")

def sjf(processes, burst_times, arrival_times):
    n = len(processes)
    start_times = [0] * n
    finish_times = [0] * n
    
    # Sort processes based on burst time
    sorted_processes = [x for _, x in sorted(zip(burst_times, processes))]
    sorted_burst_times = sorted(burst_times)
    sorted_arrival_times = [x for _, x in sorted(zip(burst_times, arrival_times))]
    
    # Calculate start and finish times
    for i in range(n):
        if i == 0:
            start_times[i] = sorted_arrival_times[i]
        else:
            start_times[i] = finish_times[i - 1]
        finish_times[i] = start_times[i] + sorted_burst_times[i]

    waiting_times = calculate_waiting_time(start_times, arrival_times)
    turnaround_times = calculate_turnaround_time(finish_times, arrival_times)
    
    display_results(sorted_processes, sorted_burst_times, start_times, finish_times, waiting_times, turnaround_times, sorted_arrival_times)

if __name__ == "__main__":
    processes = []
    burst_times = []
    arrival_times = []
    
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        process = input(f"Enter process name for process {i + 1}: ")
        processes.append(process)
        burst_time = int(input(f"Enter burst time for process {process}: "))
        burst_times.append(burst_time)
        arrival_time = int(input(f"Enter arrival time for process {process}: "))
        arrival_times.append(arrival_time)
    
    print("\nSJF Scheduling:")
    sjf(processes, burst_times, arrival_times)
