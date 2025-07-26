# --- Analysis Task 4 ---
# author: Angelo Rosal
# instructor: Professor David Brook Conner
# date: 2025-07-25

from data import User, Post, Comment
from datetime import datetime, timedelta

def trending_posts(users, keyword = None, attribute_filter = None, top_k = 10, alpha = 1, beta = 1):

    trending_list = []

    for user in users:
        # Apply user attribute filter
        if attribute_filter:
            if not all(user.attributes.get(k) == v for k, v in attribute_filter.items()):
                continue
        
        for post in user.posts:
            # Apply keyword filter
            if keyword and keyword.lower() not in post.content.lower():
                continue

            # Calculate engagement and time
            views_count = len(post.views)
            comments_count = len(post.comments)
            engagement = (alpha * views_count) + (beta * comments_count)

            time_elapsed_hours = (datetime.now() - post.timestamp).total_seconds() / 3600
            trending_score = engagement / time_elapsed_hours if time_elapsed_hours > 0 else engagement

            trending_list.append((post, trending_score))

    # Sort by trending score
    trending_list.sort(key = lambda x: x[1], reverse = True)

    return trending_list[:top_k]

# --- Sample Data for Testing ---
if __name__ == "__main__":
    # Create users
    user1 = User("Alice", {"gender": "female", "location": "Hawaii"})
    user2 = User("Bob", {"gender": "male", "location": "California"})

    # Create posts
    post1 = user1.post_content("Aloha from Hawaii!")
    post1.timestamp = datatime.now() - timedelta(hours = 2) # posted 2 hours ago
    post2 = user2.post_content("Breaking news: Something big happend")
    post2.timestamp = datetime.now() - timedelta(hours = 5)

    # Simulate views and comments
    for _ in range(10):
        post1.add_view(user2)
    for _ in range(2):
        post1.add_comment(Comment(user2, "Awsome!"))

    for _ in range(20):
        post2.add_view(user1)
    for _ in range(1):
        post2.add_comment(Comment(user1, "Wow!"))

    # Test trending post function
    report = trending_posts([user1, user2], keyword = None, attribue_filter = {"location": "Hawaii"})

    print("Trending Post Report:")
    for idx, (post, score) in enumerate(repost, start = 1):
        print(f"{idx}. Auther: {post.author.username} | Content: '{post.content}' | Score: {score:.2f}")
