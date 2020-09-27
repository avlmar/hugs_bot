import tweepy
import time

print('Virtual Hugs Bot, starting now!')

CONSUMER_KEY = 'kxiDTFJ1sV5yPMiaYFXod6qYM'
CONSUMER_SECRET = 'jUKYqw38KUBH2CKcHfR45AnZdKIJKRqVvTsa2cNj8yLKIUUqH7'
ACCESS_KEY = '1309743641104183296-43nCeyJC40g9nZfKzzZ7VjL7ykY1zC'
ACCESS_SECRET = 'tQIzMXTfWazJUXzTrozdtaEE1G0Kda2CsorbkmKKXsKge'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name,'r')
    last_seen_id = f_read.read()
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

if __name__ == '__main__':
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    #mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    search = api.search('i need a hug')
    
    #for mention in reversed(mentions):
        #print(str(mention.id) +' - ' + mention.full_text)

        #last_seen_id = mention.id
        #store_last_seen_id(last_seen_id, FILE_NAME)

    for result in search:
        if 'i need a hug' in result.text.lower():#mention.full_text.lower():
            print(result.user.screen_name + result.text)
            print('Found someone that needs virtual hugs!')
            print('Sending them over right now...')
            api.update_status('@' + result.user.screen_name + #mention.user.screen_name +
                ' Sending you lots of virtual hugs! Remember that you are loved!',result.id)#mention.id)
            store_last_seen_id(last_seen_id, FILE_NAME)
