def fcfs(nior, cy, scy):
    thm = [0] * (nior + 1)
    sum_thm = 0

    for i in range(1, nior + 1):
        if i == 1:
            thm[i] = abs(scy - cy[i])  # Calculate head movement from starting cylinder
        else:
            thm[i] = abs(cy[i - 1] - cy[i])
        sum_thm += thm[i]

    st = sum_thm / nior
    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(1, nior + 1):
        print(f"{cy[i]}\t\t\t\t\t{thm[i]}")
    print("-------------------------------------")
    print(f"AVERAGE SEEK TIME IS : {st}")
    print(f"TOTAL HEAD MOVEMENT: {sum_thm}")

if __name__ == "__main__":
    nior = int(input("Enter the Number of IO Requests:\n"))
    # Read space-separated input for cylinder numbers
    cy_input = input(f"Enter Cylinder Numbers (space-separated):\n")
    cy = [0] + list(map(int, cy_input.split()))  # Split and convert to list of integers
    scy = int(input("Enter the Starting Cylinder:\n"))
    
    print("FCFS")
    fcfs(nior, cy, scy)
