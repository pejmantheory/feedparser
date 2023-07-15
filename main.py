from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def home():
    rss_feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"  # replace with your RSS feed URL
    entries = fetch_rss_feed(rss_feed_url)
    return render_template('index.html', entries=entries)

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

