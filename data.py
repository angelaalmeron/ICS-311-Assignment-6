# This program is for all group members of the assignment to share.
# Thus, we all don't have to redefine the same classes in our own programs.

# To use in our own task, include this on top of the program -> "from data import User, Post, Comment"

# If there's no given time, use the current time.
from datetime import datetime 

# --- Comment Data ---
class Comment:
    def __init__(self, author, content, timestamp=None):
        self.author = author # A User object. 
        self.content = content # Text string the commenter wrote.
        self.timestamp = timestamp or datetime.now() # If there's no time, then use the current time.

# --- Post Data ---
class Post:
    def __init__(self, author, content, timestamp=None):
        self.author = author
        self.content = content
        self.timestamp = timestamp or datetime.now()
        self.comments = [] # To store comments on the post.
        self.views = [] # To keep track of which users have viewed the post or when.

    # Who viewed the post and when.
    def add_view(self, user, timestamp=None):
        self.views.append((user, timestamp or datetime.now()))

    # Add a comment to the post.
    def add_comment(self, comment):
        self.comments.append(comment)

# --- User Data ---
class User:
    def __init__(self, username, attributes=None):
        self.username = username # The consistent unique ID.
        self.connections = [] # The directed connections to other users.
        self.posts = [] # The posts made by this user.
        self.viewed_posts = [] # The posts this user has viewed.
        self.comments = [] # The comments made by this user.
        self.attributes = attributes or {} # The user attributes (e.g., age, gender, etc.).

    # To connect this user to another with specific relationship type (e.g., friend, follower, etc.).
    def connect_to(self, user, relationship_type):
        self.connections.append((relationship_type, user))

    # Allow the user to write new post.
    def post_content(self, content):
        post = Post(author=self, content=content) # Create a new post.
        self.posts.append(post) # Add it to the user's list of posts.
        return post # Rreturns the new post.

    # Allow the user to view a post.
    def view_post(self, post, timestamp=None):
        self.viewed_posts.append((post, timestamp or datetime.now())) # Adds the post to the user's list of viewed posts.
        post.add_view(self, timestamp) # Updates the post's view list to include this user.

    # Allow the user to comment on a post.
    def comment_on_post(self, post, content):
        comment = Comment(author=self, content=content) # Create a new comment.
        self.comments.append(comment) # Add it to the user's list of comments.
        post.add_comment(comment) # Adds the comment to the post's list of comments.
