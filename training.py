import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
import joblib

# Load CSV file into a DataFrame
df = pd.read_csv('chronic_kidney_disease_full.arff.csv')

# Define replacements for each column based on attribute information
replacements = {
    'age': 0,  # Replace '?' in age with 0 (assuming 0 represents missing age)
    'bp': 0,  # Replace '?' in bp with 0 (assuming 0 represents missing blood pressure)
    'sg': '1.010',  # Replace '?' in sg with '1.010'
    'al': '0',  # Replace '?' in al with '0'
    'su': '0',  # Replace '?' in su with '0'
    'rbc': 'normal',  # Replace '?' in rbc with 'normal'
    'pc': 'normal',  # Replace '?' in pc with 'normal'
    'pcc': 'notpresent',  # Replace '?' in pcc with 'notpresent'
    'ba': 'notpresent',  # Replace '?' in ba with 'notpresent'
    'bgr': 0,  # Replace '?' in bgr with 0 (assuming 0 represents missing value)
    'bu': 0,  # Replace '?' in bu with 0 (assuming 0 represents missing value)
    'sc': 0,  # Replace '?' in sc with 0 (assuming 0 represents missing value)
    'sod': 0,  # Replace '?' in sod with 0 (assuming 0 represents missing value)
    'pot': 0,  # Replace '?' in pot with 0 (assuming 0 represents missing value)
    'hemo': 0,  # Replace '?' in hemo with 0 (assuming 0 represents missing value)
    'pcv': 0,  # Replace '?' in pcv with 0 (assuming 0 represents missing value)
    'wbcc': 0,  # Replace '?' in wbcc with 0 (assuming 0 represents missing value)
    'rbcc': 0,  # Replace '?' in rbcc with 0 (assuming 0 represents missing value)
    'htn': 'no',  # Replace '?' in htn with 'no'
    'dm': 'no',  # Replace '?' in dm with 'no'
    'cad': 'no',  # Replace '?' in cad with 'no'
    'appet': 'good',  # Replace '?' in appet with 'good'
    'pe': 'no',  # Replace '?' in pe with 'no'
    'ane': 'no',  # Replace '?' in ane with 'no'
    'class': 'notckd'  # Replace '?' in class with 'notckd'
}

# Replace '?' values in each column with appropriate values based on attribute information
for col, replacement in replacements.items():
    df[col] = df[col].replace('?', replacement)

# One-hot encode categorical variables
categorical_cols = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
df_encoded = pd.get_dummies(df, columns=categorical_cols)      #telos preprocess

# Split data into features (X) and target variable (y)
X = df_encoded.drop(columns=['class'])
y = df_encoded['class']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose a model (Random Forest Classifier in this example)
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Save the trained model to a .pkl file
joblib.dump(model, 'trained_model.pkl')

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
