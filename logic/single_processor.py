def compute_single_processor(j):
    return sum(1 / (i * i) for i in range(1, j + 1))