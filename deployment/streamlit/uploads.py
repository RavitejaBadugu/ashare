import streamlit as st
import requests
import pandas as pd
import pickle


def app():
    st.title('Below please enter the details')
    df=pd.read_csv('data_schema.csv')
    st.subheader('Go to info page where you can find the details which are requried to file')
    requried_columns=list(df.loc[df['requried']==True,'name'].values)
    data={}
    with open('encoders.pkl','rb') as f:
        encoders=pickle.load(f)
    for col,encoder in encoders.items():
        enter=st.selectbox(f"select value for {col}",list(encoder.classes_))
        if enter:
            if col=='primary_use':
                data[col]=enter
            else:
                data[col]=int(enter)
        else:
            if col=='primary_use':
                data[col]=str(list(encoder.classes_)[0])
            else:
                data[col]=int(list(encoder.classes_)[0])
    categorical_columns=list(encoders.keys())
    numerical_columns=list(col for col in df['name'].values  if col not in categorical_columns)
    for col in numerical_columns:
        enter=st.text_input(f'fill the value of {col}')
        if enter:
            data[col]=enter

    if st.button('submit'):
        count=0
        for col in requried_columns:
            if data[col]==None:
                st.error(f"{col} is not filled")
                count+=1
        if count == 0:
            with st.spinner(text='In progress'):
                response=requests.post('http://fastapi:8000/predict',json=data).json()
                reading=response['meter_reading']
                if reading<0:
                    reading=0
                st.success(f"meter reading is {reading}")