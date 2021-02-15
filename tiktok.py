from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import subprocess
import random
import string
from selenium.webdriver.chrome.options import Options
from playsound import playsound

#variables
check_delay = 10
username = "jasonfairfield"
sound = "bruh.mp3"

#reset follower count
with open("followers.txt", "w") as myfile:
    myfile.write("0")

driver = webdriver.Edge("C:\\MEGA\\Python\\Tiktok\\msedgedriver.exe")
driver.set_window_size(300, 350)
driver.implicitly_wait(5)
driver.get('https://livecounts.io/embed/tiktok-realtime/{}'.format(username))
sleep(4)

prev_follows = "0"
with open("followers.txt") as file:
    prev_follows = file.read()

def scrape():
    global prev_follows
    followers = "0"

    with open("followers.txt") as file:
            followers = file.read()
            print(followers)

    if (followers != "0"):
        if (prev_follows != followers):
            dif = int(followers) - int(prev_follows)
            if (dif > 0):
                for y in range(dif):
                    playsound(sound)

            prev_follows = followers
        else:
            pass

    with open("followers.txt", "w") as myfile:
            myfile.write("")
    #Scrape live count
    digits = driver.find_elements_by_css_selector('.odometer-value')

    for x in digits:
        value = x.text
        with open("followers.txt", "a") as myfile:
            myfile.seek(0)
            myfile.write(value)

    if (prev_follows == "0"):
        with open("followers.txt") as file:
            prev_follows = file.read()
            print("starter followers: " + prev_follows)

    sleep(check_delay)
    scrape()

scrape()

command = "taskkill /F /IM msedgedriver.exe /T"