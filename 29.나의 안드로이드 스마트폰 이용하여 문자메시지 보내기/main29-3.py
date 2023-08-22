import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

excel_file_path = '문자발송리스트.xlsx'
df_from_excel = pd.read_excel(excel_file_path)

name_list = df_from_excel['이름'].tolist()
phone_number_list = df_from_excel['전화번호'].tolist()

print(name_list)
print(phone_number_list)

for i,name in enumerate(name_list):
    send_message = name + "안녕하세요 사랑합니다"
    phone_number = phone_number_list[i].replace("-","")
    send_command = f'am start -a android.intent.action.SENDTO -d sms:"{phone_number}" --es sms_body "{send_message}"'
    print(send_command)