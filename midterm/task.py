import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# ==========================================
# Q1. Dataset Preparation
# ==========================================
print("--- Q1. Dataset Preparation ---")
iris = load_iris()
X = iris.data      # Input features
y = iris.target    # Labels

sample_count = X.shape[0]
feature_count = X.shape[1]
class_names = iris.target_names

print(f"Total Sample Count: {sample_count}")
print(f"Total Feature Count: {feature_count}")
print(f"Target Class Names: {list(class_names)}\n")

# ==========================================
# Q2. Training and Testing Split
# ==========================================
print("--- Q2. Training and Testing Split ---")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Number of Training Samples: {X_train.shape[0]}")
print(f"Number of Testing Samples: {X_test.shape[0]}\n")

# ==========================================
# Q3. Model Implementation & Scaling
# ==========================================
print("--- Q3. Model Implementation ---")
# Standardize features (fitted ONLY on training data to prevent data leakage)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train KNN classifier (for Odd registration numbers)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
print("KNN model trained successfully with n_neighbors=5.\n")

# ==========================================
# Q4. Model Evaluation
# ==========================================
print("--- Q4. Model Evaluation ---")
y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Classification Accuracy on Test Set: {accuracy * 100:.2f}%\n")

# ==========================================
# Q5. Ten Predictions
# ==========================================
print("--- Q5. Ten Predictions (First 10 Test Rows) ---")
print(f"{'Obs No.':<10} | {'Actual Species':<18} | {'Predicted Species':<18}")
print("-" * 50)

# Odd registration number: first ten test rows (positions 0-9)
for i in range(10):
    actual_name = class_names[y_test[i]]
    predicted_name = class_names[y_pred[i]]
    print(f"{i+1:<10} | {actual_name:<18} | {predicted_name:<18}")
print()

# ==========================================
# Q6. Confusion Matrix
# ==========================================
print("--- Q6. Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)


#####################################linear regression#####################################


import pandas as pd
import matplotlib.pyplot as plt

# ## Importing the dataset
# Using 'r' before the path prevents Python escape character errors with '\R'
dataset = pd.read_csv(r"D:\Regression\Salary_Data.csv")

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# ## Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

print("X_train samples:\n", X_train)
print("\ny_train samples:\n", y_train)

# ## Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# ## Predicting the Test set results
y_pred = regressor.predict(X_test)

# ## Visualising the Training set results
plt.scatter(X_train, y_train, color='r')
plt.plot(X_train, regressor.predict(X_train), color='b')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# ## Visualising the Test set results (using training line)
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# ## Visualizing Test Results by using X_test and y_pred in plt.plot
plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, y_pred, color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# ## Making a single prediction (e.g., salary for 12 years of experience)
single_prediction = regressor.predict([[12]])
print("Single prediction for 12 years:", single_prediction)

coefficient = regressor.coef_
intercept = regressor.intercept_
print("Coefficient is:", coefficient)
print("Intercept is:", intercept)

# ## Extra Practice
manual_prediction = intercept[0] + coefficient[0] * 15
print("Manual prediction by using coefficient and intercept for 15 years:", manual_prediction)

auto_prediction = regressor.predict([[15]])
print("Auto prediction for 15 years:", auto_prediction)











############################multi linear regression#####################################


import matplotlib.pyplot as plt
import pandas as pd
"""## Importing the dataset"""
dataset = pd.read_csv(r'D:\Regression\50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
"""## Encoding categorical data"""
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])],
remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)
"""## Splitting the dataset into the Training set and Test set"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
random_state = 0)
"""## Training the Multiple Linear Regression model on the Training set"""
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
"""## Predicting the Test set results"""
1
1
Output:
Activity 3: (Logistic Regression Binary)
It is a binary logistic regression problem as there are only two possible outcomes (i.e. if person
buys insurance or he/she doesn't).
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline
from google.colab import drive
drive.mount('/content/gdrive')
df = pd.read_csv("/content/gdrive/My Drive/insurance_data.csv")
df.head()
plt.scatter(df.age,df.bought_insurance,marker='+',color='red')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_in
surance,train_size=0.8)
X_test
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1),
y_test.reshape(len(y_test),1)),1))





###########################LOGISTIC REGRESSION#####################################

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# If running locally or adjusting path, modify as needed:
# df = pd.read_csv("insurance_data.csv") 

# For Google Colab:
from google.colab import drive
drive.mount('/content/gdrive')
df = pd.read_csv("/content/gdrive/My Drive/insurance_data.csv")
print(df.head())

# Plotting the data
plt.scatter(df.age, df.bought_insurance, marker='+', color='red')
plt.xlabel('Age')
plt.ylabel('Bought Insurance')
plt.show()

# Splitting dataset into training and testing sets (80% train, 20% test)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['age']], df['bought_insurance'], train_size=0.8, random_state=42)

print("X_test:\n", X_test)

# Training the Logistic Regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predicting test set results
y_pred = model.predict(X_test)

# Display predictions side-by-side with actual test values
np.set_printoptions(precision=2)
print("\nPredicted vs Actual:")
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.to_numpy().reshape(len(y_test), 1)), 1))

# Model Evaluation and Probabilities
print("\nModel Score (Accuracy):", model.score(X_test, y_test))
print("Prediction Probabilities:\n", model.predict_proba(X_test))

# Model coefficients (m and b in logistic regression log-odds equation)
print("\nCoefficient (m):", model.coef_)
print("Intercept (b):", model.intercept_)

# Sigmoid function math definition
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def prediction_function(age):
    # Using rounded coefficients from model or explicit values
    z = model.coef_[0][0] * age + model.intercept_[0]
    y = sigmoid(z)
    return y

# Testing custom ages with the sigmoid math function
age_35 = 35
prob_35 = prediction_function(age_35)
print(f"\nAge {age_35} Probability: {prob_35:.3f}")
if prob_35 < 0.5:
    print(f"0.485 is less than 0.5 which means person with {age_35} age will not buy insurance")

age_43 = 43
prob_43 = prediction_function(age_43)
print(f"Age {age_43} Probability: {prob_43:.3f}")
if prob_43 >= 0.5:
    print(f"0.568 is more than 0.5 which means person with {age_43} will buy the insurance")
    
    
    
    
    #######################MULTICLASS LOGISTI#######################
    
    
    from sklearn.datasets import load_digits
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

# 1. Load digits dataset
digits = load_digits()

# Display the first 5 images
plt.gray()
for i in range(5):
    plt.matshow(digits.images[i])
    plt.show()

# Explore dataset structure
print("Dataset keys/attributes:", dir(digits))
print("First digit data sample representation:\n", digits.data[0])

# 2. Split dataset into training and testing sets (80% train, 20% test)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# 3. Create and train Logistic Regression model
from sklearn.linear_model import LogisticRegression
# Increased max_iter to ensure convergence on the digits dataset
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# 4. Measure accuracy of our model
accuracy = model.score(X_test, y_test)
print(f"\nModel Accuracy on Test Set: {accuracy * 100:.2f}%")

# Predict the first 5 digits
predictions = model.predict(digits.data[0:5])
print("Predictions for the first 5 digits:", predictions)

# 5. Confusion Matrix
y_predicted = model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
print("\nConfusion Matrix:\n", cm)

# 6. Plotting Confusion Matrix Heatmap
plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.title('Confusion Matrix Heatmap - Multiclass Digits')
plt.show()