**Customer Churn Prediction using Machine Learning**

An end-to-end Customer Churn Prediction System built using Machine Learning techniques to identify customers who are likely to discontinue a service. This project focuses on handling imbalanced data, evaluating multiple models, and deploying the best-performing model using Flask.

**Project Overview**

Customer churn is a major concern for subscription-based businesses. Predicting churn accurately allows companies to take proactive actions to retain customers and reduce revenue loss.
This project demonstrates a complete Machine Learning pipeline starting from data preprocessing and model training to deployment of the final model as a web application.

**Objectives**

-Predict customer churn accurately  
-Handle imbalanced datasets using SMOTE  
-Compare multiple ML models  
-Improve recall for churned customers  
-Deploy the trained model using Flask

**Models Implemented**
| Model                   | Technique                | Accuracy  |
| ----------------------- | ------------------------ | --------- |
| Decision Tree           | Baseline                 | 77.1%     |
| Decision Tree + SMOTE   | Balanced                 | 92.0%     |
| Random Forest            | Baseline                 | 77.8%     |
|  Random Forest + SMOTE | Best Model               | **92.9%** |
| Random Forest + PCA     | Dimensionality Reduction | 70.8%     |

**Best Model Performance**

Random Forest + SMOTE  
Accuracy: 92.9%  
Precision: 0.93  
Recall: 0.95  
F1 Score: 0.94

**Tech Stack**

-Language: Python  
-Libraries: Pandas, NumPy, Scikit-learn  
-Imbalance Handling: SMOTE, SMOTEENN  
-Visualization: Matplotlib, Seaborn  
-Model Deployment: Flask  
-Model Storage: Pickle

**Workflow**

-Data Cleaning & Exploration  
-Feature Engineering  
-Train-Test Split  
-Handling Imbalanced Data (SMOTE)  
-Model Training  
-Model Evaluation  
-Best Model Selection  
-Model Saving  
-Flask Deployment
