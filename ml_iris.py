import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 

print("--- Starting AI Training Phase ---")

# 1. Load the dataset (Iris flower dimensions)
iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# 2. Split data: 80% to train the AI, 20% to test if it actually learned correctly
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 3. Choose the AI Brain (Decision Tree works like a smart flowchart)
ai_model = DecisionTreeClassifier()

# 4. Train the model by showing it the flower measurements and their correct names
ai_model.fit(x_train, y_train)

# 5. Put the AI to the test on the remaining 20% of data it has never seen before 
predictions = ai_model.predict(x_test)
score = accuracy_score(y_test, predictions)

print("--- Training Complete! ---")
print(f"Your AI achieved an accuracy score of: {score * 100:.2f}%")