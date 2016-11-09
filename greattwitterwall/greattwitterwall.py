"""
Twitter Wall

This is Great twitter wall, welcome!
:ref:`documentation`.
"""

import requests
import base64
import configparser
import time
import click

def suma( a, b):
  """ This function has nothing to do with the twitter-wall application.
  Use this function to sum two numbers, in case you find the + operator too mainstream.

  """

  return a+b

def twitter_session(api_key, api_secret):
    """The function takes the twitter api key and secret and return the session.
    If you do not know what the api secret and key are, see :ref:`api-secret-key`.
    """

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
    """Function parse the file and optain the twitter api key and secret :ref:`api-secret-key`. """

    config = configparser.ConfigParser()
    config.read( file_name )
    return ( config['twitter']['key'], config['twitter']['secret'] )


def get_twitter_wall( session, word, begin, period, lang ):
    """The function takes the search properties and periodically apply and print the newest tweets."""
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



@click.group()
def cli():
  pass

@cli.command()
@click.option('--word', prompt='Find hashtag:', default='MI-PYT', help='Find the tweets for hastag.')
@click.option('--cfg_file', prompt='Your twitter secrets file:', default='auth.cfg', help='Add a file consisting of twitter key and secret.')
@click.option('--begin', default=5 , help='Show how many tweets do you want to show at beginning.')
@click.option('--period', default=5 , help='Set update period for new tweets (seconds).')
@click.option('--lang', default='en' , help='Specify the language of tweets [en,cs,zh... ].')
def console(  word, cfg_file,  begin , period, lang ):
    """Run the console application"""
    session = twitter_session( *get_secrets( cfg_file ) )
    get_twitter_wall( session, word, begin, period, lang )

############web_application########################################################################

from flask import Flask
from flask import render_template
app = Flask(__name__)

def prepare_data( r ):
    """The function takes the row output of twitter api and transform it to the form usefull to render html page."""
    data = []

    for tweet in r:
        d = {}
        d['name'] = tweet['user']['name']
        d['profile_image_url'] = tweet['user']['profile_image_url']
        d['created_at'] = tweet['created_at']
        s = tweet['text']
        if 'media' in tweet['entities']:
            d['media'] = tweet['entities']['media']

        entities = tweet['entities']['hashtags']
        entities +=tweet['entities']['urls']
        entities +=tweet['entities']['user_mentions']
        entities.sort( key = lambda c: c['indices'][0] )

        b = 0
        text = []

        for ent in entities:
            text.append( s[b:ent['indices'][0] ] )
            text.append( ent )
            b = ent['indices'][1]
        text.append(s[b:])
        
        d['text'] = text

        data.append(d)

    return data


@app.route('/')
@app.route('/<word>/')
def index(word=None):
    """The function takes the searched word (if any) and try to get the data from twitter and render the otput html file."""
    data=None
    if word:
        session = twitter_session( *get_secrets( 'auth.cfg' ) )
        r = session.get('https://api.twitter.com/1.1/search/tweets.json',
                        params={'q': '#'+word, 'count': 10, 'result_type': 'recent',},
                       ).json()['statuses']

        data = prepare_data(r)


    return render_template('index.html', word=word, tweets_list=data  )

@cli.command()
def web():
    """Run the web application"""
    app.run(debug=False) #TODO switch off debug for deployment


def main():
    cli()

