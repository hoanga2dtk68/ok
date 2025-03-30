import requests
from requests.auth import HTTPBasicAuth
import time

# Thông tin đăng nhập
ip = "3.221.161.121"
url = f"http://{ip}"  # URL gốc (có thể cần thêm endpoint)
username = "MrMilkshake"
password = "D0ntLeav3M3H3r3"

# URL tải file flag (giả định)
file_url = f"http://{ip}/flag.txt"

# Vòng lặp gửi request liên tục
while True:
    try:
        # Gửi request với Basic Auth
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            print("[+] Đăng nhập thành công!")
            print("[+] Phản hồi từ server:")
            print(response.text)

            # Thử tải file flag
            file_response = requests.get(file_url, auth=HTTPBasicAuth(username, password))

            if file_response.status_code == 200:
                flag_content = file_response.text
                print("[+] Flag thu được:")
                print(flag_content)
                break  # Dừng vòng lặp nếu lấy được flag
            else:
                print("[-] Không tìm thấy file flag! Tiếp tục thử...")
        else:
            print(f"[-] Đăng nhập thất bại! Mã lỗi: {response.status_code}")

    except Exception as e:
        print(f"[!] Lỗi xảy ra: {e}")

    time.sleep(2)  # Đợi 2 giây trước khi gửi request tiếp theo (tránh bị chặn)
