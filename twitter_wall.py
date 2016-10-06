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

def get_secrets():

  config = configparser.ConfigParser()
  config.read('auth.cfg')
  return ( config['twitter']['key'], config['twitter']['secret'] )


def get_twitter_wall( word, num, time_type ):

  max_id = 0

  while( True ):

    print( 20 * '*')


    r = session.get('https://api.twitter.com/1.1/search/tweets.json',params={'q': '#'+word, 'count': num, 'result_type': time_type, 'since_id': max_id }, )

    max_id = r.json()['search_metadata']['max_id']
    num = 100

    for tweet in r.json()['statuses']:
      print (20 * '-')
      print(tweet['text'])
      print (20 * '-')

    time.sleep(5)


def get_arguments():
  return 1;

'''
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello {}!'.format(name))

'''

if __name__ == '__main__':
  #hello()

  get_arguments()

  session = twitter_session( *get_secrets() )


  get_twitter_wall( 'travel', 5, 'recent'  )



