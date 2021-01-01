import requests
import json
import os, sys

LINE_TOKEN = os.environ["LINE_TOKEN"]


def get_xem_price() -> float:
    """XEMの現在価格を取得して返します"""
    url = "https://api.zaif.jp/api/1/last_price/xem_jpy"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"return status code is {response.status_code}")
    result = json.loads(response.text)["last_price"]
    return result


def get_status() -> dict:
    """連携状態を確認し、結果を返します"""
    url = "https://notify-api.line.me/api/status"
    # ヘッダーにLINEのトークンをセットします（超重要）
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"return status code is {response.status_code}")
    return json.loads(response.text)


def send_line_message(message):
    """ LINEへメッセージを送信する関数 """
    api_url = "https://notify-api.line.me/api/notify"
    # ヘッダーにLINEのトークンをセットします（超重要）
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": f" {message}"}
    response = requests.post(api_url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(f"return status code is {response.status_code}")


def main():
    try:
        res = get_status()
        print(f"ステータス: {res}")

        price = get_xem_price()
        message = f"XEM現在価格: {price} JPY"
        print(message)

        # LINEに現在価格の情報を含めたメッセージを送信します
        send_line_message(f"{message}")
    except:
        print(sys.exc_info())


if __name__ == "__main__":
    main()
