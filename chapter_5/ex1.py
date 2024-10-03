import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np

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

def get_closest_feature_name(feature, value):
    le = le_dict[feature]
    transformed_values = le.transform(le.classes_)
    closest_index = np.argmin(np.abs(transformed_values - value))
    return le.classes_[closest_index]


def print_tree_rules(tree, feature_names, class_names, node=0, depth=0):
    if tree.feature[node] != -2:  
        feature = feature_names[tree.feature[node]]
        threshold = tree.threshold[node]
        left_child = tree.children_left[node]
        right_child = tree.children_right[node]
        
        closest_value = get_closest_feature_name(feature, threshold)
        print('  ' * depth + f"ถ้า {feature} {'<=' if tree.feature[node] != -2 else '>'} {closest_value}:")
        print_tree_rules(tree, feature_names, class_names, left_child, depth + 1)
        
        print('  ' * depth + f"ถ้าไม่ใช่:")
        print_tree_rules(tree, feature_names, class_names, right_child, depth + 1)
    else: 
        class_index = np.argmax(tree.value[node])
        print('  ' * depth + f"ผลลัพธ์: {class_names[class_index]}")

print("กฎการตัดสินใจของ Decision Tree:")
print_tree_rules(clf.tree_, X.columns, clf.classes_)

plt.figure(figsize=(20,10))
plot_tree(
    clf, 
    feature_names=X.columns, 
    class_names=clf.classes_, 
    filled=True, 
    rounded=True, 
    proportion=True,  
    impurity=False,    
    fontsize=10        
)

plt.show()

print("\nความสำคัญของแต่ละปัจจัย:")
for feature, importance in zip(X.columns, clf.feature_importances_):
    print(f"{feature}: {importance:.4f}")

accuracy = clf.score(X_test, y_test)
print(f"\nความแม่นยำของโมเดล: {accuracy:.2f}")
