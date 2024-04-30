def is_safe(processes, allocation, need, available):
    work = available.copy()
    finish = [False] * len(processes)
    safe_sequence = []
    count = 0
    while count < len(processes):
        found = False
        for i in range(len(processes)):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(len(need[i]))):
                    for j in range(len(work)):
                        work[j] += allocation[i][j]
                    safe_sequence.append(processes[i])
                    finish[i] = True
                    count += 1
                    found = True
        if not found:
            return False, []
    return True, safe_sequence

def main():
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resources: "))

    print("Enter allocation matrix:")
    allocation = []
    for _ in range(num_processes):
        allocation.append(list(map(int, input().split())))

    print("Enter maximum matrix:")
    maximum = []
    for _ in range(num_processes):
        maximum.append(list(map(int, input().split())))

    print("Enter available resources:")
    available = list(map(int, input().split()))

    need = [[maximum[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]

    print("Need Matrix:")
    for row in need:
        print(row)

    total_resources = [sum(allocation[i][j] for i in range(num_processes)) + available[j] for j in range(num_resources)]
    print("Total resources:", total_resources)

    processes = list(range(num_processes))
    safe, sequence = is_safe(processes, allocation, need, available)
    if safe:
        print("Safe sequence:", sequence)
    else:
        print("Unsafe state")

if __name__ == "__main__":
    main()

