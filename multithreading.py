# import time
# import multiprocessing
# import sys

# def square_numbers():
#     for i in range(5):
#         time.sleep(1)
#         print(f"Square: {i * i}")

# def cube_numbers():
#     for i in range(5):
#         time.sleep(1)
#         print(f"Cube: {i * i * i}")

# if __name__ == "__main__":
#     multiprocessing.set_executable(sys.executable)  # ✅ Correct way to set interpreter

#     p1 = multiprocessing.Process(target=square_numbers)
#     p2 = multiprocessing.Process(target=cube_numbers)

#     t = time.time()

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     finished_time = time.time() - t
#     print(f"Finished in {finished_time:.2f} seconds")


## Multiprocessing
# from concurrent.futures import ThreadPoolExecutor
# import time

# def print_number(number):
#     time.sleep(1)
#     return f"Number :{number}"

# numbers=[1,2,3,4,5]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results=executor.map(print_number,numbers)

#     for result in results:
#         print(result)

##ProcessPoolExecution

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square:{number * number}"

numbers=[1,2,3,4,5,6,7,8,9]
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)

        for result in results:
            print(result)


