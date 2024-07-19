import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup

Token = "6685119417:AAGGYkc1ztEbtILrx3VmY4i8_HgzwhqdRAI"
bot = telebot.TeleBot(Token)

addAccount = types.InlineKeyboardButton(text ="( Add Account )",callback_data = "account")
Follow  = types.InlineKeyboardButton(text ="( Follow ) ",callback_data = "follow")
Like = types.InlineKeyboardButton(text ="( Send Like )",callback_data = "like")
Story = types.InlineKeyboardButton(text ="( Show Story )",callback_data = "story")
addSessionid = types.InlineKeyboardButton(text ="( Add Sessionid )",callback_data = "add_ses")
CheckSes = types.InlineKeyboardButton(text ="( Check Sessionids )",callback_data = "check_ses")						
Comment = types.InlineKeyboardButton(text ="( Comment )",callback_data = "comment")
editAccount  = types.InlineKeyboardButton(text ="( Edit Account ) ",callback_data = "edit")
urls = types.InlineKeyboardButton(text ="Programmer",url="t.me/zxexai")
Addbut = types.InlineKeyboardMarkup(row_width=4)
Addbut.add(addAccount)
Addbut.add(Comment,Like)
Addbut.add(Story,Follow)
Addbut.add(CheckSes,addSessionid)
Addbut.add(editAccount)
Addbut.add(urls)	

@bot.message_handler(commands=["start"])
def start(message):
    phot = "https://socialtradia.com/wp-content/uploads/2020/10/blue-check-on-instagram.jpg"
    get_nams = f"t.me/{message.from_user.username}"
    tag = f"[{message.from_user.first_name}]({get_nams})"
    text = f"*Hi* {tag}* To Bot Auto Activity Your Account\nSelect From the Buttons To Work !*"
     
    sent_message = bot.send_message(
    message.chat.id,
     text, parse_mode="Markdown",
      disable_web_page_preview=True,
       reply_markup=Addbut)
   
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "like":
        Function3(call.message)
    elif call.data == "comment":       
        Function2(call.message)
    elif call.data == "follow":
        Function1(call.message)
    elif call.data == "story":
        bot.answer_callback_query(call.id, "This button has not been added ")       
    elif call.data == "account":
        add_account(call.message)
    elif call.data == "check_ses":
        check_sessionid(call.message)
    elif call.data == "add_ses":
        Function4(call.message)
    elif call.data == "edit":
        Function5(call.message)
    elif call.data == "name":
        Function6(call.message)
    
    elif call.data == "back":
         text = "*Hi* Again *To Bot Auto Activity Your Account\nSelect From the Buttons To Work !*"
         bot.edit_message_text(
    text,
    disable_web_page_preview=True,
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    parse_mode="Markdown",
    reply_markup=Addbut
)
         bot.clear_step_handler_by_chat_id(call.message.chat.id)


def Function1(message):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
    markup.add(back_button)
    bot.edit_message_text("Send Username :", chat_id=message.chat.id, message_id=message.message_id,reply_markup=markup)
    bot.register_next_step_handler(message, get_username_for_follow)


def Function2(message):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Back", callback_data="back")
    markup.add(back_button)
    bot.edit_message_text("Send Url And Comment\nExample :\nhttps://www.instagram.com\nHi i send Comment ",disable_web_page_preview=True, chat_id=message.chat.id, message_id=message.message_id,reply_markup=markup)
    bot.register_next_step_handler(message, send_comment)


def Function3(message):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Back", callback_data="back")
    markup.add(back_button)
    bot.edit_message_text("Send Url :",disable_web_page_preview=True, chat_id=message.chat.id, message_id=message.message_id,reply_markup=markup)
    bot.register_next_step_handler(message, send_like)

def Function4(message):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Back", callback_data="back")
    markup.add(back_button)
    bot.edit_message_text("Send Sessionid :",disable_web_page_preview=True, chat_id=message.chat.id, message_id=message.message_id,reply_markup=markup)
    bot.register_next_step_handler(message, add_sessionid)

def Function5(message):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")  
    Bio = types.InlineKeyboardButton(text="( Change Bio )", callback_data="bio")    
    Name = types.InlineKeyboardButton(text="( Change Name )", callback_data="name")    
    Username = types.InlineKeyboardButton(text="( Change Usernames )", callback_data="back")
    markup.add(Name)
    markup.add(Username)
    markup.add(Bio)    
    markup.add(back_button)
    bot.edit_message_text("Choose From the Buttons What You Want :",disable_web_page_preview=True, chat_id=message.chat.id, message_id=message.message_id,reply_markup=markup)
    
