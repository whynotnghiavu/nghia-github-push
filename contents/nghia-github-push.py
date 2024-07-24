import os
import glob
import subprocess
import time


Downloads_Nghia_Git = os.path.expanduser("~/Downloads/Nghia/Git")

workspace = glob.glob(os.path.join(Downloads_Nghia_Git, "**/*.code-workspace"), recursive=True)


def shutdown_computer():
    if os.name == 'nt':
        os.system('shutdown /s /t 15')
    elif os.name == 'posix':
        time.sleep(15)
        os.system('shutdown now')
    else:
        print("Không thể tắt máy tự động trên hệ điều hành này.")


# Lặp qua từng tệp workspace và thực hiện git push
for i in workspace:
    print(f"🚀 \033[32m{i}\033[0m")

    os.chdir(os.path.dirname(i))

    subprocess.run(["git", "status"])

    subprocess.run(["git", "push"])

#! Tắt máy tính sau khi hoàn thành
# shutdown_computer()
