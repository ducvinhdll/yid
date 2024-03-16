from keep_alive import keep_alive
keep_alive()


import telebot
import datetime
import time
import os
import subprocess
import random
import psutil
import sqlite3
import hashlib
import requests
import datetime
import sys
import pytube

bot_token = '6838265816:AAFlzFcxH4RATMtDKftDwE656x5kg2trMDQ'
bot = telebot.TeleBot(bot_token)

allowed_group_id = "-1002036866060"
allowed_users = []
processes = []
ADMIN_ID = '5789810284'

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT
    )
''')
connection.commit()


def TimeStamp():
  now = str(datetime.date.today())
  return now


def load_users_from_database():
  cursor.execute('SELECT user_id, expiration_time FROM users')
  rows = cursor.fetchall()
  for row in rows:
    user_id = row[0]
    expiration_time = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
    if expiration_time > datetime.datetime.now():
      allowed_users.append(user_id)


def save_user_to_database(connection, user_id, expiration_time):
  cursor = connection.cursor()
  cursor.execute(
      '''
        INSERT OR REPLACE INTO users (user_id, expiration_time)
        VALUES (?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
  connection.commit()


print("✧══════ ༺༻ •══════✧\nThe bot has been started successfully\n✧══════ ༺༻ •══════✧")


def add_user(message):
  admin_id = message.from_user.id
  if admin_id != ADMIN_ID:
    bot.reply_to(message, 'BẠN KHÔNG CÓ QUYỀN SỬ DỤNG LỆNH NÀY😾.')
    return

  if len(message.text.split()) == 1:
    bot.reply_to(message, ' VUI LÒNG NHẬP ID NGƯỜI DÙNG ')
    return

  user_id = int(message.text.split()[1])
  allowed_users.append(user_id)
  expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
  connection = sqlite3.connect('user_data.db')
  save_user_to_database(connection, user_id, expiration_time)
  connection.close()

  bot.reply_to(
      message,
      f'🚀NGƯỜI DÙNG CÓ ID {user_id} ĐÃ ĐƯỢC THÊM VÀO DANH SÁCH ĐƯỢC PHÉP SỬ DỤNG LỆNH /supersms.🚀'
  )


load_users_from_database()


@bot.message_handler(commands=['get'])
def get(message):
  bot.reply_to(message, text='Vui lòng đợi')

  with open('key.txt', 'a') as f:
    f.close()

  username = message.from_user.username
  string = f'GL-{username}+{TimeStamp()}'
  hash_object = hashlib.md5(string.encode())
  key = str(hash_object.hexdigest())
  print(k)
  url_key = requests.get(
      f'https://traffic123.net/api?api=1ef0151cdb46c25932679b426f9a350093bf4695&url=yourdestinationlink.com{key}'
  ).json()['shortenedUrl']

  text = f'''
  
✧══════ ༺༻ •══════✧
  Your key : {key}.                  
✧══════ ༺༻ •══════✧
 

    '''
  bot.reply_to(message, text)


@bot.message_handler(commands=['k'])
def k(message):
  if len(message.text.split()) == 1:
    bot.reply_to(message, 'sử dụng /get để lấy key')
    return

  user_id = message.from_user.id

  key = message.text.split()[1]
  username = message.from_user.username
  string = f'GL-{username}+{TimeStamp()}'
  hash_object = hashlib.md5(string.encode())
  expected_key = str(hash_object.hexdigest())
  if key == expected_key:
    allowed_users.append(user_id)
    bot.reply_to(
        message,
        'valid key'
    )
  else:
    bot.reply_to(
        message,
        'Invalid key')

@bot.message_handler(commands=['spasbm'])
def lqm_sms(message):
    user_id = message.from_user.id
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Please enter the phone number ')
        return

    phone_number = message.text.split()[1]
    if not phone_number.isnumeric():
        bot.reply_to(message, 'Please choose another number, Invalid phone number.. !')
        return

    if phone_number in ['113','911','114','115','+84328774559','03623402']:
        # Số điện thoại nằm trong danh sách cấm
        bot.reply_to(message,"This number is in the admin area or is banned ❌")
        return

    file_path = os.path.join(os.getcwd(), "cc.py")    
    file_path2 = os.path.join(os.getcwd(), "sms.py")
    file_path3 = os.path.join(os.getcwd(), "n.py")
    file_path4 = os.path.join(os.getcwd(), "liem.py")
    process = subprocess.Popen(["python", file_path, phone_number, "400"])    
    process = subprocess.Popen(["python", file_path2, phone_number, "1000"])
    process = subprocess.Popen(["python", file_path3, phone_number, "300"])
    process = subprocess.Popen(["python", file_path4, phone_number, "300"])
    processes.append(process)
    username = message.from_user.username

    current_time = time.time()
    if username in cooldown_dict and current_time - cooldown_dict[username].get('free', 0) < 120:
        remaining_time = int(120 - (current_time - cooldown_dict[username].get('free', 0)))
        bot.reply_to(message, f"@{username} Please wait {remaining_time}few seconds to be able to use the command again  /spam.")
        return
    video_url = "https://files.catbox.moe/eewee0.mp4"  # Replace this with the actual video URL      
    message_text =f'Successful attack ✔️\nBot: @Ducvinhtzvnbot\n Spam time: 1000 seconds\n Attack by @{username}\n Number of attacks: {phone_number} \nOwer @hadukiii'
    bot.send_video(message.chat.id, video_url, caption=message_text, parse_mode='html')            
    

@bot.message_handler(commands=['fb'])
def lqm_sms(message):
  user_id = message.from_user.id
  if user_id not in allowed_users:
    bot.reply_to(
        message,
        text=
        'Hãy /get để lấy key sử dụng lệnh này'
    )
    return
  if len(message.text.split()) == 1:
    bot.reply_to(message, 'Please enter link or fb id..')
    return

  phone_number = message.text.split()[1]

  file_path = os.path.join(os.getcwd(), "info.py")
  process = subprocess.Popen(["python", file_path, phone_number, "120"])
  processes.append(process)
  bot.reply_to(
      message,
      f'Please wait a few seconds...'
  )


@bot.message_handler(commands=['start'])
def how_to(message):
  how_to_text = '''
 Cách sử dụng và All lệnh của Bot:
✧══════ ༺༻ •══════✧
- Use the /get command to get the key.
- /tiktok : Download tiktok videos
- /check : /check + [link] check anti ddos
- /k {your key} to identify the key.
- /fb <link hoặc id facebook>: Check facebook information (only authorized users).
- /status: View information about the bot's uptime, % CPU, % Memory, % Disk usage.
- /stop: Stop all running tasks. (Only Administrators Can Use This Command).
-/restart: Restart the bot (Admin only).
- /admin: Display admin information.
- /help: Command list and instructions for use.
✧══════ ༺༻ •══════✧
'''
  bot.reply_to(message, how_to_text)




@bot.message_handler(commands=['help'])
def help(message):
  help_text = '''
 Danh sách lệnh:
- /get : Lấy key sử dụng bot
- /tiktok : tải video tiktok
- /check : /check + link
- /fb <link hoặc id facebook>: Check thông tin facebook (chỉ người dùng được phép).
- /k "key của bạn": Kiểm tra key và xác nhận quyền sử dụng lệnh /fb.
- /status: Xem thông tin về thời gian hoạt động, % CPU, % Memory, % Disk đang sử dụng của bot.
- /stop: Dừng lại tất cả các tác vụ đang chạy. ( Chỉ Quản Trị Viên Mới Được Dùng Lệnh Này).
-/restart: Khởi động lại bot (Chỉ admin).
- /admin: Hiển thị thông tin admin.
'''
  bot.reply_to(message, help_text)

@bot.message_handler(commands=['check'])
def check_ip(message):
    if len(message.text.split()) != 2:
        bot.reply_to(message, 'Please enter the correct syntax\n For example: /check + link')
        return

    url = message.text.split()[1]
    
    # Kiểm tra xem URL có http/https chưa, nếu chưa thêm vào
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    # Loại bỏ tiền tố "www" nếu có
    url = re.sub(r'^(http://|https://)?(www\d?\.)?', '', url)
    
    try:
        ip_list = socket.gethostbyname_ex(url)[2]
        ip_count = len(ip_list)

        reply = f"Website's IP : {url}\n To be: {', '.join(ip_list)}\n"
        if ip_count == 1:
            reply += "Websites with 1 or 2 IPs are likely not blocked by ddos ."
        else:
            reply += "𝑊𝑒𝑏𝑠𝑖𝑡𝑒 𝑐𝑜́ 𝑛ℎ𝑖𝑒̂̀?? ℎ𝑜̛𝑛 1 𝑖?? 𝑘ℎ𝑎̉ 𝑛𝑎̆𝑛𝑔 𝑎𝑛𝑡𝑖𝑑𝑑𝑜𝑠 𝑟𝑎̂́𝑡 𝑐𝑎𝑜.\n𝐾ℎ𝑜̂𝑛𝑔 𝑡ℎ𝑒̂̉ 𝑡𝑎̂́𝑛 𝑐𝑜̂𝑛𝑔 𝑤𝑒𝑏𝑠𝑖𝑡𝑒 𝑛𝑎̀𝑦."

        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"𝐶𝑜́ 𝑙𝑜̂̃𝑖 𝑥𝑎̉𝑦 𝑟𝑎: {str(e)}")

