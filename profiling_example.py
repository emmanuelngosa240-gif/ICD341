import numpy as np

def calculate_statistics(x):
    total = np.sum(x)
    mean = np.mean(x)
    variance = np.var(x)
    result = np.sqrt(variance)
    return total, mean, result

if __name__ == "__main__":
    # Create dummy data so the function has something to process
    data = np.random.normal(size=1_000_000)
    calculate_statistics(data)