def Function6(message):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
    markup.add(back_button)
    bot.edit_message_text("Send New Name :",disable_web_page_preview=True, chat_id=message.chat.id, message_id=message.message_id,reply_markup=markup)
    bot.register_next_step_handler(message, cahnge_name)


def cahnge_name(message):
    name = message.text
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
    markup.add(back_button)
    with open("sessionid.txt", 'r') as file:
            for sessionid in file:
                cookies = {
    'sessionid': sessionid.strip(),
}

                headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.instagram.com/accounts/edit/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
    'x-ig-app-id': '936619743392459',
    'x-requested-with': 'XMLHttpRequest',
}
                try:
                    response = requests.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies=cookies, headers=headers).json()
                    oldname = response['form_data']['first_name']
                    email = response['form_data']['email']
                    username = response['form_data']['username']
                    chaining_enabled = response['form_data']['chaining_enabled']
                    external_url = response['form_data']['external_url']
                    phone_number = response['form_data']['phone_number']
                    biography = response['form_data']['biography']     
                    bot.reply_to(message,f"Old Name : {oldname} ")
                    url = "https://www.instagram.com/api/v1/web/accounts/edit/"
                    payload = {
    'biography': biography ,
    'chaining_enabled': chaining_enabled,
    'email': email,
    'external_url': external_url,
    'first_name': oldname,
    'phone_number': phone_number,
    'username': username
}

                    headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  'x-ig-www-claim': "hmac.AR0qlKSzsHmIcZuWB6aUi7H-IMKz1DeTVtfEQeMZ-yMX5FS9",
  'sec-ch-ua-platform-version': "\"12.0.0\"",
  'x-requested-with': "XMLHttpRequest",
  'sec-ch-ua-full-version-list': "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.122\", \"Google Chrome\";v=\"126.0.6478.122\"",
  'sec-ch-prefers-color-scheme': "dark",
  'x-csrftoken': "EOiLbpIOFClXHpaV9U3UUrcxycjGwlAJ",
  'sec-ch-ua-platform': "\"Android\"",
  'x-ig-app-id': "1217981644879628",
  'sec-ch-ua-model': "\"SO-51A\"",
  'sec-ch-ua-mobile': "?1",
  'x-instagram-ajax': "1014777282",
  'x-asbd-id': "129477",
  'origin': "https://www.instagram.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.instagram.com/accounts/edit/",
  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
  'Cookie': f"mid=Zk53LwAEAAHkGLfrbNVpJgdYnGXH; ig_did=1B11344A-A9B9-4A2A-AFCF-77AB484FB822; ig_nrcb=1; datr=LXdOZqsyg3XFNCiMUsQHCbbq; ps_n=1; ps_l=1; ig_lang=en; oo=v1; ds_user_id=63489588072; fbm_124024574287414=base_domain=.instagram.com; dpr=2.625; shbid=\"9691\\05463489588072\\0541751922854:01f7b5727e74baa9dcc5314136d049d4353190da7225e7005234a6ed8eb1da03774b76ba\"; shbts=\"1720386854\\05463489588072\\0541751922854:01f7503f14f25930b4afbe5064ae6669116cc605f95c92acb0123291421f59f238958a4d\"; csrftoken=EOiLbpIOFClXHpaV9U3UUrcxycjGwlAJ; ig_direct_region_hint=\"CLN\\05463489588072\\0541752015472:01f75175df540614b3cdb4840e2fb526805bddf4c284b61ff02bffefd7a8c20b6f89b530\"; wd=418x842; sessionid={sessionid.strip()}; fbsr_124024574287414=0AvYet7m-DHBDleiF0_XibeScqlC9uKDOMTOB1eOqT4.eyJ1c2VyX2lkIjoiMTAwMDg4ODY4MjkzNzcyIiwiY29kZSI6IkFRRE1fcWZGeFVJWGJfTXllVk5XSFlNMGQ0NllJSG9WZVJfbGlCQ19PNlNZMlNadG1xZm5DN3hKdm1ZSG1heHV0UnpYZWc0RjlKZmlkUzlSTXVMM1BJT29sNWJOeWFmb0VIcWExZkhRUXd2dDBGRmEzRFd0U0hISFEzZmZ5NVZXSmFsanQ2MFl0QVlXR3dsU0JQUVEtelFVdzFNZmRUMzlERVg5eXNCU2RSTmN6cS1kc2VBVC1DR0lRWWRuVXN4SmFXX3NaVW9GQXBDaGNsa01tcmh4S3NLSHlJeHptUTBFRU1nYnk0UVd6UDVsYXdjMnFmRDlWZElyWWlhWWRPTFVMakNZMFZUUklmb1dTdGdtbTJjTlJTa2QxQ0RNY3B2RlFPRUM4YTZLZWVkVl9XOXIxZXRlTlFWWVlBb1IwaXMxbmMza3JRX1NhN3hfNkJvNVRDZ0kxMXhFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzhQMVVwUzA2cVJGVmVQYWJ2WkNUU1pCREVMMko2VzJaQW9aQ3RBZnhDd1FKZzhnUmlQb2tlbWdGZ2REeFJjOEJZU1R2T0FheUUwSnhhckMyYkhOa1kzN1VvbVlMODcxWkNmdGFCaFpBTVh1QWl4VVdoSjJBSEpyNnJMS3B4N3htdUhGT2d0NFVJU0pkU0YxRnEwRUFKS1pDWkI1cGpWbnFZYWNMMVZaQVZMS203dTNEb3MwR2swRmh6T1laRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNzIwNjE1NTA5fQ; rur=\"RVA\\05463489588072\\0541752151512:01f75b075a05f66cbf3b9c21bf74a1fb488853ab1de5d464c5a24fba89787b3e24f2a173\""
}

                    try:
                        response = requests.post(url, data=payload, headers=headers)
                        if response.status_code == 200:                       
                            bot.send_message(message.chat.id,text=f"Done Change Name 🟢 : {name} ",reply_markup=markup)
                        else :
                            bot.send_message(message.chat.id,text=f"Erorr Change Name 🟡 : {name} ",reply_markup=markup)
                    except:
                            bot.reply_to(message,"Erorr Requests 🔴",reply_markup=markup)    
                except Exception as e:
                         bot.reply_to(message,f"Erorr  🔴 : {e}",reply_markup=markup)    
                                                

