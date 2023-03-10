import sys
import subprocess

tooldir="tools"

def RunCommand(cmd):
	subprocess.call(["python3", "./{}/{}.py".format(tooldir, cmd)])

print("\nShirby Compile Tools [SCOMPY]")
print("------------------------------------------------------------------\n")

if len(sys.argv) < 2:
	print("[version]")
	RunCommand("version")
	exit

for i in range(1, len(sys.argv)):
	cmd = sys.argv[i]	
	print("[{}]".format(cmd))
	RunCommand(cmd)