@bot.message_handler(commands=['admin'])
def how_to(message):
  how_to_text = '''
 Thông Tin Admin:
✧══════ ༺༻ •══════✧
- LÊ ĐỨC VINH // LÝ QUANG VINH // VU HAI LAM
🚀Thông Tin Liên Hệ ☎️:🚀
- Owner Telegram: https://t.me/hadukiii
- Ower helps : @kun_dzll
- Facebook: https://facebook.com/ducvinhdll
✧══════ ༺༻ •══════✧
'''
  bot.reply_to(message, how_to_text)

@bot.message_handler(commands=['tiktok'])
def luuvideo_tiktok(message):
  if len(message.text.split()) == 1:
    sent_message = bot.reply_to(message, '𝑉𝑈𝐼 𝐿𝑂̀𝑁𝐺 𝑁𝐻𝐴̣̂𝑃 𝐿𝐼𝑁𝐾 𝑉𝐼𝐷𝐸𝑂 /𝑡𝑖𝑘𝑡𝑜𝑘 [ 𝐿𝑖𝑛𝑘 𝑉𝑖𝑑𝑒𝑜 ]')
    return
  linktt = message.text.split()[1]
  data = f'url={linktt}'
  head = {
    "Host":"www.tikwm.com",
    "accept":"application/json, text/javascript, */*; q=0.01",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
  }
  response = requests.post("https://www.tikwm.com/api/",data=data,headers=head).json()
  linkz = response['data']['play']
  rq = response['data']
  tieude = rq['title']
  view = rq['play_count']
  sent_message = bot.reply_to(message, f'𝑋𝑖𝑛 𝑐ℎ𝑜̛̀ 𝑚𝑜̣̂𝑡 𝑡𝑖́.!😴\n+ 𝑇𝑖𝑒̂𝑢 𝑑𝑒̂̀: {tieude}\n+ 𝑆𝑜̂́ 𝑣𝑖𝑒𝑤: {view}')
  try:
   bot.send_video(message.chat.id, video=linkz, caption=f'𝐷𝑎̃ 𝑥𝑜𝑛𝑔 𝑐𝑎̉𝑚 𝑜̛𝑛 𝑏𝑎̣𝑛 𝑑𝑎̃ 𝑑𝑢̀𝑛𝑔 𝑏𝑜𝑡🐮\n+ 𝑇𝑖𝑒̂𝑢 𝐷𝑒̂̀: {tieude}\n+ 𝑆𝑜̂́ 𝑣𝑖𝑒𝑤: {view}\n+ 𝐴𝑑𝑚𝑖𝑛: t.me/hadukiii', reply_to_message_id=message.message_id, supports_streaming=True)
  except Exception as e:
   bot.reply_to(message, f'𝑉𝑖𝑑𝑒𝑜 𝑞𝑢𝑎́ 𝑛𝑎̣̆𝑛𝑔 𝑡𝑜̂𝑖 𝑘ℎ𝑜̂𝑛𝑔 𝑡ℎ𝑒̂̉ 𝑔𝑢̛̉𝑖 𝑣𝑢𝑖 𝑙𝑜̀𝑛𝑔 𝑡𝑢̛̣ 𝑡𝑎̉𝑖: {linkz}')
  bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)  