def add_sessionid(message):
    sessionid = message.text
    with open("sessionid.txt", 'w') as file:
                file.write(sessionid + "\n")
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
    markup.add(back_button)
    bot.reply_to(message,"Done Save Sessionid 🟢",reply_markup=markup)
        
def check_sessionid(message):
    bot.send_chat_action(message.chat.id, 'typing')
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
    markup.add(back_button)
    try:
        with open("sessionid.txt", 'r') as file:
            bb=0
            for sessionid in file:
                bb+=1
                cookies = {
    'sessionid': sessionid.strip(),
}
                headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.instagram.com/accounts/edit/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
    'x-ig-app-id': '936619743392459',
    'x-requested-with': 'XMLHttpRequest',
}
                try:
                    response = requests.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies=cookies, headers=headers).json()
                    if response['status'] == 'ok':
                        bot.send_message(message.chat.id,text=f"Work Sessionid 🟢 : `{sessionid.strip()}`",parse_mode="Markdown")
                    else:
                        bot.send_message(message.chat.id,text=f"Dont Work Sessionid 🔴 : {sessionid.strip()}")
                except Exception as e:
                    bot.send_message(message.chat.id,text=f"Erorr 🔴 : {e}",reply_markup=markup)                       
            bot.reply_to(message,text=f"Complite Check Sessionid : {bb} Sessionid ",reply_markup=markup)                              
    except:
        bot.send_message(message.chat.id,text="File Not Fount 🟡",reply_markup=markup)
    
  
