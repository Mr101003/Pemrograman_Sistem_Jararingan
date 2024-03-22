import os
instruction = "ps aux"
cmd = os.popen(instruction)
result = cmd.readlines()
data_clean = result[3:]
for line in data_clean:
    data = line.split()
    user = data[0]
    memmory = data[2]
    command = data[10].split("/")
    program = command[-1]
    print(f"{program} => {memmory}")