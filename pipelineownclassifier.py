from scipy.spatial import distance
import numpy
def euc(a,b):
    return distance.euclidean(a,b)

class ScrappyKNN():
    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_distance = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_distance:
                best_distance = dict
                best_index = i
        return self.Y_train[best_index]

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

# #Using K nearest neighbors instead of decision tree for classifier 
# from sklearn.neighbors import KNeighborsClassifier
# clf = KNeighborsClassifier()

clf = ScrappyKNN()

clf.fit(X_train, Y_train) #Fit classifier to training data
predictions = clf.predict(X_test) #Predict from testing 
#print (predictions)

#Compare prediction of test (X_test) to actuall values from Y_test
from sklearn.metrics import accuracy_score
print (accuracy_score(Y_test, predictions))
