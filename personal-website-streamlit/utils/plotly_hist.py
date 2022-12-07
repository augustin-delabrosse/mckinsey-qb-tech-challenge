import plotly.express as px
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import make_classification
from utils.get_color import *
import plotly.graph_objects as go

X, y = make_classification(n_samples=500, random_state=0)

model = LogisticRegression()
model.fit(X, y)
y_score = model.predict_proba(X)[:, 1]
fpr, tpr, thresholds = roc_curve(y, y_score)

# The histogram of scores compared to true labels
def plotly_hist(X, y, name_X, name_y, title, x_axis, y_axis):
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=X,
        histnorm='percent',
        name=name_X, # name used in legend and hover labels
        marker_color= primaryColor(),
        opacity=0.75,
    ))
    fig.add_trace(go.Histogram(
        x=y,
        histnorm='percent',
        name=name_y,
        marker_color= secondaryColor(),
        opacity=0.75
    ))  

    fig.update_layout(
        title_text=title, # title of plot
        xaxis_title_text=x_axis, # xaxis label
        yaxis_title_text=y_axis, # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1 # gap between bars of the same location coordinates
    )

    return fig