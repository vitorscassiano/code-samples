import concurrent.futures
import logging
import multiprocessing
import time
import random

def worker(i):
    num = random.randint(0, 10)
    print("dormi {}".format(num))
    time.sleep(num)
    print("acordei {}".format(num))

def main():
    max_cores = multiprocessing.cpu_count()
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO)
    logging.info("Using {} cores".format(max_cores))
    dataframes = range(100)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
        executor.map(worker, dataframes)

if __name__ == "__main__":
    main()