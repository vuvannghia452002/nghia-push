import os
import glob
import subprocess


root = r"C:\Users\vvn20206205\Desktop\github"
workspace = glob.glob(os.path.join(
    root, "**/*.code-workspace"), recursive=True)


for i in workspace:
    # print(f"🚀 {i}")
    os.chdir(os.path.dirname(i))
    subprocess.run(["git", "push"])
