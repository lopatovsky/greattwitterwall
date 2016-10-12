'''
Twitter Wall

Twitter Wall pro terminál. Aplikace, která bude zobrazovat tweety odpovídající určitému hledání do terminálu v nekonečné smyčce.

Aplikace načte určitý počet tweetů odpovídající hledanému výrazu, zobrazí je a v nějakém intervalu se bude dotazovat na nové tweety (použijte API argument since_id).

Pomocí argumentů půjde nastavit:

cesta ke konfiguračnímu souboru s přístupovými údaji
hledaný výraz
počet na začátku načtených tweetů
časový interval dalších dotazů
nějaké vlastnosti ovlivňující chování (např. zda zobrazovat retweety)

'''

import requests
import base64
import configparser
import time
import click

def twitter_session(api_key, api_secret):

  session = requests.Session()
  secret = '{}:{}'.format(api_key, api_secret)
  secret64 = base64.b64encode(secret.encode('ascii')).decode('ascii')

  headers = {
    'Authorization': 'Basic {}'.format(secret64),
    'Host': 'api.twitter.com',
  }

  r = session.post('https://api.twitter.com/oauth2/token',
                   headers=headers,
                   data={'grant_type': 'client_credentials'})

  bearer_token = r.json()['access_token']

  def bearer_auth(req):
      req.headers['Authorization'] = 'Bearer ' + bearer_token
      return req

  session.auth = bearer_auth
  return session


def get_secrets( file_name ):

  config = configparser.ConfigParser()
  config.read( file_name )
  return ( config['twitter']['key'], config['twitter']['secret'] )



def get_twitter_wall( session ):

  max_id = 0

  while( True ):

    r = session.get('https://api.twitter.com/1.1/search/tweets.json',
                    params={'q': '#'+word, 'count': begin, 'result_type': 'recent',
                    'since_id': max_id, 'lang' : lang }, )

    max_id = r.json()['search_metadata']['max_id']
    begin = 100

    if ( len( r.json()['statuses']  ) > 0 ):

      print( 10 * '*' ,  time.strftime("%H:%M:%S", time.gmtime()) , 10 * '*'  )

      for tweet in r.json()['statuses']:
        print(tweet['text'])
        print (20 * '-')

    time.sleep(period)



@click.command()
@click.option('--word', prompt='Find hashtag:', default='MI-PYT', help='Find the tweets for hastag.')
@click.option('--cfg_file', prompt='Your twitter secrets file:', default='auth.cfg', help='Add a file consisting of twitter key and secret.')
@click.option('--begin', default=5 , help='Show how many tweets do you want to show at beginning.')
@click.option('--period', default=5 , help='Set update period for new tweets (seconds).')
@click.option('--lang', default='en' , help='Specify the language of tweets [en,cs,zh... ].')
def get_parameters(  word, cfg_file,  begin , period, lang ):

  session = twitter_session( *get_secrets( cfg_file ) )
  get_twitter_wall( session, begin, period, lang )




if __name__ == '__main__':

  get_parameters()

