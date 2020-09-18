import time  # for time.sleep in the cicle 
import telepot # for bot telegram
import requests #for command sonoff 
import os  #for command raspberry

TOKEN='insert token bot'

def handle(msg):
    chat_id=msg['chat']['id']
    txt= msg['text']
    
#Raspberry commands
    if '/shutdown' in txt: 
        bot.sendMessage(chat_id, 'shutdown the system')
        os.popen('sudo shutdown -h now')
        
    elif '/reboot' in txt: 
        bot.sendMessage(chat_id, 'reboot the system')
        os.popen('sudo reboot')
        
#use for this command a sonoff whit firmware tasmota

    elif '/on' in txt : 
        requests.get("http://insert sonoff local ip /cm?cmnd=Power%20On")
        bot.sendMessage(chat_id, 'ON')
        
        
    elif '/off' in txt : 
        requests.get("http://insert sonoff local ip /cm?cmnd=Power%20Off")
        bot.sendMessage(chat_id, 'OFF')

    elif '/cicle' in txt : 
        requests.get("http://insert sonoff local ip/cm?cmnd=Power%20Off")
        bot.sendMessage(chat_id, 'OFF')
        time.sleep(3)
        requests.get("http://insert sonoff local ip/cm?cmnd=Power%20On")
        bot.sendMessage(chat_id, 'ON')
        
    elif '/help' in txt : 
        bot.sendMessage(chat_id, 'command avaiable are:\n /on - power on sonoff\n /off - power off sonoff\n /ciclo - power on and off sonoff\n /shutdown - shutdown the system\n /reboot - reboot the system')
    else:
        bot.sendMessage(chat_id, 'I do not know')
    
bot =telepot.Bot(TOKEN)
bot.message_loop(handle)
print('bot online :)')
    
while 1:
    time.sleep(10)
