import pandas as pd
data = pd.read_csv("./heart.csv")
data.dropna(inplace=True)

X = data.drop("AHD", axis=1)
y = data["AHD"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.3)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train,y_train)

import pickle
pickle.dump(clf, open('heart.pkl', 'wb'))