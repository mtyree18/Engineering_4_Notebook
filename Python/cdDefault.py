print("test")
command = "cd.. home/pi/Documents/Engineering_4_Notebook"
import subprocess
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)
