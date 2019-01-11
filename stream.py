import json
import tweepy
import socket

ACCESS_TOKEN = '1530972577-O7GUe7x8s9ieLEGDCZA5OmyvEYoWGuPVhA0MioZ'
ACCESS_SECRET = 'EUsaZr2dbQMj6wjhnWqpKTayoH6J6G6ikgffZEnAAbeEZ'
CONSUMER_KEY = '2GY351g5IxRrmbnIe95Im8mR5'
CONSUMER_SECRET = 'Fr4FYQm1kEEPQDCDROUtdyrpUYm5KOTdMfH4ZnO5sgtUqwY1hT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

hashtag = '#guncontrolnow'

TCP_IP = 'localhost'
TCP_PORT = 9001

# create sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((TCP_IP, TCP_PORT))
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        conn.send(status.text.encode('utf-8'))

    def on_error(self, status_code):
        if status_code == 420:
            return False
        else:
            print(status_code)

    def on_data(self,data):
        message = data.encode('utf-8')
        try:
            if "\"location\":null" not in data:
                self.producer.send('twitter',msg)
                return True
        except BaseException as e:
            print(str(e))
            return False

myStream = tweepy.Stream(auth=auth, listener=MyStreamListener())

myStream.filter(track=['#guncontrolnow'])


