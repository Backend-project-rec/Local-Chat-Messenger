import socket
from faker import Faker # テストデータの生成

def main():
    fake = Faker() # Fakerインスタンス

    host = 'localhost'
    port = 12345

    # クライアント側と同じ
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen() # クライアントからの接続を待ち受ける
        print(f"Server listening on {host}:{port}")

        conn, addr = s.accept() # クライアントからの接続を受け入れ。ソケットオブジェクトとクライアントのアドレスを返す
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data or data.decode('utf-8') == 'exit': # 終了条件はデータがなくなった時か、exitの時。
                    break
                print('Received from client:', data.decode('utf-8'))

                # Fakerを使用して偽の応答を生成
                fake_response = fake.sentence()
                conn.sendall(fake_response.encode('utf-8'))

if __name__ == '__main__':
    main()
