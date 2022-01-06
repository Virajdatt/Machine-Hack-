import os
import sys
cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")

from src.multi_label import plot_label_count,plot_multi_label
import pandas as pd


data = pd.read_csv('/Users/virajdatt/Desktop/github/public/Machine-Hack-/uHack-Sentiments/data/train.csv')
# Following are the labels in the dataset
mlabels = ['Components', 'Delivery and Customer Support',
       'Design and Aesthetics', 'Dimensions', 'Features', 'Functionality',
       'Installation', 'Material', 'Price', 'Quality', 'Usability']

#plot_label_count(data,mlabels)
plot_multi_label(data,mlabels)

