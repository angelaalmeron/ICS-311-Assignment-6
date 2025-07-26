# --- Analysis Task 3 ---
# author: Angela Joy Almeron
# instructor: Professor David Brook Conner
# date: 2025-07-25

# Import shared structure from data.py
from data import User, Post, Comment

# Import word cloud & other necessary utilities
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

# --- Sample data setup (for testing purposes) ---
user1 = User("angela", {"age": 20, "gender": "F", "region": "West"})
user2 = User("jord", {"age": 25, "gender": "M", "region": "West"})
user3 = User("arisa", {"age": 20, "gender": "F", "region": "East"})
user4 = User("theressa", {"age": 21, "gender": "F", "region": "West"})
user5 = User("kolby", {"age": 26, "gender": "M", "region": "East"})

post1 = user1.post_content("I really love coffee and coding every morning.")
post2 = user2.post_content("Coffee is okay, but I prefer tea sometimes.")
post3 = user3.post_content("Tea or coffee? I can't really decide. But I do love matcha!")
post4 = user4.post_content("Coding is fun, especially with coffee!")
post5 = user5.post_content("I enjoy matcha more than tea or coffee.")

# This is placing all users in a list for easier processing later.
users = [user1, user2, user3, user4, user5]

# --- Functions for filtering and processing ---

# To grab posts only from users with a specific attribute.
def filter_posts_by_attribute(users, attr_key, attr_val):
    return [post for user in users if user.attributes.get(attr_key) == attr_val for post in user.posts]

# To filter posts based on keywords, either including or excluding them.
def filter_posts_by_keyword(posts, include_keywords=None, exclude_keywords=None):
    include_keywords = [kw.lower() for kw in include_keywords] if include_keywords else [] # Words to include.
    exclude_keywords = [kw.lower() for kw in exclude_keywords] if exclude_keywords else [] # Words to exclude.

    # Function to check if a post passes the keyword filters.
    def post_passes(post):
        text = post.content.lower() # Convert post content to lowercase for case-insensitive comparison.

        # Check if the post contains the required keywords and does not contain excluded keywords.
        if include_keywords and not any(kw in text for kw in include_keywords): 
            return False
        if exclude_keywords and any(kw in text for kw in exclude_keywords):
            return False
        return True
    
    # Return only posts that pass the keyword filters.
    return [post for post in posts if post_passes(post)]

# To analyze a list of posts and returns how frequently each word appears.
def generate_word_frequencies(posts):
    word_count = Counter() # Initialize a counter to hold word frequencies.
    for post in posts: # Iterate through each post.
        words = re.findall(r'\b\w+\b', post.content.lower()) # Extract words, ignoring case and punctuation.
        word_count.update(words) # Update the counter with the words from the post.
    return word_count 

# To create a word cloud from the word frequencies.
def create_word_cloud(word_frequencies):
    wc = WordCloud(width=500, height=300, background_color='white') # Initialize the WordCloud object with desired dimensions and background color.
    wc.generate_from_frequencies(word_frequencies) # Generate the word cloud from the frequencies.

    # Display the word cloud using matplotlib.
    plt.figure(figsize=(10, 5)) 
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

# --- Main Execution ---

# For analysts to customize filters:
filter_key = "gender"
filter_value = "F"
include_words = ["coffee"]
exclude_words = ["matcha"]

# Step 1: Filter posts by user attribute.
filtered_posts = filter_posts_by_attribute(users, filter_key, filter_value)

# Step 2: Filter posts by keywords.
filtered_posts = filter_posts_by_keyword(filtered_posts, include_keywords=include_words, exclude_keywords=exclude_words)

# Step 3: Generate word frequencies from the filtered posts & display the word cloud.
frequencies = generate_word_frequencies(filtered_posts)
create_word_cloud(frequencies)
