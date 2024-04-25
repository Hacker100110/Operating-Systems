def fifo(page_references, num_frames):
    page_faults = 0
    frames = []
    replace_index = 0  # Index to keep track of the position to replace
    for page in page_references:
        if page not in frames:
            page_faults += 1
            if len(frames) == num_frames:
                removed_page = frames[replace_index]
                frames[replace_index] = page
                replace_index = (replace_index + 1) % num_frames  # Update the replace index
            else:
                frames.append(page)
        # Print the frames
        print(frames)
    return page_faults
def main():
    page_references = list(map(int, input("Enter page references separated by spaces: ").strip().split()))
    num_frames = int(input("Enter the number of frames: "))
    
    print("\nFIFO Page Replacement Algorithm:")
    fifo_faults = fifo(page_references, num_frames)
    print("Number of page faults:", fifo_faults)
if __name__ == "__main__":
    main()
