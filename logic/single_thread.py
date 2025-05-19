def compute_single_thread(j):
    return sum(1 / (i * i) for i in range(1, j + 1))