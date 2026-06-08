from tqdm import tqdm
import time

def count(n):
    total = 0
    for _ in tqdm(range(n), desc="идет подсчет", ncols=70, colour="#009FBD"):
        total += 1
        time.sleep(0.1)
    return total

total = count(100)
print(f"всего подсчитано {total}")