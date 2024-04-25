def SCAN(NIOR, CY, SCY, MCY):
    LCY = []
    RCY = []
    for i in range(1, NIOR + 1):
        if CY[i] <= SCY:
            LCY.append(CY[i])
        else:
            RCY.append(CY[i])
    LCY.append(0)
    RCY.append(MCY)
    LCY.sort(reverse=True)
    RCY.sort()

    DCY = LCY + RCY
    THM = [0] * len(DCY)
    sum_THM = 0

    for i in range(len(DCY)):
        if i == 0:
            THM[i] = abs(SCY - DCY[i])
        else:
            THM[i] = abs(DCY[i - 1] - DCY[i])
        sum_THM += THM[i]

    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(len(DCY)):
        print(f"{DCY[i]}\t\t\t\t\t{THM[i]}")
    print("-------------------------------------")
    ST = sum_THM / NIOR
    print(f"AVERAGE SEEK TIME IS : {ST}")
    print(f"TOTAL HEAD MOVEMENT: {sum_THM}")
if __name__ == "__main__":
    NIOR = int(input("Enter the Number of IO Request \n"))
    CY = [0] + [int(input("Enter the Cylinder No \n")) for _ in range(NIOR)]
    SCY = int(input("Enter the Starting Cylinder \n"))
    MCY = int(input("Enter the Maximum Cylinder \n"))

   
    print("\nSCAN")
    SCAN(NIOR, CY, SCY, MCY)
   

