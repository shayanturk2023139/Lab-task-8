class Author:
    def _init_(self, name):
        self.name = name

    def _str_(self):
        return f"Author: {self.name}"


class Post:
    def _init_(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def _str_(self):
        return f"{self.title} by {self.author.name} ({self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})\n{self.content}"


class Blog:
    def _init_(self, name):
        self.name = name
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def display_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found by {author.name}.")
        else:
            print(f"Posts by {author.name}:")
            for post in author_posts:
                print(post)

    def display_latest_posts(self, num_posts=5):
        if not self.posts:
            print("No posts available.")
        else:
            print(f"Latest {num_posts} posts:")
            sorted_posts = sorted(self.posts, key=lambda post: post.timestamp, reverse=True)
            for post in sorted_posts[:num_posts]:
                print(post)


# Example usage:
if _name_ == "_main_":
    author1 = Author("Alice")
    author2 = Author("Bob")

    blog = Blog("Tech Blog")

    post1 = Post("Introduction to Python", "Python is a versatile programming language.", author1)
    post2 = Post("Web Development Basics", "Learn the fundamentals of web development.", author2)
    post3 = Post("Data Science with Python", "Explore data science using Python.", author1)

    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)

    blog.display_posts_by_author(author1)

    blog.display_latest_posts()