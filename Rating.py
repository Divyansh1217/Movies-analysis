import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st
mov=pd.read_csv("movies.dat",delimiter="::")
rat=pd.read_csv("ratings.dat",delimiter="::")
mov.columns=["ID","Title","Genre"]
rat.columns=["User","ID","Ratings","Timestamp"]
data=pd.merge(mov,rat,how="inner",on=["ID","ID"])
data=data.groupby(["ID","Title"]).agg({"User":"sum","Ratings":"mean","Timestamp":"sum"})
rats=data["Ratings"].value_counts()
numbers=rats.index
qun=rats.values
fig=go.Figure(go.Pie(labels=numbers,values=qun,hoverinfo="label+percent",textinfo="value"))
st.dataframe(data.head(10))
st.plotly_chart(fig)

