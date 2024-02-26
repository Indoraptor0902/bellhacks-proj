import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN

df = pd.read_csv('heart-attack-risk-analysis/train.csv')

labels = df['Heart Attack Risk']

df = df.drop(columns = ['Heart Attack Risk', 'Patient ID', 'Blood Pressure', 'Country', 'Continent', 'Hemisphere'])

df['Sex'] = df['Sex'].map({'Female': 0, 'Male': 1})
df['Diet'] = df['Diet'].map({'Unhealthy': 0, 'Average': 0.5, 'Healthy': 1})

normalized_df = (df - df.mean()) / df.std()

data = normalized_df.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(data, labels, train_size = 0.7, test_size = 0.2, random_state = 0, shuffle=True)

knn_grid = GridSearchCV( 
    KNN(), 
    {
        'n_neighbors': [2**N for N in range(1, 10)], 
        'weights': ['uniform', 'distance'], 
        'metric': ['minkowski', 'manhattan', 'chebyshev']
    }
)

knn_grid.fit(X_train, y_train)
best_knn = knn_grid.best_estimator_

train_acc = best_knn.score(X_train, y_train)
test_acc = best_knn.score(X_test, y_test)
print(f'Training Accuracy: {train_acc}, Test Accuracy: {test_acc}')

def results_to_csv(y_test):
    y_test = y_test.astype(int)
    df = pd.DataFrame({'Category': y_test})
    df.index += 1
    df.to_csv('results.csv', index_label='Id')

results_to_csv(y_test)