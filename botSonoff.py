import time 
import telepot
import requests

# firmware my sonoff in Tasmota
#http://ip your sonoff /cm?cmnd=Power%20On    turn on sonoff  
#http://ip your sonoff/cm?cmnd=Power%20Off   turn off sonoff


TOKEN='TOKEN BOT'

def handle(msg):
    chat_id=msg['chat']['id']
    txt= msg['text']
    if '/hi' in txt: 
        bot.sendMessage(chat_id,'hi firend')

    elif '/on' in txt :  #turn on sonoff 
        requests.get("http://ip your sonoff/cm?cmnd=Power%20On")
        bot.sendMessage(chat_id, 'ON')
        
    elif '/off' in txt : 
        requests.get("http://ip your sonoff/cm?cmnd=Power%20Off")
        bot.sendMessage(chat_id, 'OFF')
        
    elif '/ciclo' in txt : 
        requests.get("http://ip your sonoff/cm?cmnd=Power%20On")
        bot.sendMessage(chat_id, 'ON')
        time.sleep (1)
        requests.get("http://ip your sonoff/cm?cmnd=Power%20Off")
        bot.sendMessage(chat_id, 'OFF')
         
    else:
        bot.sendMessage(chat_id, 'i can not')
    
bot =telepot.Bot(TOKEN)
bot.message_loop(handle)
print('listening')
    
while 1:
    time.sleep(10)
