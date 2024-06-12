import requests
import pandas as pd
from datetime import datetime
import numpy as np

def fetch_historical_data(crypto_id, vs_currency, days):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency={vs_currency}&days={days}"
    response = requests.get(url)
    data = response.json()
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Fetch 1 year of Bitcoin data
bitcoin_data = fetch_historical_data('bitcoin', 'usd', 365)
print(bitcoin_data.head())



import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_historical_data(crypto_id='bitcoin', vs_currency='usd', days=365):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency={vs_currency}&days={days}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prices = data['prices']
        volumes = data['total_volumes']
        market_caps = data['market_caps']
        
        df_prices = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df_volumes = pd.DataFrame(volumes, columns=['timestamp', 'volume'])
        df_market_caps = pd.DataFrame(market_caps, columns=['timestamp', 'market_cap'])
        
        df_prices['timestamp'] = pd.to_datetime(df_prices['timestamp'], unit='ms')
        df_volumes['timestamp'] = pd.to_datetime(df_volumes['timestamp'], unit='ms')
        df_market_caps['timestamp'] = pd.to_datetime(df_market_caps['timestamp'], unit='ms')
        
        df = pd.merge(df_prices, df_volumes, on='timestamp')
        df = pd.merge(df, df_market_caps, on='timestamp')
        
        return df
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def preprocess_data(df):
    # Handle missing values
    df = df.dropna()
    
    # Ensure the data is sorted by timestamp
    df = df.sort_values(by='timestamp')
    
    # Reset the index
    df = df.reset_index(drop=True)
    
    # Calculate additional features
    df['price_change'] = df['price'].pct_change()
    df['volume_change'] = df['volume'].pct_change()
    df['market_cap_change'] = df['market_cap'].pct_change()
    
    # Fill NaN values resulting from pct_change()
    df = df.fillna(0)
    
    return df

# Fetch 1 year of Bitcoin data
bitcoin_data = fetch_historical_data('bitcoin', 'usd', 365)
if bitcoin_data is not None:
    # Preprocess the fetched data
    bitcoin_data_preprocessed = preprocess_data(bitcoin_data)
    print(bitcoin_data_preprocessed.head())
else:
    print("No data fetched.")




# Moving averages
bitcoin_data_preprocessed['MA7'] = bitcoin_data_preprocessed['price'].rolling(window=7).mean()
bitcoin_data_preprocessed['MA30'] = bitcoin_data_preprocessed['price'].rolling(window=30).mean()

# Lagged features
bitcoin_data_preprocessed['price_lag1'] = bitcoin_data_preprocessed['price'].shift(1)
bitcoin_data_preprocessed['price_lag7'] = bitcoin_data_preprocessed['price'].shift(7)

# Volatility
bitcoin_data_preprocessed['volatility'] = bitcoin_data_preprocessed['price'].rolling(window=7).std()

# Drop NA values created by rolling and shifting
bitcoin_data_preprocessed = bitcoin_data_preprocessed.dropna()

print(bitcoin_data_preprocessed.head())

# Save to a new CSV file for further use
bitcoin_data_preprocessed.to_csv('bitcoin_data_preprocessed_with_features.csv', index=False)