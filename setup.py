import os
import subprocess
a = subprocess.run('ls', capture_output=True).stdout.decode()
if a.splitlines().count('venv/') == 0:
    print("Making venv:\n")
    subprocess.run('python -m venv venv')