def send_like(message):
    urls = message.text
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
    markup.add(back_button)
    try:
        response = requests.get(urls)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for res in soup.find_all('meta'):
                if 'content' in res.attrs and res.attrs.get('property') == 'al:ios:url':
                    text = res.attrs['content']
                    id_post = text.split('id=')[1]                
                    with open("sessionid.txt", 'r') as file:
                        bb=0
                        for sessionid in file:
                            bb+=1
                            url = f"https://www.instagram.com/api/v1/web/likes/{id_post}/like/"
                            headers = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  'x-ig-www-claim': "hmac.AR3wjErOQLmEqvPERp0gpZx2T1uPwxPfPjxR9bkOcmFRk8Is",
  'sec-ch-ua-platform-version': "\"\"",
  'x-requested-with': "XMLHttpRequest",
  'sec-ch-ua-full-version-list': "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.122\", \"Google Chrome\";v=\"126.0.6478.122\"",
  'sec-ch-prefers-color-scheme': "dark",
  'x-csrftoken': "HC2JHcMAJXUR1jpvmlNlsTiRAzBnXDOA",
  'sec-ch-ua-platform': "\"Linux\"",
  'x-ig-app-id': "936619743392459",
  'sec-ch-ua-model': "\"\"",
  'sec-ch-ua-mobile': "?0",
  'x-instagram-ajax': "1014723251",
  'x-asbd-id': "129477",
  'origin': "https://www.instagram.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.instagram.com/p/C2fCdscsn5-/",
  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
  'Cookie': f"mid=Zk53LwAEAAHkGLfrbNVpJgdYnGXH; ig_did=1B11344A-A9B9-4A2A-AFCF-77AB484FB822; ig_nrcb=1; datr=LXdOZqsyg3XFNCiMUsQHCbbq; ps_n=1; ps_l=1; ig_lang=en; oo=v1; ds_user_id=63489588072; fbm_124024574287414=base_domain=.instagram.com; dpr=2.625; csrftoken=HC2JHcMAJXUR1jpvmlNlsTiRAzBnXDOA; shbid=\"9691\\05463489588072\\0541751922854:01f7b5727e74baa9dcc5314136d049d4353190da7225e7005234a6ed8eb1da03774b76ba\"; shbts=\"1720386854\\05463489588072\\0541751922854:01f7503f14f25930b4afbe5064ae6669116cc605f95c92acb0123291421f59f238958a4d\"; wd=980x1973; sessionid={sessionid.strip()}; fbsr_124024574287414=2otKBC3COaQu_1tTTv9deHdiFL_EF-xg_TSTeWf7K7s.eyJ1c2VyX2lkIjoiMTAwMDg4ODY4MjkzNzcyIiwiY29kZSI6IkFRQXVHczFvbTMyMHpkUjNVa21PYjRGd0NBVG5PRnU3NnJtWHowZWs2dlc4WUNhMklmbGppRHhZOEdfQ1lPR2o1QWZCb2JObEtPQUp1Rm5pSVFiWHZqRUQ4V0oweEJWUndIdU84eE1rOUpXQXFIMTJ3Vk1vZlpxQnlEVXNsbEpRd1hxTkNHajljNFkxSDFsM0hKRURhVk1aQk5pSWprUEF3Z3BiQXFGeWVmYzFnTGtBOFlyNUNNNzRpZUJUZFdld19mdndwbGZpcnVwNjAyQUF2am43aFBwaWp0UnVwTHVFMXFTQUVQMGVOSVZuRDRvdDJ5R19WS09RU3FXZU5jZ3hKTUhUVXlkSzE5NUtXcHRiamphOTEyZXFUejZWNWdpS3BtWGY4SUgwOWo2RHpwbUJHQ0ZNZHU5LTl3dUFRMEJsTHhLNmNfanhETFZ1V1JwRzdwZlN3NHQ4Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzFUU2daQVNTQ204UTRlZXhReWh6Q0o5dGxxTFRiUGZVb2hVWUFmVlhmVFpDMFNOMzFBWkM0eHROS3RJSURPZE4xR2dOSWFKSjZPMTc2QXZOS0lueUNvamF4WkI0dkNEN0ZhVnFsdXNWelpBWkIzZWh0RlpCRHJ4eTBGWkNaQ1JKVGkwVzRsV1BFZk5hVG5CMGh4aFR1dUNmb2JBempQZ3I4Nm9TNTRaQjFmckh1TDVtdXR4MVNaQ2N5RlFrUVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MjA0NjU4MzB9; rur=\"RVA\\05463489588072\\0541752001869:01f798b9a7cc8a0efc82b2105b807a32b46083cd57ceeffc3e59125587018574565b6e88\""
}

                            try:
                                response = requests.post(url, headers=headers)
                                if response.status_code == 200:
                                    bot.reply_to(message,f"Done Send Like 🟢")
                                else:
                                    bot.reply_to(message, "Erorr Send Like 🔴")
                            except :
                                bot.reply_to(message, "Erorr Send Like 🔴")
                        bot.reply_to(message,text=f"Sending Has Been Completed ! : {bb} Like ✅ ",reply_markup=markup)                                
    except:
        bot.reply_to(message, "Erorr Send Like 🔴")

