import requests
import os, random
import shutil
import schedule
import time

PicFolderPath = "pics"
UploadedPicFolder = "Uploaded Pics"
full_caption = "Follow My Account!!"
bot_api_last_response_status_code = 200
global isCrashed 
isCrashed = False
#functions 

#sending update to teligram
def sendUpdate(msg):
    url = "https://api.telegram.org/bot5117144242:AAEoSCLlH4PaxMXkcTnkxUexGgO489nCLtc/sendMessage?chat_id=-409481725&text="+ msg
    requests.post(url)
 
    
def status ():
       if bot_api_last_response_status_code == 404:
                     global isCrashed
                     isCrashed = True
                     sendUpdate ("An error occurred, Script Paused")
                     
       # Move Uplaoded Photo To Uplaoded Folder
       if bot_api_last_response_status_code == 200:
            
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
    #bot.upload_photo(randfile, caption=full_caption)
    
    shutil.move(randfile, UploadedPicFolder)
    #Getting Available Pics Number
    picCount = len(os.listdir(PicFolderPath))
    sendUpdate (" Remaining Photos Are  " +str(picCount))
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
        schedule.cancel_job(job)
        print ("cancelling job")
job = schedule.every(10).seconds.do(execution)   
while True:
    schedule.run_pending()
    time.sleep(1)     