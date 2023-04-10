from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def fetch_data():
    url= 'https://www.businesstoday.in/latest/trends'
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    news = []

    container = soup.find_all('div', {'class':'widget-listing-content-section'})
    
    for item in container:
        data = {
            'date':item.span.text[10:],
            'link':item.h2.a['href'],
            'title':item.h2.a['title'],
            'desc':item.p.text
            }
        news.append(data)

    return render_template("index.html", News=news)

    