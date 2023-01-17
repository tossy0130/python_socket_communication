import socket
import csv
import datetime
import schedule
import xlwings as xw
import gc
from time import sleep

tusin = 0

# ソケットを作成する
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 12345番ポートで接続を待つ
    print('========== 開始 =========')
    s.bind(('0.0.0.0', 12345))
    s.listen(5)
    while True:
        # スケジュールを呼び出す
        # schedule.run_pending()
        sleep(1)
        # 接続と送信元IPアドレスを得る
        conn, addr = s.accept()
        with conn:
            # while True:
            # データを受信する
            data = conn.recv(1024)
            if not data:
                print("=== データなし break ===")
                break
            data = data.decode()
            tusin += 1
            # 受信したデータを表示する
            print(str(tusin) + ' Recv:' + data)
            # レスポンスを送信する
            conn.sendall(('Received: ' + data + '\n').encode())
            #　csvファイルに時間とセンサー番号を書き込み
            d_today = datetime.date.today()
            t_now = datetime.datetime.now().time()
            t_now = t_now.replace(microsecond=0)
            dataSplit = data.split("_")
            with open("https://192.168.254.204/tossy_test/" + str(d_today) + "-" + dataSplit[0] + ".csv", 'a', newline="") as f:
                writer = csv.writer(f)
                writer.writerow([str(d_today), str(t_now), dataSplit[1]])

        del data, d_today, t_now, dataSplit, writer
        gc.collect()
