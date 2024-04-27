def findWaitingTime(processes, n, bt, wt, quantum, at, ft):  
    rem_bt = [0] * n  
    for i in range(n):  
        rem_bt[i] = bt[i]
    t = 0
    while True:
        done = True  
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum  
                    rem_bt[i] -= quantum  
                else:
                    t = t + rem_bt[i]  
                    wt[i] = t - bt[i]  
                    rem_bt[i] = 0
                    ft[i] = t
        if done:
            break
             
def findTurnAroundTime(processes, n, bt, wt, tat):  
    for i in range(n):
        tat[i] = bt[i] + wt[i]  
 
def findavgTime(processes, n, bt, quantum, at, ft):  
    wt = [0] * n
    tat = [0] * n  
    findWaitingTime(processes, n, bt, wt, quantum, at, ft)  
    findTurnAroundTime(processes, n, bt, wt, tat)  
    total_wt = 0
    total_tat = 0
    print("\nProcess\tBurst Time\tArrival Time\tFinish Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", processes[i], "\t\t", bt[i], "\t\t", at[i], "\t\t", ft[i], "\t\t", wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.5f "%(total_wt /n) )
    print("Average turnaround time = %.5f "% (total_tat / n))  

def displayGanttChart(processes, n, bt, wt, quantum, at, ft):
    print("\nGantt Chart:")
    total_time = sum(bt)
    timeline = []
    t = 0
    while t < total_time:
        for i in range(n):
            if bt[i] > 0:
                exec_time = min(quantum, bt[i])
                timeline.append((processes[i], t, t + exec_time))
                t += exec_time
                bt[i] -= exec_time
    print("------------------------------------------------------------------")
    print("|", end="")
    for t in timeline:
        print(f"     P{t[0]}     |", end="")
    print("\n------------------------------------------------------------------")
    print("0", end=" " * 12)
    for t in timeline:
        print(f"{t[2]}", end=" " * (12 - len(str(t[2]))))
    print()


def main():
    n = int(input("Enter number of processes: "))  
    processes = list(range(1, n+1))
    burst_time = []
    arrival_time = []
    finish_time = [0] * n
    for i in range(n):
        burst_time.append(int(input(f"Enter burst time for process {i+1}: ")))
        arrival_time.append(int(input(f"Enter arrival time for process {i+1}: ")))

    quantum = int(input("Enter time quantum: "))  
    wt = [0] * n
    findavgTime(processes, n, burst_time, quantum, arrival_time, finish_time)
    displayGanttChart(processes, n, burst_time, wt, quantum, arrival_time, finish_time)

if __name__ == "__main__":
    main()

