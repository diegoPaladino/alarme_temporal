# importing libraries
import tweepy as tw
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


# codding

consumer_key = 'MRJ6x2T53GY7pGkU30MSqHdzs'
consumer_secret = 'aX1US3g1z356nSZvswDYT2OHSs4nJyJ8Fi1xGithIirSjAjgKU'
access_token = '3221258481-cX1wtuIwIcGif3fvKTDIOcCaYv7h7kUQJ2WHyHG'
access_token_secret = 'fd7u2eTzzU8B3P7f6WSZYB4dKnm1fqVpKHIQfevfe6x8C'

# CONTEUDO DA 1ª PARTE DO TUTORIAL DE WORDCLOUD
autorizacao = tw.OAuthHandler(consumer_key, consumer_secret)
autorizacao.set_access_token(access_token, access_token_secret)
api = tw.API(autorizacao)

# capturando os dados

procura = tw.Cursor(api.search,lang="pt")


# tentativa de uso do matplotlib
# meu_stopwords = set(STOPWORDS)
# meu_stopwords.update(['a','as','e','o','os','meu','meus','minha','minhas','seu','seus','sua','suas','tua','tuas','nossa','nossas','da','da','das','de','do','em','https','é','t','co','der','000011','esse','que','uma','na','ou','rt',])
# minha_nuvem = WordCloud(stopwords=meu_stopwords, background_color='black', width=800, height=800).generate(meus_tweets)

a = tw.loc[3].to_string()
figura, eixo = plt.subplots(figsize=(8,8))
plt.imshow(procura)
# plt.axis("off")
plt.show()

# places = api.geo_search(query="BRAZIL",granularity="country")
# place_id = places[0].id
# tweets = api.search(q="place:%s" % place_id)


