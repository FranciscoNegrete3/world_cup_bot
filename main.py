import re
import tweepy
import datetime

from urllib import response
from credentials import access_token, access_token_secret, api_key, api_key_secret

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)


def create_tweet():

    word_cup_startdate = datetime.date(2022, 11, 20)

    days_remaining = word_cup_startdate - datetime.date.today()

    date = str(days_remaining)

    response = client.create_tweet(text=f"¡Faltan {date[0:2]} días para el Mundial de Qatar!")

    return response


print(create_tweet())


def delete_tweet(id : str):

    """
    This function takes as a parameter a Twit's ID (string), which can be
    found selecting an specifyc tweet. See Steps for more details.
    """

    delete = client.delete_tweet(id)

    return delete

#print(delete_tweet("1576603698792435712"))