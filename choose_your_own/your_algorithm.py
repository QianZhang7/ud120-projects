#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
### KNN Classifier #######
clf1 = KNeighborsClassifier()
clf1 = clf1.fit(features_train, labels_train)
labels_predict_knn = clf1.predict(features_test)
prettyPicture(clf1, features_test, labels_test)
knn_accuracy = accuracy_score(labels_test, labels_predict_knn)
print "KNN accuracy is ", knn_accuracy

### Random Forest #######

clf2 = RandomForestClassifier()
clf2 = clf2.fit(features_train, labels_train)
labels_predict_RF = clf2.predict(features_test)
prettyPicture(clf2, features_test, labels_test)
rf_accuracy = accuracy_score(labels_test, labels_predict_RF)
print "Random Forest accuracy is ", rf_accuracy

### Adaboost #######

clf3 = AdaBoostClassifier()
clf3 = clf3.fit(features_train, labels_train)
labels_predict_RF = clf3.predict(features_test)
prettyPicture(clf3, features_test, labels_test)
adaboost_accuracy = accuracy_score(labels_test, labels_predict_RF)
print "Adaboosting accuracy is ", adaboost_accuracy



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
