import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the titles of all posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")  

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])  

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves selected data to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # Prepare data to be written to CSV
        data_to_write = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Writing to CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_to_write)