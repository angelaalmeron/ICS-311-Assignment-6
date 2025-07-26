# --- Analysis Task 5 ---
# author: Brandon Nguyen
# instructor: Professor David Brook Conner
# date: 2025-07-24

from data import User, Post, Comment
from typing import List, Dict, Set
from datetime import datetime

def analyze_referenced_posts(users: List[User], include_references: bool = False, 
                          keywords: Set[str] = None, attributes: Dict[str, str] = None) -> List[Dict]:
    """
    Analyze posts with optional reference inclusion, keyword, and attribute filters.
    Returns list of dicts with post details and metrics.
    """
    result = []
    
    # Filter users by attributes
    valid_users = {u.username for u in users if not attributes or 
                  all(u.attributes.get(k) == v for k, v in attributes.items())}
    
    for user in users:
        if user.username not in valid_users:
            continue
            
        for post in user.posts:
            # Keyword filter
            if keywords and not any(kw.lower() in post.content.lower() for kw in keywords):
                continue
                
            # Calculate metrics
            views = len(post.views)
            comments = len(post.comments)
            
            # Include referenced posts if specified
            if include_references:
                for ref_id in post.references:
                    ref_post = next((p for u in users for p in u.posts if p.id == ref_id), None)
                    if ref_post and ref_post.author in valid_users:
                        views += len(ref_post.views)
                        comments += len(ref_post.comments)
            
            result.append({
                'post_id': post.id,
                'author': user.username,
                'content': post.content,
                'views': views,
                'comments': comments,
                'timestamp': post.timestamp
            })
    
    return result

# --- Sample Data for Testing ---
if __name__ == "__main__":
    # Create users
    user1 = User("alice", {"gender": "F", "region": "West"})
    user2 = User("bob", {"gender": "M", "region": "West"})
    
    # Create posts
    t1 = datetime(2025, 7, 25, 10, 0)
    t2 = datetime(2025, 7, 25, 11, 0)
    post1 = user1.post_content("I love coding!", t1)
    post2 = user2.post_content("Check this code!", t2, references=[post1.id])
    
    # Simulate views and comments
    for _ in range(5):
        post1.add_view(user2)
    post1.add_comment(Comment(user2, "Nice!"))
    
    for _ in range(3):
        post2.add_view(user1)
    post2.add_comment(Comment(user1, "Cool!"))
    
    # Test analysis
    report = analyze_referenced_posts(
        [user1, user2],
        include_references=True,
        keywords={"code"},
        attributes={"gender": "F"}
    )
    
    print("Post Analysis Report:")
    for idx, item in enumerate(report, start=1):
        print(f"{idx}. Author: {item['author']} | Content: '{item['content']}' | "
              f"Views: {item['views']} | Comments: {item['comments']}")
