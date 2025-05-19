import threading

def compute_multithread(j):
    result = [0]
    lock = threading.Lock()

    def worker(start, end):
        subtotal = sum(1 / (i * i) for i in range(start, end))
        with lock:
            result[0] += subtotal

    threads = []
    num_threads = 4
    chunk_size = j // num_threads

    for n in range(num_threads):
        start = n * chunk_size + 1
        end = j + 1 if n == num_threads - 1 else (n + 1) * chunk_size + 1
        t = threading.Thread(target=worker, args=(start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return result[0]
