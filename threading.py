import concurrent.futures
import time


start = time.perf_counter()
def do_something(secs: int):
    print(f'Sleeping {secs} second...')
    time.sleep(secs)
    return f'Done Sleeping... {secs}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    # returns result in the order at which the function is passed or started
    results = executor.map(do_something, secs)
    #for res in results:
    #    print(res)

    # returns results as they're being completed
    # results = [executor.submit(do_something, sec) for sec in secs]
    
    # for f in concurrent.futures.as_completed(results):
    #   print(f.result())

"""
# Old Way Of Running Threads
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=(5,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
"""

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
