import pandas as pd
from ppadb.client import Client
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def adb_connect():
    client = Client(host="127.0.0.1", port=5037) 
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('No devices')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')

    return device, client

device, client = adb_connect()


excel_file_path = '문자발송리스트.xlsx'
df_from_excel = pd.read_excel(excel_file_path)

name_list = df_from_excel['이름'].tolist()
phone_number_list = df_from_excel['전화번호'].tolist()

for i,name in enumerate(name_list):
    send_message = name + "님 사랑합니다 안녕히 계세요"
    phone_number = phone_number_list[i].replace("-","")
    send_command = f'am start -a android.intent.action.SENDTO -d sms:"{phone_number}" --es sms_body "{send_message}"'
    #print(send_command)
    device.shell(send_command)
    time.sleep(1.0)
    xyPosition = "1005 1355"
    device.shell(f'input tap {xyPosition}')  # 전송버튼 클릭
    time.sleep(1.0)