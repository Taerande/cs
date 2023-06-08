import os
import time
from multiprocessing import Process, Value, Lock

count = Value('i', 0)  # 공유 변수 초기화

print('-------Multi Process------')
lockA = Lock()  # A프로세스 동기화를 위한 Lock 객체
lockB = Lock()  # B프로세스 동기화를 위한 Lock 객체

def increment(lockA, lockB):
    global count
    lockB.acquire()
    print(f"Process ID: {os.getpid()}, Enter Increment")
    for _ in range(500):
      lockA.acquire()
      count.value += 1
      lockA.release()
    print(f"Process ID: {os.getpid()}, Leave Increment")
    lockB.release()


def decrement(lockA, lockB):
    global count
    lockA.acquire()
    print(f"Process ID: {os.getpid()}, Enter Decrement")
    for _ in range(500):
      lockB.acquire()
      count.value -= 1
      lockB.release()
    print(f"Process ID: {os.getpid()}, Leave Decrement")
    lockA.release()

# 총 소요 시간 측정을 위한 시작 시간 기록
start_time = time.time()

# A, B 프로세스 생성 및 각각의 Mutex Lock획득
# increment, decrement 의 Mutex Lock을 교차로 획득하게 하여 Dead Lock 발생
processA = Process(target=increment, args=(lockA,lockB))
processB = Process(target=decrement, args=(lockA,lockB))
processA.start()
processB.start()

# A, B 프로세스 종료시 까지 대기
processA.join()
processB.join()

# 결과 출력
print("Count:", count.value)
print("Total Elapsed Time:", time.time() - start_time)
