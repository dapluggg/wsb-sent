# %%
import pickle
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# Load Results
pickle_file = open("results.pkl", "rb")
objects = []
while True:
    try:
        objects.append(pickle.load(pickle_file))
    except EOFError:
        break
pickle_file.close()
# %%
named_ents = objects[0]['Named_Entities']
# Get the entities
entlist = [ent.ents for ent in named_ents]
# Break open the tuples for word cloud  
wclist = [item for t in entlist for item in t]
# %%
from wordcloud import WordCloud, STOPWORDS

wc = WordCloud(background_color="white", max_words=2000, contour_width=3, contour_color='steelblue')
wc.generate(wclist)

# %%
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # return string  
    return (str1.join(s))

text = listToString(str(wclist))
# tmp = (listToString([str(itm) for itm in wclist]) 
# %%
tmp
# %%
wc = WordCloud()
# %%
wc = WordCloud(background_color="white", max_words=2000, contour_width=3, contour_color='steelblue', collocations=False, width=1600, height=800)
wc.generate(tmp)
wc.to_file("wsb_wordcloud.png")
# %%
sentiment = objects[0]['Sentiments']
neg = [sent['neg'] for sent in sentiment]
pos = [sent['pos'] for sent in sentiment]
dates = reddit['timestamp']
sentimentdf = pd.DataFrame({'neg': neg, 'pos': pos, 'dates': dates})
sentimentdf['dates'] = sentimentdf['dates'].dt.date
negative_sent = sentimentdf.groupby(sentimentdf['dates'])['neg'].agg(['mean'])
negative_sent['dates'] = negative_sent.index
positive_sent = sentimentdf.groupby(sentimentdf['dates'])['pos'].agg(['mean'])
positive_sent['dates'] = positive_sent.index
#ax = sns.lineplot(x=positive_sent.index, y=positive_sent)
# %%
#negative_sent
ax = sns.lineplot(x=negative_sent['dates'], y=negative_sent['mean'])
ax = sns.lineplot(x=positive_sent['dates'], y=positive_sent['mean'])
ax.set(ylabel='Average VADER Sentiment', title='r/wallstreetbets: VADER Sentiment Analysis',
xlabel='Date')
ax.legend(['Negative Sentiment', 'Positive Sentiment'])
# %%
