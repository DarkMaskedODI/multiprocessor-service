# logic/multiprocessing_impl.py

import multiprocessing

def worker(start, end, queue):
    subtotal = sum(1 / (i * i) for i in range(start, end))
    queue.put(subtotal)

def compute_multiprocessing(j):
    processes = []
    queue = multiprocessing.Queue()
    num_processes = 4
    chunk_size = j // num_processes

    for n in range(num_processes):
        start = n * chunk_size + 1
        end = j + 1 if n == num_processes - 1 else (n + 1) * chunk_size + 1
        p = multiprocessing.Process(target=worker, args=(start, end, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return sum(queue.get() for _ in processes)
