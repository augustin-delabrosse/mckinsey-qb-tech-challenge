import streamlit as st
import utils
import plotly.figure_factory as ff
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import make_classification

st.title("Projects")

st.write("Test plotly Histogram Random")

x0 = np.random.uniform(500,0,1)
x1 = np.random.uniform(500,0,1)

st.plotly_chart(utils.plotly_hist(x0, x1, "Silo", "Not-Silo","a",'b',"c"), use_container_width=True)

X, y = make_classification(n_samples=500, random_state=0)

model = LogisticRegression()
model.fit(X, y)
y_score = model.predict_proba(X)[:, 1]

st.write("break hecre comes AUC")

st.plotly_chart(utils.roc_curve_plot(y, y_score), use_container_width=True)
