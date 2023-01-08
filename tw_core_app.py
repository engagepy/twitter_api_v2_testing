import tweepy

try:
    import api_token
except:
    pass
import os

try:
    token= os.environ['BEARER_TOKEN']
except:
    token = api_token.BEARER_TOKEN

client = tweepy.Client(bearer_token=token)
#client_2 = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

query = ' ChatGPT -is:retweet -#eximbank -btc -eth -nft -crypto -donation -donating -donate lang:en'
response = tweepy.Paginator(
        client.search_recent_tweets, query=query, max_results=100, 
        tweet_fields=['created_at', 'lang'], 
        user_fields=['profile_image_url'], 
        expansions=['author_id']).flatten(limit=1000        )

counts = client.get_recent_tweets_count(query=query, granularity = 'day')

#case sensitive word check
word_check_1 = "potential"
word_check_2 = "google"
word_check_3 = "scary"
word_check_4 = "disruptor"
word_check_5 = "plagiarism"

#setting counters for ease of data relay
count = 0
word_count_1 = 0
word_count_2 = 0
word_count_3 = 0
word_count_4 = 0
word_count_5 = 0

for tweet in response:        
    count+=1
    print(count)
    lowercase_tweet = tweet.text.lower()
    #enter the word you wish to count occurence of in each tweet !
    word_1_alert = lowercase_tweet.count(word_check_1.lower())
    word_2_alert = lowercase_tweet.count(word_check_2.lower())
    word_3_alert = lowercase_tweet.count(word_check_3.lower())
    word_4_alert = lowercase_tweet.count(word_check_4.lower())
    word_5_alert = lowercase_tweet.count(word_check_5.lower())

    #print(f" '--->>>{word_check_1}' repeated {word_1_alert} times")
    #print(f" '--->>>{word_check_2}' repeated {word_2_alert} times")
    word_count_1 += word_1_alert
    word_count_2 += word_2_alert
    word_count_3 += word_3_alert
    word_count_4 += word_4_alert
    word_count_5 += word_5_alert    
    print(tweet.text)
    print(tweet.author_id)
    print("\n")
    print("\n")

print(f"Research Query: {query.split()[0]}")
print("")
print(f"Tweets Scanned {count}")
print("")
print(f"""
        \n'{word_check_1.lower()}' count is {word_count_1} 
        \n'{word_check_2.lower()}' count is {word_count_2} 
        \n'{word_check_3.lower()}' count is {word_count_3}
        \n'{word_check_4.lower()}' count is {word_count_4} 
        \n'{word_check_5.lower()}' count is {word_count_5}
        """)
print("")
print("<<<<<<<<------------ TWEET VOLUME IN PAST 7 DAYS")
tweet_count_total = 0
for tweet in counts.data:
    print(f"Tweet Count {tweet['tweet_count']} Start Date: {tweet['start'][:10]} End Date: {tweet['end'][:10]}")
    tweet_count_total += tweet['tweet_count']
print(f"Total Tweets = {tweet_count_total}")
