import sys
import time
import processing_and_graphs
import collect_data_from_spotify

if __name__ == '__main__':
    
    start = time.time()

    if len(sys.argv) > 1:
        n = sys.argv[1]
    else:
        n = None

    collect_data_from_spotify
    processing_and_graphs.main(n)
    
    print(f"total time: {time.time()-start} seconds")
    sys.exit()