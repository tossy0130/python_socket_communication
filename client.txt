import socket                                           # socketライブラリをインポート
import pickle
from tkinter import EXCEPTION
import csv
import pprint
import os

from exceptiongroup import catch


HOST = '127.0.0.1'                                      # ServerのIPアドレスを指定
PORT = 65432                                            # Serverのポート番号を指定
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # socket(IP, TCP)を作成
# s.connect((HOST, PORT))                                 # Serverにアクセス

FIEL_PATH = r'D:\\外山工業\\python 問い合わせ 2023\\file\\'


def Check_Dir(path):
    # ===　path　の場所に ディレクトリ作成
    d_path = path

    try:
        if(os.path.isdir(d_path)):  # フォルダが存在していた場合
            pass
        else:
            os.makedirs(d_path)
    except FileExistsError:
        print('関数名:Check_Dir ::: ディレクトリ作成エラー')


Check_Dir(FIEL_PATH)

# ================================= ソケット通信実行
try:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        data = s.recv(4096)                                  # メッセージを受け取る

        if not data:
            print('データがありません')
            break
        else:
            data = data.decode("utf-8")
            data_split = data.split('*')
        #  with open(FIEL_PARH + '')
            print("============" + "\n")
            print("01:" + data_split[0])
            print("02:" + data_split[1] + "\n")
            print("============")

            file_name1 = data_split[0]
            file_name2 = data_split[0]
            print(file_name1[0:9])
            print(file_name2[11:])
            file_name_02 = file_name2[11:].replace('.', '_')
            file_name_03 = file_name_02.replace(':', '')

            file_name = file_name1[0:9] + '_' + file_name_03

            with open(FIEL_PATH + file_name + '.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([file_name1[0:9] + ',' + file_name2[11:18] + ','
                                 + data_split[1]])
except (ZeroDivisionError, TypeError) as e:
    print(e)
# except EXCEPTION as e:
#    print('=== 例外発生===' + "\n")
#    print('=== エラー内容 ===')
#    print('type:' + str(type(e)))
#    print('args:' + str(e.args))
#    print('message:' + e.message)
#    print('e自身:' + str(e))
