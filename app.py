from flask import Flask, render_template
import requests
import pandas as pd
import plotly.express as px
import json
import plotly
from datetime import datetime, timedelta

app = Flask(__name__)

def get_crypto_data():
    """Fetches a few cryptocurrency prices from the CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,cardano",
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching simple data: {e}")
        return None

def get_historical_data(coin_id, days='30'):
    """Fetches historical price data for a given cryptocurrency."""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['prices']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical data for {coin_id}: {e}")
        return []

@app.route('/')
def home():
    crypto_data = get_crypto_data()
    
    historical_dfs = []
    if crypto_data:
        for coin_id in crypto_data.keys():
            prices = get_historical_data(coin_id)
            if prices:
                df = pd.DataFrame(prices, columns=['timestamp', 'price'])
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                df['crypto'] = coin_id
                historical_dfs.append(df)

    if historical_dfs:
        historical_df = pd.concat(historical_dfs)
        
        # Create a Plotly line graph
        fig = px.line(
            historical_df,
            x='timestamp',
            y='price',
            color='crypto',
            title='Historical Price (Last 30 Days)',
            labels={'timestamp': 'Date', 'price': 'Price in USD', 'crypto': 'Cryptocurrency'}
        )
        
        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    else:
        graph_json = None

    return render_template('index.html', crypto_data=crypto_data, graph_json=graph_json)

if __name__ == '__main__':
    app.run(debug=True)