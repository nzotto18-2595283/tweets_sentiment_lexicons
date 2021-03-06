"""
Nicola Zotto

Step 3: "Use TweetTokenizer package to tokenize the tweet messages and remove all links and special characters, and draw histogram of the most common terms, excluding stop-words."
"""
from nltk.tokenize import TweetTokenizer 
from nltk.corpus import stopwords

import draw_bar_plot as plt

def tokenizer_term_to_count(tweets,case_sensityvity=False, reduced_length=True, delete_handles=True):
    """
    Tokenizes a collection of tweets and counts the appearences of each token.
    :param tweets: a list (or any iterable) containing the tweets to be tokenized and analysed
    :param case_sensityvity: if False, the tokenizer is downcases all words except for emoticons (default to False) 
    :param reduced_length: if True, the tokenizer normalizes repeated characters to only 3 characters (default to True)
    :param delete_handles: if True, the tokenizer removes user handles such as "@Erme" (default to True)
    :return: a dictionary with a term as key and the number of appearances of the term as value

    examples:
    >>> tweets = ["David Bowey is dead !!!!!!!!!!!!", "@A_Name LOOOOng live David bowey !"]
    >>> tokenizer_term_to_count(tweets) =={"david":2, "bowey": 2, "is":1, "dead":1, "!":4, "looong":1, "live":1}
    True
    """
    tknzr = TweetTokenizer(preserve_case=case_sensityvity, strip_handles=delete_handles, reduce_len=reduced_length)
    res = dict()
    temp = []
    for tw in tweets:
        temp = tknzr.tokenize(tw)
        filtered_tweets = [w for w in temp if w not in stopwords.words('english')]
        for token in filtered_tweets:
            if token in res.keys():
                res[token] += 1
            else:
                res[token] = 1
    return res


def main():
    tweets = ["David Bowey is dead !!!!!!!!!!!!", "@A_Name LOOOOng live David bowey !"]
    d=tokenizer_term_to_count(tweets)
    for i in d:
        print (i, d[i])

    plt.draw_bar_plot(d, "Term frequency of Tweets", "Terms", "Number of appearences")

if __name__ == "__main__": main()
