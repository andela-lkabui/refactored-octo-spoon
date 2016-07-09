import os
import base64
import urllib
import urllib2
import json


class Twitter(object):
    """
    This class contains the core of this app's functionality.
    """

    def __init__(self, screen_name):
        self.screen_name = screen_name

    def api_key_secret_encoder(self):
        """
        Performs `url encoding` on this Twitter app's `key` and `secret`
        values.

        These encoded values are then concatenated in the following format.
            `<key>:<secret>`
        The resulting concatenated string is then returned in a base64 encoded
        format.
        """
        api_key = urllib.urlencode({'k': os.environ.get('API_KEY')})[2::]
        api_secret = urllib.urlencode({'s': os.environ.get('API_SECRET')})[2::]
        encodeable = "{0}:{1}".format(api_key, api_secret)
        return base64.b64encode(encodeable)

    def get_access_token(self):
        """
        Returns a response object from the Twitter API's authentication route.

        Sends a get request to Twitter's authentication route with the
        `grant_type` parameter along with the `Authorization` and `Content-Type`
        headers.
        """
        auth_url = 'https://api.twitter.com/oauth2/token?'
        headers = {
            'Authorization': 'Basic {0}'.format(self.api_key_secret_encoder()),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        values = {'grant_type': 'client_credentials'}
        data = urllib.urlencode(values)
        req = urllib2.Request(auth_url, data, headers)
        resp = urllib2.urlopen(req)
        resp_dict = json.loads(resp.read())
        return resp_dict

    def fetch_tweets(self):
        """
        Returns tweets of the Twitter user identified by the `screen_name`
        parameter.
        """
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?'
        headers = {
            'Authorization': 'Bearer {0}'.format(
                                        self.get_access_token().get(
                                            'access_token'
                                        )
                            )
        }
        values = {
            'screen_name': self.screen_name,
            'contributor_details': False,
            'trim_user': True
        }
        data = urllib.urlencode(values)
        full_url = '{0}{1}'.format(url, data)
        req = urllib2.Request(full_url)
        req.add_header('Authorization', headers.get('Authorization'))
        resp = urllib2.urlopen(req)
        return resp.read()

    def save_tweets(self):
        """
        Saves the tweets returned from `fetch_tweets` method into a text file
        named `tweets.json`.
        """
        content = self.fetch_tweets()
        cont = json.loads(content)
        words = []
        for tweets in cont:
            words.append(tweets.get('text'))
        tweet_file = open('tweets.json', 'w')
        tweet_file.write(content)
        tweet_file.close()
        return words
        # re.sub('RT?\s@([a-zA-Z0-9_]+)', '', sen)
        # stripped = re.sub('\s'+word+'\s', ' ', stripped)
        # splitted = re.split('[ \s]+', stripped)

