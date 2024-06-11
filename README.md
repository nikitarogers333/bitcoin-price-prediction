# Bitcoin Price Analysis

This repository contains a comprehensive data analysis project on Bitcoin prices. The project includes data collection, preprocessing, and analysis using SQL and Snowflake. Key analyses include daily averages, moving averages, volatility, trend identification, and correlation analysis. The insights gained from this project can inform investment strategies, risk management, and further research into cryptocurrency markets.

## Contents

- **Notebooks**:
  - `snowflake_bitcoin.ipynb`: Jupyter notebook containing all SQL queries, data analysis, and visualizations.
  
- **Data**:
  - `bitcoin_data.csv`: Dataset containing historical Bitcoin data used for analysis.

- **SQL Queries**:
  - `sql_queries.sql`: File containing all SQL queries used in the project.

- **Documentation**:
  - `README.md`: Detailed documentation of the project including introduction, methodology, key insights, and how to run the analysis.
  - `Medium_Article.md`: Markdown file of the published Medium article.

- **Python Scripts**:
  - `data_collection.py`: Script to collect data from the CoinGecko API.

- **Additional Items**:
  - **Medium Article**: A comprehensive Medium article detailing the project, its methodology, and findings.
  - **Presentation**: `presentation.pdf`: Slides summarizing the project's key insights and findings.

## Project Overview

### Introduction
Predicting the price of Bitcoin can be challenging due to its volatility and the complex factors influencing its value. In this project, we analyze historical Bitcoin data to uncover trends, calculate key metrics, and understand the relationships between different variables.

### Data Collection
We collected historical Bitcoin data using the CoinGecko API, which provides comprehensive information about cryptocurrency prices, volumes, and market caps.

### Data Loading
The data was preprocessed and loaded into a Snowflake database for analysis. The following SQL queries were used to analyze the data.

### Data Analysis
1. **Preview of Data**: An overview of the structure and content of the data.
2. **Daily Averages**: Calculating daily average Bitcoin prices, volumes, and market caps.
3. **7-Day Moving Average**: Calculating the average price over a rolling 7-day window.
4. **Volatility**: Measuring the standard deviation of the price over the past 7 days.
5. **Identifying Trends**: Identifying upward and downward trends in the Bitcoin price.
6. **Correlation Analysis**: Examining the relationship between the Bitcoin price and other variables such as volume and market cap.

### Key Insights
- The average price of Bitcoin showed significant growth from July to December 2023, peaking at around $72,130.55 on March 12, 2024.
- The 7-day moving average helps smooth out daily fluctuations, providing a clearer view of the long-term trend.
- Significant peaks and troughs in price, volume, and market cap were observed, highlighting periods of increased market activity.

## How to Run the Analysis
1. Clone the repository.
2. Ensure you have the required dependencies installed.
3. Use the Jupyter notebook `snowflake_bitcoin.ipynb` to run the analysis.
4. Refer to `sql_queries.sql` for all SQL queries used in the project.
5. For data collection, run `data_collection.py`.

## Conclusion
These analyses provide a comprehensive understanding of the Bitcoin market over the analyzed period. By examining daily averages, moving averages, volatility, trends, and correlations, we gain valuable insights into price behavior, market activity, and potential risks. These findings can inform investment strategies, risk management, and further research into cryptocurrency markets.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
