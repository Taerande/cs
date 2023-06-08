import os
from math import ceil
import time
from multiprocessing import Process, Value, Lock

count = Value('i', 0)  # 공유 변수 초기화
lock = Lock()  # 프로세스 동기화를 위한 Lock 객체
max_count = 3000000
num_process = 2
for_range = ceil(max_count/num_process)

print('-------Multi Process------')

def increment(lock):
    global count
    for _ in range(for_range):
        lock.acquire()
        if count.value < max_count:
          count.value += 1
          # print(f"Process ID: {os.getpid()}, CPU: {os.sched_getaffinity(0)}, Count: {count.value}")
        lock.release()
    print(f"Process ID: {os.getpid()}")


# 총 소요 시간 측정을 위한 시작 시간 기록
start_time = time.time()

# 3개의 프로세스 생성 및 실행
processes = []
for _ in range(num_process):
    process = Process(target=increment, args=(lock,))
    process.start()
    processes.append(process)

# 모든 프로세스의 실행 종료를 대기
for process in processes:
    process.join()

# 결과 출력
print("Count:", count.value)
print("Total Elapsed Time:", time.time() - start_time)
