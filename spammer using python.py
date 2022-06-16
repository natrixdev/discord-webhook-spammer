import time;import requests;import pyfiglet;import pystyle ;import threading;from pystyle import Colorate, Colors, Add;print(Colorate.Horizontal(Colors.blue_to_red, "github: natrixdev"));banner = pyfiglet.figlet_format("WEBHOOK SPAMMER");print(banner);z = print(Colorate.Horizontal(Colors.green_to_red, "[Console]"));msg = input("Please Insert WebHook Spam Message: ");webhook = input("Please Insert WebHook URL: ")
print(Colorate.Horizontal(Colors.green_to_red, "[Sending Messages]"))
def spam(msg, webhook):
    spam.daemon = True 
    while True:
        
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                
                print(f"Sent message {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()
natrix = 1
while natrix == 1:
    spam(msg, webhook)
