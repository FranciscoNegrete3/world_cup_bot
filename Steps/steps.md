# Steps to connect to Twitter API


## Functions

### Create Tweets:
The following lines of code are the minimun to post a Tweet from our main.py app  

    def create_tweet(string : str):

        response = client.create_tweet(text=string)

        return response
    
    print(create_tweet("Tweet post from main.py example!!"))

### Delete Tweets:
To delete a specific tweet, you can use delete_tweet() function, that was created in main.py  
Tey key parameter it admits is an string, which you can fin selectig the tweet you want to
delete.

<img src="delete_tweet.jpg">