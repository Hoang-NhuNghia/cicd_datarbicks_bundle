import subprocess
import os
import sys

# Lấy đường dẫn tuyệt đối của file script
# Giả sử script nằm cùng thư mục scripts/ với file python này
script_path = os.path.join(os.path.dirname(__file__), "lake_utils_install.sh")

try:
    # Chạy script bash
    subprocess.check_call(["bash", script_path])
except subprocess.CalledProcessError as e:
    print(f"Error running script: {e}")
    sys.exit(1)
