import time

start = time.perf_counter()

def do_something():
    print('Sleeping For 1 Second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()
do_something()

end = time.perf_counter()
print(f'Finished in {round(end - start, 2)} --> secs')