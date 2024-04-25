def optimal(page_references, num_frames):
    page_faults = 0
    frames = []
    counter = 0  # Counter to keep track of the current position in page_references
    for page in page_references:
        if page not in frames:
            page_faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                distances = [len(page_references)] * num_frames
                for j, frame in enumerate(frames):
                    if frame in page_references[counter:]:
                        distances[j] = page_references[counter:].index(frame)
                max_distance_index = distances.index(max(distances))
                frames[max_distance_index] = page
        else:
            pass
        
        # Print the frames
        print(frames)
        
        counter += 1  # Increment the counter
    return page_faults
def main():
    page_references = list(map(int, input("Enter page references separated by spaces: ").strip().split()))
    num_frames = int(input("Enter the number of frames: "))

    print("\nOptimal Page Replacement Algorithm:")
    opt_faults = optimal(page_references, num_frames)
    print("Number of page faults:", opt_faults)

if __name__ == "__main__":
    main()
