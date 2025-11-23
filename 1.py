import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

train_df = pandas.read_csv('train.csv')
test_df = pandas.read_csv('test.csv')
sample_sub = pandas.read_csv('sample_submission.csv')

X_train = train_df.drop(['id', 'smoking'], axis=1)
y_train = train_df['smoking']

X_test = test_df.drop('id', axis=1)

X_train = X_train.fillna(X_train.mean())
X_test = X_test.fillna(X_test.mean())

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_tr, X_val, y_tr, y_val = train_test_split(
    X_train_scaled,
    y_train,
    test_size=0.2,
    random_state=42,
    stratify=y_train
)