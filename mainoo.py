#whitepro
import os
try :
    import pyfiglet
    import telethon
    import requests
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install telethon')
    os.system('pip3 install requests')
import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 

api_id = "26000833"
api_hash = "84c1346a84e94fed4952a81d524d8de6"
client = TelegramClient('session', api_id, api_hash)
client.start()
ch = 'https://t.me/h_s_32',"https://t.me/+jJPr8Scd-XtkYWUy",'https://t.me/qqu27','https://t.me/zzab1', 'https://t.me/+uW9Or-KdtvI2MDZi' ,'https://t.me/e_e_g_e','https://t.me/+_e8Ib9XB03w0ZTZi','https://t.me/+VnsmOSXeOMA4N2Mx','https://t.me/ooa60','https://t.me/+yFWxxT8hBIk4ZTlh','https://t.me/+77gNtoXLYiNkNzkx','https://t.me/+Mkd6z-nkqDQ1NjE0','https://t.me/+Wk29o3KsRwE2NzU8','https://t.me/+tmoDaaXv6DQ5YjZk','https://t.me/+Kkgdt9YHLWliZjc0'
while True :
    ch1 = "https://t.me/qqu27"
    randomm=random.choice(ch)
    print(randomm)
    chh="""للبيع حسابات انستا 
    ترويج مايطلب فيس
    و حسابات وهميه لجماعه رشق 
    لتواصل :
    @aaalaaa ; @horo1bot
    
    اسعار كسر ليريد خاص"""
    client.send_message(randomm ,chh)
    u=time.sleep(random.randint(20,20))
    #print(u)
        
        #whitepro
