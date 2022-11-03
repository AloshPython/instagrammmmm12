import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=["start"])
def boten(message):
            email="hdiebei@gmail.com"
            user="klneoe"
            name="Alosh TeleGram: https://t.me/aaalaaa"    
            pess="ali0968241"
            ############
            headers={}
            USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; ) Gecko/20100101 Firefox/65.0"
            BASE_URL = "https://www.instagram.com/"                    
            session = requests.Session()
            #proxy=session.get("https://gimmeproxy.com/api/getProxy").json()['curl']            
            #print("PROXY : "+proxy)
#            session.proxies.update({
#            'http': proxy,
#            'https': proxy,
#            })  
     
            session.headers = {'user-agent': USER_AGENT, 'Referer': BASE_URL,'accept':'*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9',
            'content-length':'372',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':'ig_did=6B80CE00-7703-4B67-8FFB-64237D1A4526; ig_nrcb=1; mid=Y1atWAALAAFJe7yhqQTm_4YG73ll; rur="NCG\05455895443439\0541698161196:01f780cf7ed77bfa0872d6b2db93ad6dfbd907a9ceb9e6c09c0e574b3dbccb313e46eb03"; csrftoken=16KXai5ARwzXILip43vedEnmFFJFF3YP; datr=u6JXY8YleJCnGIwkBi_Xkt6J',
            'origin':'https://www.instagram.com',
            'referer':'https://www.instagram.com/sem/campaign/emailsignup/?campaign_id=13530334509&extra_1=s|c|547348909654|e|instagram%20%27|&placement=&creative=547348909654&keyword=instagram%20%27&partner_id=googlesem&extra_2=campaignid%3D13530334509%26adgroupid%3D126262421974%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-1321618851291%26loc_physical_ms%3D9059770%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIpbTu4Yf7-gIVDr3ICh1RoArREAAYASAAEgIZb_D_BwE','sec-ch-prefers-color-scheme':'light',
            'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width':'701',
            'x-asbd-id':'198387',
            'x-csrftoken':'16KXai5ARwzXILip43vedEnmFFJFF3YP',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'x-instagram-ajax':'529bd295327c',
            'x-requested-with':'XMLHttpRequest',
            }
            url_attempt="https://www.instagram.com/accounts/web_create_ajax/attempt/"            
            url_check_age_eligibility= "https://www.instagram.com/web/consent/check_age_eligibility/"            
            url_send_verify_email="https://i.instagram.com/api/v1/accounts/send_verify_email/"
            url_check_confirmation_code='https://i.instagram.com/api/v1/accounts/check_confirmation_code/'
            url_web_create_ajax='https://www.instagram.com/accounts/web_create_ajax/'   
                  
            req_attempt=session.post(
            url=url_attempt,
            data={
             'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:'+pess,
        'email':email,
            'username':user,
            'first_name':name,
            'client_id':'Y1atWAALAAFJe7yhqQTm_4YG73ll',
            'seamless_login_enabled':'1',
            'opt_into_one_tap':'false',
            },)
            #print(req_attempt.text)
            bot.send_message(message.chat.id,f"req ydhe{req_attempt}")
            sessionid= '56173168935%3A3e78HiFRkGHe1E%3A23%3AAYf7nX1V_jhuVPZxYfIXXNU-WpjqriY57n8DJd6GUQ'
            bot.send_message(message.chat.id,f"req id ")
            id=(
requests.get(
url='https://i.instagram.com/api/v1/business/account/get_suggested_categories/?withCredentials=true',
headers={
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9',
'cookie':'ig_did=93F3D391-E946-4CA9-BC28-9872CC88F8D8; ig_nrcb=1; mid=Y0L_qwALAAHR2BDqxOmhbdtme3-r; csrftoken=poCr2cta8DPR1LMq0hinbpCACUc56FpG; ds_user_id=55779596318; datr=BQFDY6nz56dq8hLbNslV5uFJ; sessionid='+sessionid+'; rur="NCG\05455779596318\0541696923586:01f70039228a05d9bf6c445426623f646e15b44add77eb69616f4bb03f1bf16793a2f37b"',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'x-asbd-id':'198387',
'x-csrftoken':'poCr2cta8DPR1LMq0hinbpCACUc56FpG',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR2SlIOJpZWuy4vZq8Nx4kskVlUqBIl1-4HJqFNot7mCf9Pz',
'x-instagram-ajax':'c9e803a8d542',



},
data={
'withCredentials':'true'
},
).text)		
            bot.send_message(message.chat.id,f"req id {id}")
            k=(
requests.post(
url='https://i.instagram.com/api/v1/business/account/convert_account/',
headers={'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9',
'content-length':'217',
'content-type':'application/x-www-form-urlencoded',
'cookie':'ig_did=93F3D391-E946-4CA9-BC28-9872CC88F8D8; ig_nrcb=1; mid=Y0L_qwALAAHR2BDqxOmhbdtme3-r; csrftoken=poCr2cta8DPR1LMq0hinbpCACUc56FpG; ds_user_id=55779596318; datr=BQFDY6nz56dq8hLbNslV5uFJ; sessionid='+sessionid+'; rur="NCG\05455779596318\0541696923596:01f7893d4c4f9d72e39501bff8e7a0bc901dd3a4e198a2187556a82552457074a7c9bbfd"',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'x-asbd-id':'198387',
'x-csrftoken':'poCr2cta8DPR1LMq0hinbpCACUc56FpG',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR2SlIOJpZWuy4vZq8Nx4kskVlUqBIl1-4HJqFNot7mCf9Pz',
'x-instagram-ajax':'c9e803a8d542',},
data={'category_id':'2214',
'create_business_id':'true',
'entry_point':'ig_web_settings',
'fb_user_id':'',
'fb_user_nonce':'',
'page_id':'',
'preferred_business_id':'',
'should_bypass_contact_check':'true',
'should_show_category':'0',
'set_public':'true',
'to_account_type':'3',

},
))
            bot.send_message(message.chat.id,f"req k {k}")
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://kkwosg.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
