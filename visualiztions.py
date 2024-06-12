import matplotlib.pyplot as plt

# Plot historical prices
plt.figure(figsize=(14, 7))
plt.plot(bitcoin_data_preprocessed['timestamp'], bitcoin_data_preprocessed['price'], label='Price')
plt.title('Bitcoin Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Plot trading volume
plt.figure(figsize=(14, 7))
plt.plot(bitcoin_data_preprocessed['timestamp'], bitcoin_data_preprocessed['volume'], label='Volume', color='orange')
plt.title('Bitcoin Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# Plot market capitalization
plt.figure(figsize=(14, 7))
plt.plot(bitcoin_data_preprocessed['timestamp'], bitcoin_data_preprocessed['market_cap'], label='Market Cap', color='green')
plt.title('Bitcoin Market Capitalization Over Time')
plt.xlabel('Date')
plt.ylabel('Market Cap (USD)')
plt.legend()
plt.show()

# Plot price change
plt.figure(figsize=(14, 7))
plt.plot(bitcoin_data_preprocessed['timestamp'], bitcoin_data_preprocessed['price_change'], label='Price Change', color='red')
plt.title('Bitcoin Price Change Over Time')
plt.xlabel('Date')
plt.ylabel('Price Change (%)')
plt.legend()
plt.show()

# Calculate and display basic statistics
print("Basic Statistics:")
print(bitcoin_data_preprocessed[['price', 'volume', 'market_cap']].describe())

# Correlation matrix
correlation_matrix = bitcoin_data_preprocessed[['price', 'volume', 'market_cap', 'price_change', 'volume_change', 'market_cap_change']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Visualize the correlation matrix
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
