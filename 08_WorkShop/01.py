import requests
from flask import json
import json

URL = 'https://jsonplaceholder.typicode.com/user/1/posts'
response = requests.get(url=URL)
print(response.status_code)
print("*"*40)
print(response.text)
print("*"*40)
print(response.content)
print("*"*40)
print(response.json())

posts = response.json()
for i in range(0,3):
    post = posts[i]
    print(f'Post cu ID {post["id"]}, title {post["title"]}, user Id {post["userId"]}')
left_posts = len(posts) - 3
print(f'+{left_posts} more posts')
print("*"*40)

for post in posts[0:3]:
    post = posts[i]
    print(f'Post cu ID {post["id"]}, title {post["title"]}, user Id {post["userId"]}')
left_posts = len(posts) - 3
print(f'+{left_posts} more posts')
print("*" * 40)

for index, post in enumerate(posts):
    if index > 2:
        left_posts = len(posts) - 3
        print(f'+{left_posts} more posts')
        break
    print(f'Post cu ID {post["id"]}, title {post["title"]}, user Id {post["userId"]}')
