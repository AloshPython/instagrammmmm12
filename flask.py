import requests
from flask import *

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
  return 'business'

@app.route('/business/',methods=['GET'])

def check():
        sessionid = str(request.args.get('sessionid'))
        print(sessionid)
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
).text);
        rlo={'ok': 'true','status':id};
        #return rlo

        if '"status":"ok"' in id:
            #time.sleep(59)
                    
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
            #print(k.text)
            try:
                user=k.json()["user"]["username"]
                
            except:
                rl0={'ok': 'true','status':'Error Account'}
                return rl0
            if '"status":"ok"' in k.text:
                
               # {'ok': 'true','status':
                rl1={'ok': 'true','status':f"Done accont :{user} | response : {k} "}
                return rl1
                          
            else:
                rl2={'ok': 'true','status':'Error Id'}
                return rl2
                
        else:
            rl3={'ok': 'true','status':'Error business'}
            return rl3


if __name__ == '__main__':
  app.run()