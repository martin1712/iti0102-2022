"""Twitter."""


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
    pass


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    pass


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 6, 8)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 5, 8)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 5, 15)
    tweet4 = Tweet("@Google", "Its a prank. #heart", 1, 100)
    tweet5 = Tweet("@Patrick", "NOOOOOOOOOOOOOOOOOOO #heart", 2, 15)
    tweet6 = Tweet("@elonmusk", "Car is red, sun is moon #heart", 3, 100)
    tweets = [tweet1, tweet2, tweet3, tweet4, tweet5, tweet6]

    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@elonmusk"
    print(filtered_by_popularity[1].user)  # -> "@Patrick"
    print(filtered_by_popularity[2].user)  # -> "@CIA"
    print(filtered_by_popularity[3].user)  # -> "@realDonaldTrump"
    print(filtered_by_popularity[4].user)  # -> "@Google"
    print(filtered_by_popularity[5].user)  # -> "@Google"

    #filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    #print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    #print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    #sorted_hashtags = sort_hashtags_by_popularity(tweets)
    #print(sorted_hashtags[0])  # -> "#heart"