# NBA_Win_Percentage_Prediction
A machine learning project that predicts a basketball team’s win percentage using game statistics such as FG%, EFG%, points scored, and plus/minus values.  This project uses Streamlit to create a simple web application where users can enter game stats and get a predicted win probability.


🏀 NBA Win Percentage Prediction App

A simple Machine Learning project that predicts NBA Team Win Percentage based on game statistics such as FG%, EFG%, Points, and Plus/Minus.
The project also includes a Streamlit web application to allow users to interact with the model.

📌 Project Overview

This project builds an ML model using:

OrdinalEncoder → To convert team names into numeric values

StandardScaler → To scale numerical features

K-Nearest Neighbors (KNN) → Regression model

Streamlit → Web UI for user interaction

The model learns from past match data and predicts whether a team is likely to win or lose based on selected game stats.

🔧 Features

✔ Predicts WIN % (0–100%) for NBA teams
✔ Uses five input features
✔ Interactive Streamlit UI
✔ Clean preprocessing pipeline
✔ Easy to run & understand
✔ Beginner-friendly ML workflow

📊 Dataset Description

The dataset contains these columns:

Column	Description
TEAM_NAME	Name of the basketball team (categorical)
FG_PCT	Field goal percentage
PLUS_MINUS	Score difference vs opponent
PTS	Total points scored

EFG_PCT	Effective field goal percentage
WIN_PCT	Output label (0 or 100)


NBA-Win-Predictor/
│── app.py
│── model_training.ipynb
│── knn_model_pickle.pkl
│── requirements.txt
│── README.md
