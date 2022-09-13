from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
irisdata=load_iris()
print(irisdata.data)
x=irisdata.data
y=irisdata.target
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42)
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
print(knn.predict(x_test))
print(knn.score(x_test,y_test))
