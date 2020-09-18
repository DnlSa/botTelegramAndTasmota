import time 
import telepot
import requests
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TOKEN='insert bot token'

def handle(msg):
    chat_id=msg['chat']['id']
    txt= msg['text']
    if '/helpmore' in txt: 
        bot.sendMessage(chat_id,'I reley sono 7  : /on seguito dal numero del reley che vuoi accendere\n /off seguito dal numero del reley che vuoi accendere\n /onall - tutti accesi\n /offall - tutti spenti\n ')
    
    if '/help' in txt: 
        bot.sendMessage(chat_id,'/on1\n/on2\n/on3\n/on4\n/on5\n/on6\n/on7\n/off1\n/off2\n/off3\n/off4\n/off5\n/off6\n/off7\n/offall\n/onall\n/reboot\n/shutdown')
    

    elif '/on1' in txt : 
        GPIO.setup( 11, GPIO.OUT)
        GPIO.output(11, False) #accendi la gpio 11
        bot.sendMessage(chat_id, 'acceso 1')  # messaggio che e acceso il primo rele
        
    elif '/off1' in txt : 
        GPIO.setup( 11, GPIO.OUT)     
        GPIO.output(11, True) # spegni la gpio 11
        bot.sendMessage(chat_id, 'spento 1') #messaggio che e spento il primo rele
        
    elif '/on2' in txt :
        GPIO.setup( 12, GPIO.OUT) # inizializzo gpio
        GPIO.output(12,False)  # accendo GPIO
        bot.sendMessage(chat_id, 'acceso 2')
        
    elif '/off2' in txt :
        GPIO.setup( 12, GPIO.OUT) # inizializzo gpio
        GPIO.output(12,True)  # Spengo GPIO
        bot.sendMessage(chat_id, 'spento 2')

    elif '/on3' in txt :
        GPIO.setup( 13, GPIO.OUT)
        GPIO.output(13,False)
        bot.sendMessage(chat_id, 'acceso 3')
    
    elif '/off3' in txt :
        GPIO.setup( 13, GPIO.OUT)
        GPIO.output(13,True)
        bot.sendMessage(chat_id, 'spento 3')

    elif '/on4' in txt :
        GPIO.setup( 15, GPIO.OUT)
        GPIO.output(15,False)
        bot.sendMessage(chat_id, 'acceso 4')
        
    elif '/off4' in txt :
        GPIO.setup( 15, GPIO.OUT)
        GPIO.output(15,True)
        bot.sendMessage(chat_id, 'spento 4')
        
    elif '/on5' in txt :
        GPIO.setup( 16, GPIO.OUT)
        GPIO.output(16,False)
        bot.sendMessage(chat_id, 'acceso 5')
        
    elif '/off5' in txt :
        GPIO.setup( 16, GPIO.OUT)
        GPIO.output(16,True)
        bot.sendMessage(chat_id, 'spento 5')
    
 
    elif '/on6' in txt :
        GPIO.setup( 18, GPIO.OUT)
        GPIO.output(18,False)
        bot.sendMessage(chat_id, 'acceso 6')
        
    elif '/off6' in txt :
        GPIO.setup( 18, GPIO.OUT)
        GPIO.output(18,True)
        bot.sendMessage(chat_id, 'spento 6')
    
    elif '/on7' in txt :
        GPIO.setup( 22, GPIO.OUT)
        GPIO.output(22,False)
        bot.sendMessage(chat_id, 'acceso 7')
        
    elif '/off7' in txt :
        GPIO.setup( 22, GPIO.OUT)
        GPIO.output(22,True)
        bot.sendMessage(chat_id, 'spento 7')
    
    elif '/offall' in txt :
        GPIO.setup( 11, GPIO.OUT)
        GPIO.output(11,True)
        GPIO.setup( 12, GPIO.OUT)
        GPIO.output(12,True)
        GPIO.setup( 13, GPIO.OUT)
        GPIO.output(13,True)
        GPIO.setup( 15, GPIO.OUT)
        GPIO.output(15,True)
        GPIO.setup( 16, GPIO.OUT)
        GPIO.output(16,True)
        GPIO.setup( 18, GPIO.OUT)
        GPIO.output(18,True)
        GPIO.setup( 22, GPIO.OUT)
        GPIO.output(22,True)
        bot.sendMessage(chat_id, 'tutti spenti')


    elif '/onall' in txt :
        GPIO.setup( 11, GPIO.OUT)
        GPIO.output(11,False)
        GPIO.setup( 12, GPIO.OUT)
        GPIO.output(12,False)
        GPIO.setup( 13, GPIO.OUT)
        GPIO.output(13,False)
        GPIO.setup( 15, GPIO.OUT)
        GPIO.output(15,False)
        GPIO.setup( 16, GPIO.OUT)
        GPIO.output(16,False)
        GPIO.setup( 18, GPIO.OUT)
        GPIO.output(18,False)
        GPIO.setup( 22, GPIO.OUT)
        GPIO.output(22,False)
        bot.sendMessage(chat_id, 'tutti accesi')

    elif '/shutdown' in txt: 
        bot.sendMessage(chat_id, 'spengo il sistema')
        os.popen('sudo shutdown -h now')
        
    elif '/reboot' in txt: 
        bot.sendMessage(chat_id, 'riavvio il sistema')
        os.popen('sudo reboot')


    else:
        bot.sendMessage(chat_id, 'i do not know')
    
bot =telepot.Bot(TOKEN)
bot.message_loop(handle)
print('receive')
    
while 1:
    time.sleep(10)
