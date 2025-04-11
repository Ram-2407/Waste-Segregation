# train_model.py
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import pandas as pd

# Load dummy dataset
df = pd.read_csv('waste_dataset.csv')
X = df.drop('label', axis=1)
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model training
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save model
joblib.dump(clf, 'waste_model.pkl')

# Print classification report
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
