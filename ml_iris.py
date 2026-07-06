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
print("\n=============================================")
print("🤖 Interactive AI Flower Predictor Engine 🤖")
print("=============================================")

# Names of the flowers our AI knows (a List!)
flower_species = ["Setosa 🌸", "Versicolor 🌻", "Virginica 🌺"]

while True:
    print("\nEnter the measurements of a mystery flower to test the AI:")
    user_input = input("Type 4 numbers separated by commas (e.g., 1.2, 2.4, 0.6, 0.2) or 'quit': ")
    
    if user_input.lower() == 'quit':
        print("Shutting down the AI Engine. Goodbye!")
        break
        
    try:
        # 1. Break the user's text into 4 separate decimal numbers
        measurements = [float(x.strip()) for x in user_input.split(",")]
        
        if len(measurements) != 4:
            print("❌ Error: You must enter exactly 4 measurements!")
            continue
            
        # 2. Feed the measurements into your trained AI model
        # (Assuming your model variable is named 'model' or 'clf')
        # We wrap the data in a list [measurements] because the AI expects a 2D array
        prediction_numeric = ai_model.predict([measurements])[0]
        
        # 3. Look up the flower name using the numeric index the AI gave us
        predicted_flower = flower_species[prediction_numeric]
        
        print(f"🔮 AI PREDICTION: This flower is a {predicted_flower}")
        
    except Exception as e:
        print("❌ Invalid format. Please make sure to enter only numbers separated by commas!")
