# import os

# def read():
#     with open('test.txt','r+') as fh:
#         lines = fh.readlines()
#         # print(lines)
#         for line in lines:
#             ipOutput = os.system('nslookup' + " " + str(line))
#             # print(ipOutput)
#             ipOutuputString = str(ipOutput)
#             # print(ipOutuputString)
#             write(ipOutuputString)

# def write(res):
#     with open('results.txt','w+') as fh2:
#         fh2.write(res)


# if __name__ == "__main__":
#     read()

import subprocess

with open('test.txt') as f, open('results.txt', 'w') as out:
    for line in map(str.rstrip, f):
        if line:  # skips empty lines
            subprocess.check_call(["nslookup", line],
                                    stdout=out)
            print("Checked")