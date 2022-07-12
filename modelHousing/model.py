import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


USAHousing = pd.read_csv('/Users/macbookprop/Documents/PERSONAL/Datasets/USA_Housing.csv')

X = USAHousing[['Avg. Area Income',
                'Avg. Area House Age',
                'Avg. Area Number of Rooms',
                'Avg. Area Number of Bedrooms',
                'Area Population'
                ]]
Y = USAHousing['Price']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=101)


lm = LinearRegression()
lm.fit(X_train,y_train)

pickle.dump(lm, open('model.pickle', 'wb'))