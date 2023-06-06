import os
import time
from multiprocessing import Process, Value, Lock

count = Value('i', 0)  # 공유 변수 초기화

print('-------Multi Process------')

def increment(lock):
    lock.acquire()
    global count
    while count < 3000000:
        count.value += 1
    lock.release()
    print(f"Process ID: {os.getpid()}")

# 총 소요 시간 측정을 위한 시작 시간 기록
start_time = time.time()

# 3개의 프로세스 생성 및 실행
processes = []
for _ in range(3):
    lock = Lock()  # 프로세스 동기화를 위한 Lock 객체
    process = Process(target=increment, args=(lock,))
    process.start()
    processes.append(process)

# 모든 프로세스의 실행 종료를 대기
for process in processes:
    process.join()

# 결과 출력
print("Count:", count.value)
print("Total Elapsed Time:", time.time() - start_time)
