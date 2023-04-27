# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data (https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data)
df = pd.read_csv('../../../Data/BTC.csv')

print(df)

df.dropna(inplace=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['Open', 'High', 'Low']], df['Close'],
                                                    test_size=0.2, random_state=42)

# Create and train the linear regression model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = reg.predict(X_test)

# Print the mean squared error and r-squared score
print('Mean Squared Error: ', mean_squared_error(y_test, y_pred))
print('R-squared Score: ', r2_score(y_test, y_pred))

# Predict the future prices
future_prices = reg.predict(np.array([[8800, 8900, 8700]]))
print('Predicted Future Price: ', future_prices[0])
