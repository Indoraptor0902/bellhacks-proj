import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

class HeartAttackPredictor:
    def __init__(self):
        self.df = pd.read_csv('heart-attack-risk-analysis/train.csv')
        self.zero_not_accepted = ['Age', 'Cholesterol', 'Blood Pressure', 'Heart Rate', 'BMI', 'Triglycerides']
    
    def setup_df(self):
        self.df = self.df.drop(columns=['Heart Attack Risk', 'Country', 'Continent', 'Hemisphere', 'Patient ID', 'Family History'])
        self.df['Sex'] = self.df['Sex'].map({'Female': 0, 'Male': 1})
        self.df['Diet'] = self.df['Diet'].map({'Unhealthy': 0, 'Average': 0.5, 'Healthy': 1})

        for column in self.zero_not_accepted:
            self.df[column] = self.df[column].replace(0, np.nan)
            mean = int(self.df[column].mean(skipna=True))
            self.df[column] = self.df[column].replace(np.nan, mean)
        
        self.X = self.df.iloc[:, 0:len(self.df.columns) - 1]
        self.y = self.df.iloc[:, len(self.df.columns) - 1]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)

        self.sc_X = StandardScaler()
        self.X_train = self.sc_X.fit_transform(self.X_train)
        self.X_test = self.sc_X.transform(self.X_test)
    
    def train(self):
        self.classifier = KNeighborsClassifier(n_neighbors=11, p=2, metric='euclidean')
        self.classifier.fit(self.X_train, self.y_train)

        self.y_pred = self.classifier.predict(self.X_test)