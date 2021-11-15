#!/usr/bin/python
# -*- coding: utf-8 -*-
import warnings

import arff
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

warnings.filterwarnings('ignore')

dataset_to_classify = 'data/vote.arff'

arffile = arff.load(open(dataset_to_classify))
data = np.array(arffile['data'])

# Recover missing data
data[data == None] = np.nan
imputer = SimpleImputer(strategy='most_frequent')
imputer.fit(data)
data = imputer.transform(data)


X = np.array(data[:, 0:data.shape[1] - 1])
X = X.astype(np.float64)
Y = np.array(data[:, data.shape[1] - 1])

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)


pca = PCA(n_components=2)

pca_x = pca.fit_transform(X)

fig, ax = plt.subplots()

for label, color in zip(['democrat', 'republican'], ['blue', 'red']):
    ax.scatter(
        pca_x[np.argwhere(Y == label), 0],
        pca_x[np.argwhere(Y == label), 1],
        c=color,
        label=label
    )

ax.legend()
plt.show()

pca = PCA(n_components=2)

pca_x = pca.fit_transform(X)

fig, ax = plt.subplots()

for label, color in zip(['democrat', 'republican'], ['blue', 'red']):
    ax.scatter(
        pca_x[np.argwhere(Y == label), 0],
        pca_x[np.argwhere(Y == label), 1],
        c=color,
        label=label
    )

ax.legend()

fig1 = plt.figure()
ax1 = fig1.add_subplot(projection='3d')

pca_3 = PCA(n_components=3)

pca_3_x = pca_3.fit_transform(X)

for label, color in zip(['democrat', 'republican'], ['blue', 'red']):
    ax1.scatter(
        pca_3_x[np.argwhere(Y == label), 0],
        pca_3_x[np.argwhere(Y == label), 1],
        pca_3_x[np.argwhere(Y == label), 2],
        c=color,
        label=label
    )

ax1.legend()

plt.show()

# Grid Search

param_grid_tree = {
    'max_depth': [3, 4, 5, 6, 7, 8],
    'min_samples_split': [2, 3, 4, 5, 6],
    'min_samples_leaf':  [1, 2, 3, 4, 5]
}

param_grid_smv = {
    'C': [1e-1, 1, 10, 100],
    'kernel': ['linear'],
}

param_grid_knn = {
    'n_neighbors': [1, 3, 5, 7, 9, 11],
    'p': [1, 2]
}

grid_search_tree_clf = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid=param_grid_tree,
    scoring='accuracy',
    n_jobs=-1
)

grid_search_svm_clf = GridSearchCV(
    SVC(random_state=42),
    param_grid=param_grid_smv,
    scoring='accuracy',
    n_jobs=-1,
)

grid_search_knn_clf = GridSearchCV(
    KNeighborsClassifier(),
    param_grid=param_grid_knn,
    scoring='accuracy',
    n_jobs=-1
)

print("Mejor modelo de decision tree utilizando grid search")
grid_search_tree_clf.fit(X, Y)
print(grid_search_tree_clf.best_estimator_)

print("Mejor modelo de SVM utilizando grid search")
grid_search_svm_clf.fit(X, Y)
print(grid_search_svm_clf.best_estimator_)

print("Mejor modelo de knn utilizando grid search")
grid_search_knn_clf.fit(X, Y)
print(grid_search_knn_clf.best_estimator_)

print("\n")

#Random search

param_random_tree = {
    'max_depth': [3, 4, 5, 6, 7, 8],
    'min_samples_split': [2, 3, 4, 5, 6],
    'min_samples_leaf':  [1, 2, 3, 4, 5]
}

param_random_smv = {
    'C': uniform(1e-5, 100),
    'kernel': ['linear'],
}

param_random_knn = {
    'n_neighbors': [1, 3, 5, 7, 9, 11],
    'p': [1, 2]
}

random_search_tree_clf = RandomizedSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_random_tree,
    scoring='accuracy',
    n_jobs=-1
)

random_search_svm_clf = RandomizedSearchCV(
    SVC(random_state=42),
    param_random_smv,
    scoring='accuracy',
    n_jobs=-1,
)

random_search_knn_clf = RandomizedSearchCV(
    KNeighborsClassifier(),
    param_random_knn,
    scoring='accuracy',
    n_jobs=-1
)

print("Mejor modelo de decision tree utilizando random search")
random_search_tree_clf.fit(X, Y)
print(random_search_tree_clf.best_estimator_)

print("Mejor modelo de SVM utilizando random search")
random_search_svm_clf.fit(X, Y)
print(random_search_svm_clf.best_estimator_)

print("Mejor modelo de knn utilizando random search")
random_search_knn_clf.fit(X, Y)
print(random_search_knn_clf.best_estimator_)

print("\n")


# Cross validation

print("Cross validation results")

print("SVM")
svm_clf = SVC(kernel='linear', C=1, random_state=42)
cross_val_svm = cross_val_score(svm_clf, X, Y, cv=10, scoring='accuracy', n_jobs=-1)
print(cross_val_svm)

print("Árbol de decision")
tree_clf = DecisionTreeClassifier(random_state=42, max_depth=4, min_samples_split=2)
cross_val_tree = cross_val_score(tree_clf, X, Y, cv=10, scoring='accuracy', n_jobs=-1)
print(cross_val_tree)

print("Knn")
knn_clf = KNeighborsClassifier(n_neighbors=5, p=1)
cross_val_knn = cross_val_score(knn_clf, X, Y, cv=10, scoring='accuracy', n_jobs=-1)
print(cross_val_knn)
