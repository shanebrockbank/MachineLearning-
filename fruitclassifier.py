from sklearn import tree

#Weight, Texture (1:smooth, 0:bumpy)
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
#1:orange, 0:apple
labels = [0, 0, 1, 1]

#Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print (clf.predict([[160, 0]]))
