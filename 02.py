import socket
import xml.etree.ElementTree as ET

PORT = 60001
RES_XML = 'xml/res.xml'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # ホストに割当たっている IP を指定する
    host = socket.gethostname()
    s.bind((socket.gethostbyname(host), PORT))

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(1)

    while True:
        try:
            client, addr = s.accept()

            # バッファサイズ 100 byte
            data = client.recv(100)
            print(f'data: {data}, addr: {addr}')

            # XML から抽出したデータでレスポンスのバイナリを作成
            b = bytearray()
            root = ET.parse(RES_XML).getroot()
            res = root.find('res').text.encode('utf-8')
            b.extend(res)

            client.sendall(b)

        except KeyboardInterrupt:
            print('Interrupted.')
            break

        except socket.error:
            print('Has error occurred.')
            pass