# Hàm tính thời gian hoạt động của bot
start_time = time.time()
@bot.message_handler(commands=['time'])
def show_uptime(message):
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} 𝐺𝑖𝑜̛̀, {minutes} 𝑃ℎ𝑢́𝑡, {seconds} 𝐺𝑖𝑎̂𝑦'
    bot.reply_to(message, f'𝐵𝑜𝑡 𝐷𝑎̃ 𝐻𝑜𝑎̣𝑡 𝐷𝑜̣̂𝑛𝑔 𝐷𝑢̛𝑜̛̣𝑐: {uptime_str}')
    


@bot.message_handler(commands=['status'])
def status(message):
  user_id = message.from_user.id
  process_count = len(processes)
  bot.reply_to(message, f'Số quy trình đang xử lý {process_count}.')


@bot.message_handler(commands=['restart'])
def restart(message):
  user_id = message.from_user.id
  if user_id != ADMIN_ID:
    bot.reply_to(message, 'Đã khởi động lại bot')
    return

  bot.reply_to(message, 'Bot sẽ được khởi động lại sau 3s')
  time.sleep(2)
  python = sys.executable
  os.execl(python, python, *sys.argv)


@bot.message_handler(commands=['stop'])
def stop(message):
  user_id = message.from_user.id
  if user_id != ADMIN_ID:
    bot.reply_to(message, 'Bạn không có quyền Admin')
    return

  bot.reply_to(message, 'Đã dừng bot')
  time.sleep(2)
  bot.stop_polling()


bot.infinity_polling(timeout=60, long_polling_timeout = 1)
