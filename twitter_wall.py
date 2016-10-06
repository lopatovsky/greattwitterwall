import requests
import base64
import configparser


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


def get_twitter_wall( word ):

  r = session.get('https://api.twitter.com/1.1/search/tweets.json',params={'q': '#'+word },)
  for tweet in r.json()['statuses']:
    print(tweet['text'])
  return 1




if __name__ == '__main__':

  session = twitter_session( *get_secrets() )

  get_twitter_wall( 'bullshit' )




