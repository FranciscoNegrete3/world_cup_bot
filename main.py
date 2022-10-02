import re
from urllib import response
import tweepy

from credentials import access_token, access_token_secret, api_key, api_key_secret

client = tweepy.Client(
    consumer_key= api_key,
    consumer_secret= api_key_secret,
    access_token= access_token ,
    access_token_secret=access_token_secret
)

print(client)

response = client.create_tweet(text="Hola Copa Qatar!")


response_dos = 
print(response)