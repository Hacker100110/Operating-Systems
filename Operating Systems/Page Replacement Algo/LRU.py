def lru(page_references, num_frames):
    page_faults = 0
    frames = []
    last_used = {}  # Dictionary to store the last used time of each page
    time = 0  # Variable to keep track of the current time
    for page in page_references:
        if page not in frames:
            page_faults += 1
            if len(frames) == num_frames:
                # Find the page with the oldest last use time
                replace_page = min(frames, key=last_used.get)
                replace_index = frames.index(replace_page)
                frames[replace_index] = page
                del last_used[replace_page]
            else:
                frames.append(page)
            last_used[page] = time  # Update the last used time of the page
        else:
            last_used[page] = time  # Update the last used time of the page
        time += 1  # Increment the time
        print(frames)
    return page_faults



def main():
    page_references = list(map(int, input("Enter page references separated by spaces: ").strip().split()))
    num_frames = int(input("Enter the number of frames: "))
    
    print("\nLRU Page Replacement Algorithm:")
    lru_faults = lru(page_references, num_frames)
    print("Number of page faults:", lru_faults)

if __name__ == "__main__":
    main()
