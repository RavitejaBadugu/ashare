import pandas as pd
from xgboost import XGBRegressor
import pickle
import numpy as np

with open('utils/feature_changes','rb') as f:
    feature_changes=pickle.load(f)
with open("utils/encoders.pkl",'rb') as f:
    encoders=pickle.load(f)
with open("utils/total_columns.pkl",'rb') as f:
    total_columns=pickle.load(f)
with open('utils/model_params.json','rb') as f:
    model_params=pickle.load(f)
xgb1=XGBRegressor(**model_params)
xgb1.load_model('utils/xgboost_0')
xgb2=XGBRegressor(**model_params)
xgb2.load_model('utils/xgboost_1')
xgb3=XGBRegressor(**model_params)
xgb3.load_model('utils/xgboost_2')
xgb4=XGBRegressor(**model_params)
xgb4.load_model('utils/xgboost_3')
xgb5=XGBRegressor(**model_params)
xgb5.load_model('utils/xgboost_4')


def fill_cloud(site):
    if str(feature_changes['fill_null/weather/cloud_coverage'][site])=='nan':
        return feature_changes['fill_null/weather/cloud_coverage_cloud_fill_nan']
    else:
        return feature_changes['fill_null/weather/cloud_coverage'][site]
def fill_precip(site):
    if str(feature_changes['fill_null/weather/precip_depth_1_hr'][site])=='nan':
        return feature_changes['fill_null/weather/precip_depth_1_hr_precip_fill_nan']
    else:
        return feature_changes['fill_null/weather/precip_depth_1_hr'][site]

def get_preprocessed(data):
    df=pd.DataFrame(data,index=[0])
    df['air_temperature'].fillna(value=feature_changes['fill_null/weather/air_temperature'],inplace=True)
    df['sea_level_pressure'].fillna(value=feature_changes['fill_null/weather/sea_level_pressure'],inplace=True)
    df['wind_speed'].fillna(value=feature_changes['fill_null/weather/wind_speed'],inplace=True)
    df['dew_temperature'].fillna(value=feature_changes['fill_null/weather/dew_temperature'],inplace=True)
    df['wind_direction'].fillna(value=feature_changes['fill_null/weather/wind_direction'],inplace=True)
    df.loc[df['floor_count'].isnull()==True,'floor_count']=df.loc[df['floor_count'].isnull()==True,'primary_use'].map(feature_changes['fill_null/build/floor_count'])
    df.loc[df['cloud_coverage'].isnull()==True,'cloud_coverage']=df.loc[df['cloud_coverage'].isnull()==True,'site_id'].apply(fill_cloud)
    df.loc[df['precip_depth_1_hr'].isnull()==True,'precip_depth_1_hr']=df.loc[df['precip_depth_1_hr'].isnull()==True,'site_id'].apply(fill_precip)
    for col,encoder in encoders.items():
        df[col]=encoder.transform(df[col])
    return df

def get_model_prediction(data):
    data=data[total_columns].values
    p1=np.expm1(xgb1.predict(data))
    p2=np.expm1(xgb2.predict(data))
    p3=np.expm1(xgb3.predict(data))
    p4=np.expm1(xgb4.predict(data))
    p5=np.expm1(xgb5.predict(data))
    p=(p1+p2+p3+p4+p5)/5.0
    return float(p)
    