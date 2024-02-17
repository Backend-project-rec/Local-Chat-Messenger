import socket

def main():
    # サーバのホスト名とポート番号
    host = 'localhost'
    port = 12345

    # socket.socket() 新しいソケットオブジェクトの作成
    # AF_INET : IPv4
    # SOCK_STREAM : TCP接続
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True: # 複数のメッセージを送れるようにする
            message = input("Enter your message: ")
            if message == "exit":
                break

            s.sendall(message.encode('utf-8')) # 全て送る

            data = s.recv(1024) # サーバーから最大1024バイトまで受信することにする
            print('Received from server:', data.decode('utf-8'))

        # ループを抜けた後、サーバーに終了を通知するために 'exit' メッセージを送信
        s.sendall('exit'.encode('utf-8'))

# Pythonファイルが直接実行された場合にのみ、main関数が呼び出し
if __name__ == '__main__':
    main()
