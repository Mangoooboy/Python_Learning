import subprocess

result = subprocess.run(
    ["wmic", "logicaldisk", "get", "size,freespace,caption"],
    capture_output=True,
    text=True,
    shell=True
)

print(result.stdout)