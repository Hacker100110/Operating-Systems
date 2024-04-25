def SSTF(NIOR, CY, SCY):
    DCY = CY[:]  # Make a copy of CY to work with
    THM = [0] * (NIOR + 1)
    sum_THM = 0

    for i in range(1, NIOR + 1):
        min_distance = float('inf')
        min_index = -1
        for j in range(1, NIOR + 1):
            if DCY[j] != -1:
                distance = abs(DCY[j] - SCY)
                if distance < min_distance:
                    min_distance = distance
                    min_index = j
        THM[i] = min_distance
        sum_THM += min_distance
        SCY = DCY[min_index]  # Update SCY to the next cylinder to access
        DCY[min_index] = -1  # Mark the accessed cylinder as visited (-1)

    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(1, NIOR + 1):
        print(f"{CY[i]}\t\t\t\t\t{THM[i]}")
    print("-------------------------------------")
    ST = sum_THM / NIOR
    print(f"AVERAGE SEEK TIME IS : {ST}")
    print(f"TOTAL HEAD MOVEMENT: {sum_THM}")

if __name__ == "__main__":
    NIOR = int(input("Enter the Number of IO Requests: "))
    CY = [0] + [int(input(f"Enter Cylinder No {i + 1}: ")) for i in range(NIOR)]
    SCY = int(input("Enter the Starting Cylinder: "))

    print("\nSSTF")
    SSTF(NIOR, CY, SCY)
