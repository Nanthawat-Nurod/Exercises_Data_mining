import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

data = pd.read_excel('Sunburned.xlsx')

X = data.drop('Sunburned', axis=1)
y = data['Sunburned']

le_dict = {}
for column in X.columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    le_dict[column] = le

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred_tree = clf.predict(X_test)
accuracy_tree = accuracy_score(y_test, y_pred_tree)
print(f"ความแม่นยำของ Decision Tree: {accuracy_tree:.2f}")

nb = GaussianNB()
nb.fit(X_train, y_train)

y_pred_nb = nb.predict(X_test)

accuracy_nb = accuracy_score(y_test, y_pred_nb)
print(f"ความแม่นยำของ Naïve Bayes: {accuracy_nb:.2f}")

print("\nเปรียบเทียบผลลัพธ์:")
print(f"ความแม่นยำของ Decision Tree: {accuracy_tree:.2f}")
print(f"ความแม่นยำของ Naïve Bayes: {accuracy_nb:.2f}")
