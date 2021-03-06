# ashare_prediction

The dataset for this can be found at https://www.kaggle.com/c/ashrae-energy-prediction.

In ashare-v1.ipynb you will find the eda, feature_engineering, hyperparameter tuning and model building
components.

In inferashare.ipynb you will find submission to kaggle.

The metric used is **Root Mean Squared Logarithmic Error.** 

* My score for the competition is ::
![Alt text](https://github.com/RavitejaBadugu/ashare/blob/main/images/Screenshot%202021-12-20%20204439.png)

In deployment directory you will find docker-compose.yml file.

run docker-compose up -d --build to build the images.

The app is made using fastapi as backend and streamlit as frontend.

Most of the code for building docker is inspried from https://github.com/davidefiocco/streamlit-fastapi-model-serving .

Also for making multipage streamlit app, I followed https://www.youtube.com/watch?v=nSw96qUbK9o.

To run the code: Run this command::  docker compose up -d --build.

After using it to remove the containers type:: docker compose down.

# The main page of app:
![Alt text](/images/homepage.png?raw=true)


# sidebar
![Alt text](/images/side_bar.png?raw=true)


# info_page
![Alt text](/images/info_page.png?raw=true)


# uploads_page
![Alt text](/images/upload_page.png?raw=true )


# example of result
![Alt text](/images/result_shown.png?raw=true)



