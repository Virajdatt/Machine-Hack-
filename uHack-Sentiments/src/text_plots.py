import pandas as pd
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt


def word_cloud(df: pd.DataFrame, tclomun: str)-> None:

    #Building the word cloud for MOST used WORDS
    print("The MOST used WORDS:")
    wordcloud = WordCloud(width = 1000, height = 500,background_color='white').generate(' '.join(df[tclomun]))
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def word_frequency(df: pd.DataFrame, tclomun: str)-> None:

    rslt = pd.DataFrame(Counter(" ".join(df[tclomun]).split()).most_common(20),columns=['Word', 'Frequency']).set_index('Word')
    rslt.plot.bar(rot=0, figsize=(16,10), width=0.8)
    plt.show()