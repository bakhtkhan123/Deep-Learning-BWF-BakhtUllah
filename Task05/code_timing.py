#timing  the code
import time
start_time=time.time()
for i in range(1000):
    print(i)
end_time=time.time()
Execution_time=end_time-start_time
print("Code Execution time ",Execution_time)

# to get CPU execution time
st_time=time.process_time()
for i in range(1000):
    print(i)
ed_time=time.process_time()
exec_time=ed_time-st_time
print("CPU Execution time ",exec_time)