def send_comment(message):
    urls , comment = message.text.split('\n')
    try:
        response = requests.get(urls)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for res in soup.find_all('meta'):
                if 'content' in res.attrs and res.attrs.get('property') == 'al:ios:url':
                    text = res.attrs['content']
                    media_id = text.split('id=')[1]                
                    with open("sessionid.txt", 'r') as file:
                        bb=0
                        for sessionid in file:
                            bb+=1
                            url = "https://www.instagram.com/graphql/query"
                            payload = {
        "av": "17841463482176198",
        "__d": "www",
        "__user": "0",
        "__a": "1",
        "__req": "1w",
        "__hs": "19912.HYP:instagram_web_pkg.2.1..0.1",
        "dpr": "3",
        "__ccg": "UNKNOWN",
        "__rev": "1014728296",
        "__s": "64i4if:3rf8mt:t9i9jg",
        "__hsi": "7389405149159204062",
        "__dyn": "7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awpUO0n24oaEnxO1ywOwv89k2C1Fwc60D82IzXwae4UaEW2G0AEcobEaU2eUlwhEe87q7U1bobpEbUGdG1QwVwDwHg2ZwrUdUbGwmk0zU8oC1Iwqo5q3e3zhA6bwg8rAwHxW6Uf9EObzUaU",
        "__csr": "gX5MX3aewm9n9R_aMF9fYIARmyfAHnX_OuCZ8D9QjQ_Vt4QnuGFfKXKJF4FAQqALXBUyUzzTbZ2e8KuZrWXwAAJahoxuayfiyZVoGmicF7AgymV8y7uq9F28q-K6ahFER2ucBAyVXKK8xO00lP2bV8eU4imz0Nwb-6A3tuow0jTw1N92kmtr6xG0Fo2LDxahBCgeYE4x8g0aGw960Je0kuzo2dg1a80QG581mpYE38800zQ8",
        "__comet_req": "7",
        "fb_dtsg": "NAcOlXQPAir16fPLttk6y3keQb6040Zey_6a0IOmPAF5vvMZUcIwTPg:17843708194158284:1720479330",
        "jazoest": "26186",
        "lsd": "TPXRXP1im1gyVyxjm7_OBB",
        "__spin_r": "1014728296",
        "__spin_b": "trunk",
        "__spin_t": "1720479957",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "PolarisPostCommentInputRevampedMutation",
        "variables": '{"connections":["client:root:__PolarisPostCommentsDirect__xdt_api__v1__media__media_id__comments__connection_connection(data:{},media_id:\\"' + media_id + '\\",sort_order:\\"popular\\")"],"request_data":{"comment_text":"' + comment + '"},"media_id":"' + media_id + '"}',
        "server_timestamps": "true",
        "doc_id": "7980226328678944"
    }
                            headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  'sec-ch-ua-model': "\"SO-51A\"",
  'x-ig-app-id': "1217981644879628",
  'sec-ch-ua-mobile': "?1",
  'x-bloks-version-id': "213e4f338be29ab2c08f8071c4feb979c6b2fe37d4124f56e5c4b00e51a21aaf",
  'x-fb-lsd': "TPXRXP1im1gyVyxjm7_OBB",
  'sec-ch-ua-platform-version': "\"12.0.0\"",
  'x-fb-friendly-name': "PolarisPostCommentInputRevampedMutation",
  'x-asbd-id': "129477",
  'sec-ch-ua-full-version-list': "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.122\", \"Google Chrome\";v=\"126.0.6478.122\"",
  'sec-ch-prefers-color-scheme': "dark",
  'x-csrftoken': "EOiLbpIOFClXHpaV9U3UUrcxycjGwlAJ",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://www.instagram.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.instagram.com/p/C9LR5HNgrA8/comments/",
  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
  'Cookie': f"mid=Zk53LwAEAAHkGLfrbNVpJgdYnGXH; ig_did=1B11344A-A9B9-4A2A-AFCF-77AB484FB822; ig_nrcb=1; datr=LXdOZqsyg3XFNCiMUsQHCbbq; ps_n=1; ps_l=1; ig_lang=en; oo=v1; ds_user_id=63489588072; fbm_124024574287414=base_domain=.instagram.com; dpr=2.625; shbid=\"9691\\05463489588072\\0541751922854:01f7b5727e74baa9dcc5314136d049d4353190da7225e7005234a6ed8eb1da03774b76ba\"; shbts=\"1720386854\\05463489588072\\0541751922854:01f7503f14f25930b4afbe5064ae6669116cc605f95c92acb0123291421f59f238958a4d\"; csrftoken=EOiLbpIOFClXHpaV9U3UUrcxycjGwlAJ; sessionid={sessionid.strip()}; ig_direct_region_hint=\"CLN\\05463489588072\\0541752015472:01f75175df540614b3cdb4840e2fb526805bddf4c284b61ff02bffefd7a8c20b6f89b530\"; wd=418x842; fbsr_124024574287414=-nJmPoFC3Idt-X8HBmpH1GpXMD-Di7zNn-YI6S9ueTs.eyJ1c2VyX2lkIjoiMTAwMDg4ODY4MjkzNzcyIiwiY29kZSI6IkFRQTk5dHB4cFlYZ21SdXpwQkJpUUk5RlB3TVcyNmlEbm9IYlZOSXhHWXBCWldxeXZsZlIyWTdaUzcwdkRzUjEtVjVtUW9aV1Q0ejVVeUNNMS1tVUlOYjU3YU43Znp4MWxmSTZ4aDZ0RllFNWpTVmhTVlNzN3JEaDk3VGtXWmdkQTlqbnFzVEF1TU41VV9yTTdnbHdMejd2MkpvelZBNlRQYm9Lc1Y5aGF4aXFDcHhHc1JGNFBGRUhiODhZVXFycFJTNmc2LU51OFVReW52a0dSTjBabXpQNWd1dnBkc0tBTENmWnlmRmJrdmd4RXI2WHp0SDBzUk81ME1aOE1Jdy1Wd1ladTRoZ0ZqTXRsc2N4bkdLS1dHaTdabWNnVXpfdnVYMkJtaDZMN2JGWDI2TEhYSVlwX3paMlVCTTZBQlVUS0RUdm5OVEM5MkJxTHBLQi1qeVRpY2Z4Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzZCWkMzcGY2akd0WkFoSHVXR3lTMVBtT3hlZGVjalFaQ204VkhTZjVOcW5iM3N3SzBnWkFJRzJaQ0hBOHMzdGVJaVlxN0dTSVFnb3JwbXFIdkhOdjB2aU04UVk0TlE4R2NtNjN6NFd4OWpEdUNlV2kwSTlWRE13OUNMajdJNE45Vm4zUnNJS25QYWpUUFNGWkJLWG1QV2lreHlvSGRpUk53YTJsNk1nWFI4QnpXalFaRFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MjA0Nzk5NTd9; fbsr_124024574287414=-nJmPoFC3Idt-X8HBmpH1GpXMD-Di7zNn-YI6S9ueTs.eyJ1c2VyX2lkIjoiMTAwMDg4ODY4MjkzNzcyIiwiY29kZSI6IkFRQTk5dHB4cFlYZ21SdXpwQkJpUUk5RlB3TVcyNmlEbm9IYlZOSXhHWXBCWldxeXZsZlIyWTdaUzcwdkRzUjEtVjVtUW9aV1Q0ejVVeUNNMS1tVUlOYjU3YU43Znp4MWxmSTZ4aDZ0RllFNWpTVmhTVlNzN3JEaDk3VGtXWmdkQTlqbnFzVEF1TU41VV9yTTdnbHdMejd2MkpvelZBNlRQYm9Lc1Y5aGF4aXFDcHhHc1JGNFBGRUhiODhZVXFycFJTNmc2LU51OFVReW52a0dSTjBabXpQNWd1dnBkc0tBTENmWnlmRmJrdmd4RXI2WHp0SDBzUk81ME1aOE1Jdy1Wd1ladTRoZ0ZqTXRsc2N4bkdLS1dHaTdabWNnVXpfdnVYMkJtaDZMN2JGWDI2TEhYSVlwX3paMlVCTTZBQlVUS0RUdm5OVEM5MkJxTHBLQi1qeVRpY2Z4Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzZCWkMzcGY2akd0WkFoSHVXR3lTMVBtT3hlZGVjalFaQ204VkhTZjVOcW5iM3N3SzBnWkFJRzJaQ0hBOHMzdGVJaVlxN0dTSVFnb3JwbXFIdkhOdjB2aU04UVk0TlE4R2NtNjN6NFd4OWpEdUNlV2kwSTlWRE13OUNMajdJNE45Vm4zUnNJS25QYWpUUFNGWkJLWG1QV2lreHlvSGRpUk53YTJsNk1nWFI4QnpXalFaRFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MjA0Nzk5NTd9; rur=\"CLN\\05463489588072\\0541752015968:01f768ed5c5e328511f99d8bbe8b95bdf1e6656cccad6af55ac944fc2a004270e7419edf\""
}

                            try:
                                response = requests.post(url, data=payload, headers=headers)
                                if response.status_code == 200:
                                    bot.send_message(message.chat.id,text=f"Done Sned Comment 🟢 : {comment} ")
                                else:
                                    bot.reply_to(message.chat.id,text=f"Erorr Sned Comment 🔴 : {comment} ")     
                            except:
                                bot.reply_to(message,f"Erorr Sned Comment 🟡 : {comment} ")
                            markup = types.InlineKeyboardMarkup()
                            back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
                            markup.add(back_button)
                        bot.reply_to(message,text=f"Sending Has Been Completed ! : {bb} Cooment ✅ ",reply_markup=markup)    
    except Exception as e:
                 bot.reply_to(message,f"Erorr Sned Comment 🟡 : {e} ")                                           


