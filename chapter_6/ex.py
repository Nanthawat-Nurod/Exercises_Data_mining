import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions
from sklearn.datasets import load_iris  

def select_best_model(models, X_test, y_test):
    best_model = None
    best_accuracy = 0
    for name, model in models.items():
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f'{name} Accuracy: {accuracy:.2f}')
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = name
    return best_model, best_accuracy

iris = load_iris()
X = iris.data[:, [0, 2]]  
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# สร้างและฝึกโมเดล SVM
svm = SVC(kernel='rbf', random_state=1, gamma=0.10, C=10.0)
svm.fit(X_train_std, y_train)

# สร้างและฝึกโมเดล KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_std, y_train)

# เปรียบเทียบและเลือกโมเดลที่ดีที่สุด
models = {'SVM': svm, 'KNN': knn}
best_model, best_accuracy = select_best_model(models, X_test_std, y_test)

print(f"\nโมเดลที่ดีที่สุดคือ {best_model} ด้วยความแม่นยำ {best_accuracy:.2f}")
print(f"ผมเลือกใช้โมเดล {best_model} เนื่องจากมีค่าความแม่นยำสูงกว่าครับ")

# สร้างกราฟแสดงขอบเขตการตัดสินใจ
plt.figure(figsize=(12, 5))

plt.subplot(121)
plot_decision_regions(X_train_std, y_train, clf=svm, legend=2)
plt.title('SVM Decision Regions')

plt.subplot(122)
plot_decision_regions(X_train_std, y_train, clf=knn, legend=2)
plt.title('KNN Decision Regions')

plt.tight_layout()
plt.show()