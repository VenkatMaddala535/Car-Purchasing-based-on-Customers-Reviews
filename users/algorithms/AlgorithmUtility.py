import pandas as pd
from sklearn.model_selection import train_test_split
from django.conf import settings
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

path = settings.MEDIA_ROOT + "//" + "cars.csv"
df = pd.read_csv(path)
X = df.iloc[:, :-1].values  # indipendent variable
y = df.iloc[:, -1].values  # Dependent variable
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.85, random_state=0)




def calc_random_forest():
    path = settings.MEDIA_ROOT + "//" + "cars.csv"
    df = pd.read_csv(path)
    X = df.iloc[:, :-1].values  # indipendent variable
    y = df.iloc[:, -1].values  # Dependent variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, random_state=1)
    print("*" * 25, "Random Forest Classification")
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)  # Trained wih 80% Data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('RF Accuracy:', accuracy)
    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    print('RF Precision Score:', precision)
    recall = recall_score(y_test, y_pred)
    print('RF Recall Score:', recall)
    f1score = f1_score(y_test, y_pred)
    print('RF F1-Score:', f1score)
    return accuracy, precision, recall, f1score


def calc_naive_bayes_classifier():
    path = settings.MEDIA_ROOT + "//" + "cars.csv"
    df = pd.read_csv(path)
    X = df.iloc[:, :-1].values  # indipendent variable
    y = df.iloc[:, -1].values  # Dependent variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.85, random_state=1)
    print("*"*25,"Naive Bayes")
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(X_train, y_train)  # Trained wih 80% Data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('NB Accuracy:', accuracy)
    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    print('NB Precision Score:', precision)
    recall = recall_score(y_test, y_pred)
    print('NB Recall Score:', recall)
    f1score = f1_score(y_test, y_pred)
    print('NB F1-Score:', f1score)
    return accuracy,precision,recall,f1score


def calc_k_nearest_neighbour_classifier():
    path = settings.MEDIA_ROOT + "//" + "cars.csv"
    df = pd.read_csv(path)
    X = df.iloc[:, :-1].values  # indipendent variable
    y = df.iloc[:, -1].values  # Dependent variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, random_state=0)
    print("*" * 25, "Random Forest Classification")
    print("*" * 25, "K Nearest Neighbour Classifier")
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)  # Trained wih 80% Data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('Knn Accuracy:', accuracy)
    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    print('Knn Precision Score:', precision)
    recall = recall_score(y_test, y_pred)
    print('Knn Recall Score:', recall)
    f1score = f1_score(y_test, y_pred)
    print('Knn F1-Score:', f1score)
    return accuracy, precision, recall, f1score


def calc_support_vector_classifier():
    print("*" * 25, "SVM Classification")
    from sklearn.svm import SVC
    model = SVC(kernel='rbf')
    model.fit(X_train, y_train)  # Trained wih 80% Data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('SVM Accuracy:', accuracy)
    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    print('SVM Precision Score:', precision)
    recall = recall_score(y_test, y_pred)
    print('SVM Recall Score:', recall)
    f1score = f1_score(y_test, y_pred)
    print('SVM F1-Score:', f1score)
    return accuracy, precision, recall, f1score


def calc_perceptron_classifier():
    print("*" * 25, "Perceptron Classifiers")
    from sklearn.linear_model import Perceptron
    model = Perceptron(tol=1e-3, random_state=0)
    model.fit(X_train, y_train)  # Trained wih 80% Data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('Perceptron Accuracy:', accuracy)
    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    print('Perceptron Precision Score:', precision)
    recall = recall_score(y_test, y_pred)
    print('Perceptron Recall Score:', recall)
    f1score = f1_score(y_test, y_pred)
    print('Perceptron F1-Score:', f1score)
    return accuracy, precision, recall, f1score


def test_user_date(test_features):
    print(test_features)
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    test_pred = model.predict([test_features])
    return test_pred


def calculate_ann_results():
    from keras.models import Sequential
    from keras.layers import Dense
    classifier = Sequential()
    classifier.add(Dense(units=4, init='uniform', activation='relu', input_dim=5))
    classifier.add(Dense(units=4, init='uniform', activation='relu'))
    classifier.add(Dense(units=1, init='uniform', activation='sigmoid'))
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    print(classifier.summary())
    classifier.fit(X_train, y_train, batch_size=10, nb_epoch=100)

    y_pred = classifier.predict(X_test)
    y_pred = (y_pred > 0.5)
    accuracy = accuracy_score(y_test, y_pred)
    print('ANN Accuracy:', accuracy)
    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    print('ANN Precision Score:', precision)
    recall = recall_score(y_test, y_pred)
    print('ANN Recall Score:', recall)
    f1score = f1_score(y_test, y_pred)
    print('ANN F1-Score:', f1score)
    return accuracy, precision, recall, f1score


