import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

def fetch_post():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\nPost Details")
        print("------------")
        print(f"User ID : {data['userId']}")
        print(f"Post ID : {data['id']}")
        print(f"Title   : {data['title']}")
        print(f"Body    : {data['body']}\n")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    fetch_post()
