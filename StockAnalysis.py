import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt  

# Using the Ticker module to create an object to access functions for extracting data
apple = yf.Ticker("AAPL")

# Using the attribute info to extract information about the stock as a Python dictionary
apple_info = apple.info

# Save the stock information to a JSON file
with open('apple_info.json', 'w') as json_file:
    json.dump(apple_info, json_file, indent=4)

# Print the type of data variable
# print("Type:", type(apple_info))

# Extracting Share Price
apple_share_price_data = apple.history(period="max")

apple_share_price_data.head()

# Reset the index of DataFrame with the reset_index function
# Set the inplace parameter to True so the change takes place to the DataFrame itself
apple_share_price_data.reset_index(inplace=True)

# Plot the Open price against the Date
apple_share_price_data.plot(x="Date", y="Open")

# Extracting dividends
apple_dividends = apple.dividends

# Plot the dividends over time
apple_dividends.plot()

# Display the plots
plt.show()
