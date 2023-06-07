import os
import time
import threading
from math import ceil

count = 0  # 전역 변수 초기화
max_count = 3000000
num_process = 1
for_range = ceil(max_count/num_process)

print('------Single Thread-----')

def increment():
    global count
    for _ in range(for_range):
      if count < max_count:
        count += 1
    print(f"Thread ID: {threading.get_ident()}, Process ID: {os.getpid()}")

# 총 소요 시간 측정을 위한 시작 시간 기록
start_time = time.time()

# 5개의 스레드 생성 및 실행
threads = []
for _ in range(num_process):
    thread = threading.Thread(target=increment)
    thread.start()
    threads.append(thread)

# 모든 스레드의 실행 종료를 대기
for thread in threads:
    thread.join()

# 결과 출력
print("Count:", count)
print("Total Elapsed Time:", time.time() - start_time)
