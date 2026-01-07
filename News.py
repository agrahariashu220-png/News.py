import requests

API_KEY = "a722c4322e7d4bc98cde17c7b215ec86"

url = f"https://newsapi.org/v2/everything?q=india&apiKey=a722c4322e7d4bc98cde17c7b215ec86"

response = requests.get("https://newsapi.org/v2/everything?q=india&apiKey=a722c4322e7d4bc98cde17c7b215ec86")

# check if request was successful
if response.status_code == 200 :
        data = response.json()
        articles = data["articles"]
        print("\nTop 10 News\n")
        for i, article in enumerate(articles[:10], start=1):
         print(f"\n{i}. {article['title']}")
         print(f"   Source: {article['source']['name']}")
         print(f"   Description: {article['description']}")
else:
    print("Error fetching news:", response.status_code)

