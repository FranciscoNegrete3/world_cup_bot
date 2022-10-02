import re
from urllib import response
import tweepy

from credentials import access_token, access_token_secret, api_key, api_key_secret

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)


def create_tweet(string : str):

    response = client.create_tweet(text=string)

    return response


#print(create_tweet(input("Enter a Tweet you want to post: ")))


def delete_tweet(id : str):

    """
    This function takes as a parameter a Twit's ID (string), which can be
    found selecting an specifyc tweet. See Steps for more details.
    """

    delete = client.delete_tweet(id)

    return delete

print(delete_tweet("1576603698792435712"))