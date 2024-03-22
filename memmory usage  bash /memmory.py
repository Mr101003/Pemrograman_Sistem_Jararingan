import os
import xlsxwriter

instruction = "ps -eo pid,rss,cmd --sort -rss"
cmd = os.popen(instruction)
result = cmd.readlines()
data_clean = result[3:]
task = []
for line in data_clean:
    data = line.split()
#     user = data[0]
    memmory = data[1]
    command = data[2].split("/")
    program = command[-1]
    
    try:
        task.append( (float(memmory),program))
    except:
        pass
    
data_memmory = []
data_task = []

for baris in task[:5]:
    print(f"{baris[1]} => {baris[0]}")
    data_memmory.append(baris[0])
    data_task.append(baris[1])
    
    # print(f"{program} => {memmory}")
# print(data_clean)

