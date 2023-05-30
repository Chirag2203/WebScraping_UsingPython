import praw
# Add your own credentials here for the reddit API
reddit = praw.Reddit(
    client_id=" ",
    client_secret=" ",
    user_agent=" ",
    username=" ",
    password=" "
)
# The following code prints the top 5 posts in the subreddit Python
subreddit = reddit.subreddit("Python")

for post in subreddit.hot(limit=5):
    print(post.title)
    print()
    
# The following code prints the top 10 posts in the subreddit MachineLearning
print("The top 10 hottest posts in machine learning subreddit are->")
hot_posts = reddit.subreddit("MachineLearning").hot(limit=10)
for posts in hot_posts:
    print(posts.title)
print()

# The following code prints the top 10 posts in the subreddit climatechange
print("The top 10 hottest posts in climate change subreddit are->")
climate = reddit.subreddit("climatechange").top(limit=10)
for posts in climate:
    print(posts.title)
print()

# The following code prints the top 10 commentors in the subreddit damnthatsinteresting
print("The top 10 recent commentors in the subreddit damnthatsinteresting are->")
for comment in reddit.subreddit("Damnthatsinteresting").comments(limit=10):
    print(comment.author)