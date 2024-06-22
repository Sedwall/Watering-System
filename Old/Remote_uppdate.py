import tweepy as tw

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
Sedwall_ID = "960455320987426816"
Alfred_ID = "1600563617099042816"
print("Setup done...")


def send_message(text=None, screenshot=False):
    try:
        DM = api.send_direct_message(Sedwall_ID, text)
        print("Message sent:\n" + text)
    except:
        print("Message not sent...")


def get_message():
    my_dms = api.get_direct_messages()
    dm = my_dms[0]
    print("Massage resived...")
    return dm