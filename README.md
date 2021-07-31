# ashare_prediction

The dataset for this can be found at https://www.kaggle.com/c/ashrae-energy-prediction.

In ashare-v1.ipynb you will find the eda, feature_engineering, hyperparameter tuning and model building
components.

In inferashare.ipynb you will find submission to kaggle.

In deployment directory you will find docker-compose.yml file.

run docker-compose up -d --build to build the images.

The app is made using fastapi as backend and streamlit as frontend.

Most of the code for building docker is inspried from https://github.com/davidefiocco/streamlit-fastapi-model-serving .

Also for making multipage streamlit app, I followed https://www.youtube.com/watch?v=nSw96qUbK9o
