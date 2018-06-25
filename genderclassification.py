from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier

#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42],     
     [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#Classifier
clf = tree.DecisionTreeClassifier()
clfKNN = KNeighborsClassifier()

clf = clf.fit(X,Y)
clfKNN = clfKNN.fit(X,Y)

clfPrediction = clf.predict([[190,70,43]])
clfKNNPrediction = clfKNN.predict([[190,70,43]])

print('tree: %s' % clfPrediction)
print('KNN: %s' % clfKNNPrediction)