import instabot
import requests
import os, random
import shutil
import schedule
import time
from instabot import Bot, utils 



PicFolderPath = "pics"
UploadedPicFolder = "Uploaded Pics"
full_caption = "Follow My Account!!"
global isCrashed 
isCrashed = False
#functions 

bot = Bot()
bot.login(username="cute_animals_fans_2021", password="Avinash@2003")

#sending update to teligram
def sendUpdate(msg):
    url = "https://api.telegram.org/bot5117144242:AAEoSCLlH4PaxMXkcTnkxUexGgO489nCLtc/sendMessage?chat_id=-409481725&text="+ msg
    requests.post(url)
 
    
def status ():
       if bot.api.last_response.status_code != 200:
                     global isCrashed
                     isCrashed = True
                     sendUpdate ("An error occurred, Script Paused")
                     
       # Move Uplaoded Photo To Uplaoded Folder
       if bot.api.last_response.status_code == 200:
            
               isCrashed = False
               sendUpdate ("All Okay")
#Uploading Pic To Ig
def uploadPic():
    # Choosing Random Photo
    randfile1 = random.choice(os.listdir(PicFolderPath)) 
    sendUpdate ("Uploaded Pic Is : "+randfile1)
    #Get Path
    randfile = os.path.join(PicFolderPath, randfile1)
    # Upload Random Photos
    bot.upload_photo(randfile, caption=full_caption)
    time.sleep(1)
    shutil.move(randfile+"REMOVE_ME", UploadedPicFolder)
    #Getting Available Pics Number
    picCount = len(os.listdir(PicFolderPath))
    sendUpdate ("Remaining Photos Are  " +str(picCount))
    print(str(picCount)+" Left")

#execution
def execution ():
    status ()
    print ("Running Update")
    if isCrashed == False:
        uploadPic ()   
        print ("Uploading Pic")
    else:
        #schedule.clear()
        schedule.clear()
        print ("cancelling job")
        sendUpdate( "job cleared ")

def timegen():
    global time_str1
    time_str1 = '{:02d}:{:02d}'.format(random.randint(9, 10), random.randint(0, 59)) # MorningUpload
    global time_str2
    time_str2 = '{:02d}:{:02d}'.format(random.randint(15, 16), random.randint(0, 59)) # AfterNoon
    global time_str3
    time_str3 = '{:02d}:{:02d}'.format(random.randint(21, 22), random.randint(0, 59)) # EvenongUpload
    sendUpdate("Posting Time Generated\n" "Morning      : " + time_str1 + "\n" "AfterNoon  : " + time_str2 + "\n" "Night           : " + time_str3)
    job1 = schedule.every().day.at(time_str1).do(execution)
    job2 = schedule.every().day.at(time_str2).do(execution)
    job3 = schedule.every().day.at(time_str3).do(execution)

def clrjob():
    schedule.clear()

schedule.every().day.at("08:00").do(timegen)
schedule.every().day.at("23:15").do(clrjob)

while True:
    schedule.run_pending()
    time.sleep(1)