def get_username_for_follow(message):
    username = message.text.strip()
    send_follow(message, username)

def send_follow(message, username):
    try:                                 
        info = requests.get(f'https://anonyig.com/api/ig/userInfoByUsername/{username}').json()  
        id = info['result']['user']['pk_id']
        followers = info['result']['user']['follower_count']
        name = info['result']['user']['full_name']
    except:
        bot.reply_to(message,text="Not Found User 🔴")	
    bot.reply_to(message,text=f"Name : {name}\nFollowers : {followers}")
    with open("sessionid.txt", 'r') as file:
        bb = 0
        for sessionid in file:
            bb+=1
            url = "https://www.instagram.com/graphql/query"
            payload = "av=17841463482176198&__d=www&__user=0&__a=1&__req=1d&__hs=19912.HYP%3Ainstagram_web_pkg.2.1..0.1&dpr=3&__ccg=UNKNOWN&__rev=1014719072&__s=rnaco8%3Anz1wox%3Av5y2ff&__hsi=7389311274914457240&__dyn=7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awpUO0n24oaEnxO1ywOwv89k2C1Fwc60AEC1TwQzXwae4UaEW2G0AEcobEaU2eUlwhEe87q7U1bobpEbUGdG1QwTU9UaQ0Lo6-3u2WE5B08-269wr86C1mwPwUQp1yUb9UK6V89F8uxK3OqcyU-2K&__csr=gnhG2s9gywjinNI8OldPijZiGGbRrZEhSIjFFeAApkFozAlpG-TpVaUGrp2Al-qjGmaLfUDF4K-tauLK8vGVUBzK8AiyAhaAGhuGzFbXx6UCVumQ9GaUhJe6ryK5EKqfpqJ5Kt4AXwyheuag01mpP1S0hNusw0xO6A0a_w1T8pJ9BBixaaDgb40YUvK-8wDxkMW4o94J9O03t82LU1oYM1C40l0wW2l0iU3vF0VBwct2K2S3-EG1f80xE-00BrU&__comet_req=7&fb_dtsg=NAcNf2aV3SdMGH7QeuaNW5sJV-I0Wg-HKoyvq6G40sCY_bWQHPNzufg%3A17843676607167008%3A1720386839&jazoest=26131&lsd=KWr0jl7RmIV0DIXM6doKmO&__spin_r=1014719072&__spin_b=trunk&__spin_t=1720458100&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=usePolarisFollowMutation&variables=%7B%22target_user_id%22%3A%22"+str(id)+"%22%2C%22container_module%22%3A%22profile%22%2C%22nav_chain%22%3A%22PolarisFeedRoot%3AfeedPage%3A1%3Avia_cold_start%2CPolarisProfilePostsTabRoot%3AprofilePage%3A2%3Aunexpected%22%7D&server_timestamps=true&doc_id=7275591572570580"
            headers = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
  'sec-ch-ua-model': "\"\"",
  'x-ig-app-id': "936619743392459",
  'sec-ch-ua-mobile': "?0",
  'x-bloks-version-id': "213e4f338be29ab2c08f8071c4feb979c6b2fe37d4124f56e5c4b00e51a21aaf",
  'x-fb-lsd': "KWr0jl7RmIV0DIXM6doKmO",
  'sec-ch-ua-platform-version': "\"\"",
  'x-fb-friendly-name': "usePolarisFollowMutation",
  'x-asbd-id': "129477",
  'sec-ch-ua-full-version-list': "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.122\", \"Google Chrome\";v=\"126.0.6478.122\"",
  'sec-ch-prefers-color-scheme': "dark",
  'x-csrftoken': "HC2JHcMAJXUR1jpvmlNlsTiRAzBnXDOA",
  'sec-ch-ua-platform': "\"Linux\"",
  'origin': "https://www.instagram.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.instagram.com/e___e/",
  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
  'Cookie': f"mid=Zk53LwAEAAHkGLfrbNVpJgdYnGXH; ig_did=1B11344A-A9B9-4A2A-AFCF-77AB484FB822; ig_nrcb=1; datr=LXdOZqsyg3XFNCiMUsQHCbbq; ps_n=1; ps_l=1; ig_lang=en; oo=v1; ds_user_id=63489588072; fbm_124024574287414=base_domain=.instagram.com; dpr=2.625; csrftoken=HC2JHcMAJXUR1jpvmlNlsTiRAzBnXDOA; sessionid={sessionid.strip()}; shbid=\"9691\\05463489588072\\0541751922854:01f7b5727e74baa9dcc5314136d049d4353190da7225e7005234a6ed8eb1da03774b76ba\"; shbts=\"1720386854\\05463489588072\\0541751922854:01f7503f14f25930b4afbe5064ae6669116cc605f95c92acb0123291421f59f238958a4d\"; wd=980x1973; fbsr_124024574287414=2zuIAvEsLotMZ4NVNBCB09rx0UY6NCqZqL499eFonKY.eyJ1c2VyX2lkIjoiMTAwMDg4ODY4MjkzNzcyIiwiY29kZSI6IkFRQ290MGZKeFdsenpJS0Q0MHVySGJHUHA5aWZVX2hSbjd6Q1BvVFVtOHM1dFZKM0xlRnZyRE85OHJOV25QTTItSDV1bnVJT1lSUU1aRGtRRFNzd3FMSV9wMVM5R1VadXFacFF1SVdqbWZvN05ZUjJwZEpGN0l0elJCcnE3Z3Y2QkxfOHdWc0gyemtXdEtFMkJVLVNYSkNOa1FvZ0FVcjZfc1RXcWxEbXB1VjNTaFc0cjNQQ21jMTJxYnBJVGozbWJhTS1VcDVoajRSb0ZZaWk2T0JLdmlNOXpIRHBWMXBNUjV3Sk02em9WZ1BDM3dOUjYxcXA5bkZQV3ZyaGxlVlJOYVZoTEhwM1F0SWtOVTkwNlQta2VvT1VOYTVUNkRCcldoYnNBOUtWZzFaMExOalZNVXhVODhwQjFTcjJ5NFR6UVlWMkZJLW95d3h3UHRDaG41YjhyUGh5Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCT3p2WkJ1OU1rN21jYUQ4NjFHaXdiNVNaQnVYZ1JwN0VtajFsYjhmWkJFYUF0bzhwV2tHQXQ0TXJvUnhRNXI0emFQZ3gyamdtWkFyamlFUnlOQlVKUkdGc0xUNk5SNGxROUVsOWZrSnB4anJnSU5QalVpUG9XeVFwSlRQT3BVN2tkWVZmOHVtUkVxMVUydGtiRkxzckZoTW13VlRDbkNzc3lVb1pDYmE2a1A3QnAxUUg0WkJZT2dxN0FaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNzIwNDU4MTA0fQ; rur=\"RVA\\05463489588072\\0541751994112:01f7b18faaa0d55fdfbba13c9b0334f5ee25bdb539a6b6fb7bdbff92cbe3c182a005787a\""
}


            try:
                response = requests.post(url, data=payload, headers=headers)
    
                if response.status_code == 200:                
                    bot.send_message(message.chat.id,f"Done Send Follow 🟢\nName : {name}\nFollowers : {followers+bb} 🆙")
                else:
                    bot.send_message(message.chat.id, "Erorr Send Follow 🔴")
                markup = types.InlineKeyboardMarkup()
                back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
                markup.add(back_button)
                bot.reply_to(message,text=f"Sending Has Been Completed ! : {bb} Followers ✅ ",reply_markup=markup)
            except:
                bot.send_message(message.chat.id, "Erorr Send Follow 🟡")

def show_story(message):
    pass

def add_account(message):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="( Back )", callback_data="back")
    markup.add(back_button)
    msg = bot.send_message(message.chat.id, "Send Username (email) And Password\nExample:\nusername\npassword",reply_markup=markup)
    
def process_account(message):
    try:
        username, password = message.text.split('\n')
        response = login_instagram(username, password)
        if response and 'authenticated":true' in response.text:
            sessionid = response.cookies.get('sessionid', None)
            if sessionid:
                with open("sessionid.txt", 'w') as file:
                    file.write(sessionid + "\n")
                bot.reply_to(message, f"-Your Key 🟢  : `{sessionid}`", parse_mode="Markdown")
        else:
            bot.reply_to(message, "Error Login 🔴")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)} 🔴")
        
def login_instagram(username, password):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    data = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
        'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': 'bc3d5af829ea',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.post(url, headers=headers, data=data)
    return response

@bot.message_handler(commands=["showsessions"])
def show_sessions(message):
        with open("sessionid.txt", 'r') as file:
            for line in file:        
                bot.reply_to(message, f"List session IDs 🟡 :\n{line.strip()}")
   
bot.polling()
