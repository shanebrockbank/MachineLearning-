#Import data set
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data #Features
Y = iris.target #Labels

#Split data into test and train 
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5)

# from sklearn import tree

# #Classifier tree
# clf = tree.DecisionTreeClassifier()

#Using K nearest neighbors instead of decision tree for classifier 
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()

clf = clf.fit(X_train, Y_train) #Fit classifier to training data
predictions = clf.predict(X_test) #Predict from testing 
#print (predictions)

#Compare prediction of test (X_test) to actuall values from Y_test
from sklearn.metrics import accuracy_score
print (accuracy_score(Y_test, predictions))
