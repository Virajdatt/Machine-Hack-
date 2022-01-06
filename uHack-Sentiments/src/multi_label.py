import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_label_count(df: pd.DataFrame, mlabels: list)-> None:
    """
    This function accepts the dataframe that contains the data with
    multiple lables which are passed as a list and produces a bar plot
    which contains information about the count of each label

    Args:
        df (pd.DataFrame): dataframe with the data
        mlabels (list): list of lables that the df contains
    
    Example:
        df = pd.read_csv('train.csv')
        mlabels = ['Components', 'Delivery and Customer Support',]
        plot_label_count(df,mlabels)

    """    
    categories = list(df[mlabels].columns.values)
    sns.set(font_scale = 2)
    plt.figure(figsize=(15,8))
    ax= sns.barplot(categories, df[mlabels].sum().values)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    plt.title("Reviews in each category", fontsize=24)
    plt.ylabel('Number of Reviews', fontsize=18)
    plt.xlabel('Review Type ', fontsize=18)
    #adding the text labels
    rects = ax.patches
    labels = df[mlabels].sum().values
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom', fontsize=18)
    plt.show()


def plot_multi_label(df: pd.DataFrame, mlabels: list)-> None:
    """
    This function accepts the dataframe that contains the data with
    multiple lables which are passed as a list  and produces a bar plot
    which contains information about how many times multiple labels are presented
    in a review

    Args:
        df (pd.DataFrame): dataframe with the data
        mlabels (list): list of lables that the df contains
    Example:
        df = pd.read_csv('train.csv')
        mlabels = ['Components', 'Delivery and Customer Support',]
        plot_multi_label(df,mlabels)
    """
    rowSums = df[mlabels].sum(axis=1)
    multiLabel_counts = rowSums.value_counts()
    multiLabel_counts = multiLabel_counts.iloc[1:]
    sns.set(font_scale = 2)
    plt.figure(figsize=(15,8))
    ax = sns.barplot(multiLabel_counts.index, multiLabel_counts.values)
    plt.title("Reviews having multiple labels ")
    plt.ylabel('Number of Reviews', fontsize=18)
    plt.xlabel('Number of Labels', fontsize=18)
    #adding the text labels
    rects = ax.patches
    labels = multiLabel_counts.values
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')
    plt.show()
