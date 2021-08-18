# FONTES
# https://www.linkedin.com/pulse/coletando-dados-do-twitter-utilizando-python-parte-1-mauro-ferreira/
# https://www.linkedin.com/pulse/coletando-dados-do-twitter-utilizando-python-parte-2-mauro-ferreira?originalSubdomain=pt



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
# meus_tweets = api.home_timeline()
# print(meus_tweets)

meus_tweets = api.search(q='stf',lang="pt")
# print(meus_tweets '\n')

# for twitters in meus_tweets:
#     print(twitters.created_at)
#     print(twitters.text,  '\n')


dados = []

for cada_tweett in meus_tweets:
    dados.append(cada_tweett.text)


df = pd.DataFrame()

colunas = [
    'tweet'
]
df = pd.DataFrame(dados,columns=colunas)
# print(df)

tweets = df['tweet']
todos_twitters = " ".join(s for s in tweets)

meu_stopwords = set(STOPWORDS)
meu_stopwords.update(['tá','farpa','pret','q','mais','à','Sr','ao','Val_705','anu','está','aí','vez','ser','prá','não','por','como','com','nos','já','até','dos','nas','tem','num','pe','pode','tal','diz','d','para','mas','eles','só','um','ele','nós','se','a','as','e','o','os','meu','meus','minha','minhas','seu','seus','sua','suas','tua','tuas','nossa','nossas','da','da','das','de','do','em','https','é','t','co','der','000011','esse','que','uma','na','ou','rt',])


minha_nuvem = WordCloud(stopwords=meu_stopwords, background_color='black', width=800, height=800,max_words=200).generate(todos_twitters)

# nesta parte, utiliza-se matplotlib, pyplot:
a = df.loc[3].to_string()
figura, eixo = plt.subplots(figsize=(8,8))
plt.imshow(minha_nuvem)
# plt.axis("off")
plt.show()
# print(plt.imshow(minha_nuvem))