def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)
    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i]
                break
    return allocation
def display_allocation(process_sizes, allocation):
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process_sizes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{process_sizes[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{process_sizes[i]}\t\tNot Allocated")

def main():
    num_blocks = int(input("Enter the number of memory blocks: "))
    memory_blocks = [int(input(f"Enter size of block {i+1}: ")) for i in range(num_blocks)]
    num_processes = int(input("Enter the number of processes: "))
    process_sizes = [int(input(f"Enter size of process {i+1}: ")) for i in range(num_processes)]

    print("\nFirst Fit Allocation:")
    first_fit_allocation = first_fit(memory_blocks[:], process_sizes)
    display_allocation(process_sizes, first_fit_allocation)
if __name__ == "__main__":
    main()
