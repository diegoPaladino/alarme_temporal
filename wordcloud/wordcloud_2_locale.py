# importing libraries
import tweepy as tw
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt



# from wordcloud import






# codding

consumer_key = 'MRJ6x2T53GY7pGkU30MSqHdzs'
consumer_secret = 'aX1US3g1z356nSZvswDYT2OHSs4nJyJ8Fi1xGithIirSjAjgKU'
access_token = '3221258481-cX1wtuIwIcGif3fvKTDIOcCaYv7h7kUQJ2WHyHG'
access_token_secret = 'fd7u2eTzzU8B3P7f6WSZYB4dKnm1fqVpKHIQfevfe6x8C'

# CONTEUDO DA 1ª PARTE DO TUTORIAL DE WORDCLOUD
autorizacao = tw.OAuthHandler(consumer_key, consumer_secret)
autorizacao.set_access_token(access_token, access_token_secret)
api = tw.API(autorizacao)


places = api.geo_search(query="BRAZIL",granularity="country")
place_id = places[0].id
tweets = api.search(q="place:%s" % place_id)


meus_tweets = api.geo_id()