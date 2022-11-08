"""Twitter."""
import re


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fasteyst growing tweet.
    """
    result = []
    for i in tweets:
        number = (i.retweets / i.time)
        if number not in result:
            result.append(number)
    max_number = result.index(max(result))
    return tweets[max_number]


def sort_by_popularity(tweets: list,) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.
    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    result = []
    for i in tweets:
        result.insert(0, i)
    sorted_list = sorted(sorted(result, key=lambda x: x.time), key=lambda x: x.retweets, reverse=True)
    return sorted_list


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    result = []
    for i in tweets:
        if hashtag in i.content:
            result.insert(0, i)
    return result


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularit is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    all_retweets = []
    result = []
    for x in tweets:
        result.extend(re.findall(r'#\w+', x.content))
        number_of_hashtags = x.content.count("#")
        retweet_list = [x.retweets] * number_of_hashtags
        all_retweets.append(retweet_list)
    flat_list = [item for sublist in all_retweets for item in sublist]
    my_dict = {}
    for s, t in zip(result, flat_list):
        my_dict[s] = my_dict.get(s, 0) + t
    my_dict = {val[0]: val[1] for val in sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))}
    return list(my_dict.keys())


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart #Pelmeen", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweet4 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #SUS #sos", 2192, 220803)
    tweets = [tweet1, tweet2, tweet3, tweet4]

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"
    print(sorted_hashtags[1])
    print(sorted_hashtags[2])
    print(sorted_hashtags[3])
    print(sorted_hashtags[4])
