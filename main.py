import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath
import time

from dotenv import load_dotenv
import requests
from instabot import Bot
from fetch_spacex_last_launch import fetch_spacex_last_launch
from fetch_hubble_last_launch import fetch_hubble_last_launch


if __name__ == "__main__":
    try:
        load_dotenv()
        fetch_spacex_last_launch()
        fetch_hubble_last_launch()

        bot = Bot()
        bot.login(username=os.environ['LOGIN'], password=os.environ['PASSWORD'])
        mypath = "images"
        for pic in listdir(mypath):
            if not isfile(joinpath(mypath, pic)):
                continue

            picture = '.\{}\{}'.format(mypath, pic)
            bot.upload_photo(picture, caption=pic)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
                time.sleep(1)

    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))
