import os
import time
import threading
import math


count = 0  # 전역 변수 초기화
lock = threading.Lock()  # 스레드 동기화를 위한 Lock 객체
max_count = 3000000
num_thread = 4
for_range = math.ceil(max_count / num_thread)

print('------Multi Thread-----')

def increment(lock):
    global count
    for _ in range(for_range):
      lock.acquire()
      if count < max_count:
        count += 1
      lock.release()
    print(f"Thread ID: {threading.get_ident()}, Process ID: {os.getpid()}")

# 총 소요 시간 측정을 위한 시작 시간 기록
start_time = time.time()

# 5개의 스레드 생성 및 실행
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment, args=(lock,))
    thread.start()
    threads.append(thread)

# 모든 스레드의 실행 종료를 대기
for thread in threads:
    thread.join()

# 결과 출력
print("Count:", count)
print("Range:", for_range)
print("Total Elapsed Time:", time.time() - start_time)
