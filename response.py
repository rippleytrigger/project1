import requests
from flask import jsonify

res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "K3Vcr1bUtGxwuMZLAZFFA", "isbns": "9781632168146"})

print(jsonify({res.json()["books"][0]}))