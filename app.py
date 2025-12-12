import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

with open("knn_model_pickle.pkl", "rb") as f:
    model = pickle.load(f)

st.title("NBA Win Percentage Prediction App")

TEAM_NAME = st.selectbox("Team Name", [
    "Wizards", "Cavaliers", "Heat", "Celtics", "Lakers"
])

TEAM_NAME = int(st.number_input("TEAM_NAME", value=0))
FG_PCT = int(st.number_input("FG_PCT", value=0))
PTS = int(st.number_input("PTS", value=0))
PLUS_MINUS = int(st.number_input("PLUS_MINUS", value=0))
EFG_PCT = int(st.number_input("EFG_PCT", value=0))


if st.button("Predict WIN %"):

    input_df = pd.DataFrame([{
        "TEAM_NAME": TEAM_NAME,
        "FG_PCT": FG_PCT,
        "PTS": PLUS_MINUS,
        "PLUS_MINUS": PLUS_MINUS,                                  
        "EFG_PCT": EFG_PCT,
    }])

    result = model.predict(input_df)[0]

    st.success(f"Predicted WIN % : {result:.2f}")

st.markdown(
"""
<style>
/* Page background */
[data-testid="stAppViewContainer"] {
  background-image: url("https://images.unsplash.com/photo-1555949963-aa79dcee981c?q=80&w=1600");
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
}

/* dim overlay to improve readability */
[data-testid="stAppViewContainer"]::before{
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.45); /* adjust darkness */
  pointer-events: none;
  z-index: 0;
}

/* Main content area: keep above overlay */
[data-testid="stAppViewContainer"] > .main {
  position: relative;
  z-index: 1;
}

/* Frosted glass card where you can put inputs */
.block {
    margin: 20px auto;
    padding: 24px;
    max-width: 920px;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(8px) saturate(120%);
    -webkit-backdrop-filter: blur(8px) saturate(120%);
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.35);
    color: #fff !important;
}

/* Title styling */
.block h1, .block h2 {
    color: #ffd670 !important;
    margin: 0 0 8px 0;
}

/* Small description text inside block */
.block p {
    color: rgba(255,255,255,0.85);
    margin-top: 0;
}

/* Make labels and numbers readable */
input[type="number"], input[type="text"], .stTextInput, select {
    border-radius: 8px !important;
    padding: 10px 12px !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    background: rgba(255,255,255,0.06) !important;
    color: #fff !important;
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.4);
}

/* Streamlit selects often render as a button-like element; style button tags too */
button {
    border-radius: 10px !important;
    padding: 10px 16px !important;
    font-weight: 600;
    cursor: pointer;
}

/* Primary-looking predict button — more visible */
button[data-testid="stButton"] {
    background: linear-gradient(90deg,#ff8a00,#da1b60) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 6px 18px rgba(218,27,96,0.24) !important;
}

/* Make success messages stand out */
.css-1kyxreq .stAlert { /* fallback styling area */
    color: #fff !important;
}

/* Small responsive tweak */
@media (max-width: 640px) {
  .block { margin: 8px; padding: 16px; }
  .block h1 { font-size: 20px; }
}
</style>
""",
unsafe_allow_html=True
)
