import os
shutdown = input("shutdown your PC? (yes/no):\n")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")