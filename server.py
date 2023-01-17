import socket                                          # socketライブラリをインポート
import datetime
import pickle


class Date_To():
    # ============ 日時・時刻　クラス　============
    # 予約時間　格納用
    def __init__(self):
        self.time_num = [
            ['1', '9:00'],
            ['2', '10:00'],
            ['3', '11:00'],
            ['4', '12:00'],
            ['5', '13:00'],
            ['6', '14:00'],
            ['7', '15:00']
        ]

        self.dt_now = ""

    # === 当日取得 ::: 2022-11-04 14:26:56.878021
    def Now_date(self):
        self.dt_now = datetime.datetime.now()
        return self.dt_now

    # === 日付 ::: フォーマット 22-11-04
    def Date_cut(self, t_date):
        now_date = t_date
        n_now_date = now_date.strftime("%y-%m-%d")
        return n_now_date

    # === index に応じた time_num の時間を出力
    def Yoyaku_Time_idx(self, idx, idx_02):
        return self.time_num[idx][idx_02]

    def Date_Add(self, num):
        date_add = self.dt_now + datetime.timedelta(days=num)
        return date_add
        # Date_To ****** END ********


# 日付け　オブジェクト
Date_Obj = Date_To()
now_date = Date_Obj.Now_date()  # 日付け

# data = {1: "Apple", 2: "Orange"}

OUT_NUM = 1
# =========================== ソケット 部分
HOST = '127.0.0.1'                                     # ServerのIPアドレスを指定
PORT = 65432                                           # Serverのポート番号を指定
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket(IP, TCP)を作成
# socketに指定したIPアドレスとポート番号を適用
s.bind((HOST, PORT))
s.listen(100)                                             # socketをlisten状態にする
# conn, addr = s.accept()                                # socket通信を受け入れ

LOOP_FLG = True

if LOOP_FLG == True:
    while True:
        conn, addr = s.accept()

        # msg = pickle.dumps(data)  # 辞書データ
        # conn.send(msg)

        conn.sendall((str(now_date) + '*' + str(OUT_NUM)).encode()
                     )                 # メッセージ(バイト列)を送信
        OUT_NUM += 1

        if (OUT_NUM >= 5000):
            LOOP_FLG = False

        else:
            pass

else:
    while True:
        conn, addr = s.accept()

        # msg = pickle.dumps(data)  # 辞書データ
        # conn.send(msg)

        conn.sendall((str(now_date) + ' ' + str(OUT_NUM)).encode()
                     )                 # メッセージ(バイト列)を送信
        OUT_NUM += 1

        if (OUT_NUM >= 10000):
            conn.sendall("kk")
            break
            s.close()
        else:
            pass
            s.close()

s.close()
