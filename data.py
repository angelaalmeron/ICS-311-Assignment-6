# to use in own task, include this on top of the program -> "from data import User, Post, Comment"

# if there's no given time, use the current time
from datetime import datetime 

# --- Comment Data ---
class Comment:
    def __init__(self, author, content, timestamp=None):
        self.author = author # User object 
        self.content = content # text string the commenter wrote
        self.timestamp = timestamp or datetime.now() # if no time, then use current time (just in case)

# --- Post Data ---
class Post:
    def __init__(self, author, content, timestamp=None):
        self.author = author
        self.content = content
        self.timestamp = timestamp or datetime.now()
        self.comments = [] # to store comments on the post
        self.views = [] # to keep track of which users have viewed the post or when

    # who viewed the post and when
    def add_view(self, user, timestamp=None):
        self.views.append((user, timestamp or datetime.now()))

    # add a comment to the post
    def add_comment(self, comment):
        self.comments.append(comment)

# --- User Data ---
class User:
    def __init__(self, username, attributes=None):
        self.username = username # the consistent unique ID
        self.connections = [] # the directed connections to other users
        self.posts = [] # the posts made by this user
        self.viewed_posts = [] # the posts this user has viewed
        self.comments = [] # the comments made by this user
        self.attributes = attributes or {} # user attributes (e.g., age, gender, etc.)

    # to connect this user to another with specific relationship type (e.g., friend, follower, etc.)
    def connect_to(self, user, relationship_type):
        self.connections.append((relationship_type, user))

    # allow the user to write new post
    def post_content(self, content):
        post = Post(author=self, content=content) # create a new post
        self.posts.append(post) # add it to the user's list of posts
        return post # returns the new post

    # allow the user to view a post
    def view_post(self, post, timestamp=None):
        self.viewed_posts.append((post, timestamp or datetime.now())) # adds the post to the user's list of viewed posts
        post.add_view(self, timestamp) # updates the post's view list to include this user

    # allow the user to comment on a post
    def comment_on_post(self, post, content):
        comment = Comment(author=self, content=content) # create a new comment
        self.comments.append(comment) # add it to the user's list of comments
        post.add_comment(comment) # adds the comment to the post's list of comments
