import os
import glob
import subprocess


root = r"C:\Users\vvn20206205\Desktop"
Desktop = os.path.expanduser("~/Desktop")
root = os.path.expanduser("~/Desktop")

workspace = glob.glob(os.path.join(root, "**/*.code-workspace"), recursive=True)


def shutdown_computer():
    if os.name == 'nt':
        os.system('shutdown /s /t 5')
    # elif os.name == 'posix':
    #     os.system('sudo shutdown now')
    else:
        print("Không thể tắt máy tự động trên hệ điều hành này.")


for i in workspace:
    print(f"🚀 {i}")
    os.chdir(os.path.dirname(i))
    subprocess.run(["git", "push"])


# shutdown_computer()


# Thêm màu phân biệt ko có????
# đa luồng  ?? 5 phút
