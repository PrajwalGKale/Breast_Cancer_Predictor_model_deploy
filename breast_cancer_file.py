import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def breast_cancer_model_deployment(radius_m,
        texture_mean,
        perimeter_mean,
        area_mean,
        smoothness_mean,
        compactness_mean,
        concavity_mean,
        concave_points_mean,
        symmetry_mean,
        fractal_dimension_mean,
        radius_se,
        texture_se,    
        perimeter_se,
        area_se,
        smoothness_se,
        compactness_se,
        concavity_se,
        concave_points_se,
        symmetry_se,
        fractal_dimension_se,
        radius_worst,
        texture_worst,
        perimeter_worst,
        area_worst,
        smoothness_worst,	
        compactness_worst,
        concavity_worst,
        concave_points_worst,
        symmetry_worst,
        fractal_dimension_worst):
    cancer_data = pd.read_csv('venv\data.csv')
    cancer_data.drop(['Unnamed: 32', 'id'], axis=1, inplace=True)
    label = LabelEncoder()
    cancer_data['diagnosis'] = label.fit_transform(cancer_data['diagnosis'])
    data = cancer_data.drop(['diagnosis'], axis = 1)
    target = cancer_data['diagnosis']
    # print(data.shape)
    # print(target.shape)
    x_train,x_test,y_train,y_test = train_test_split(data,target,test_size = 0.25, random_state = 0)
    randforest = RandomForestClassifier(criterion='entropy',max_depth=5,max_features='auto',min_samples_split=6,n_estimators=9,random_state=0)
    randforest.fit(x_train,y_train)
    x_test_r = np.array([
        radius_m,
        texture_mean,
        perimeter_mean,
        area_mean,
        smoothness_mean,
        compactness_mean,
        concavity_mean,
        concave_points_mean,
        symmetry_mean,
        fractal_dimension_mean,
        radius_se,
        texture_se,    
        perimeter_se,
        area_se,
        smoothness_se,
        compactness_se,
        concavity_se,
        concave_points_se,
        symmetry_se,
        fractal_dimension_se,
        radius_worst,
        texture_worst,
        perimeter_worst,
        area_worst,
        smoothness_worst,	
        compactness_worst,
        concavity_worst,
        concave_points_worst,
        symmetry_worst,
        fractal_dimension_worst])
    x_test_r  = x_test_r.reshape((1,-1))
    return randforest.predict(x_test_r)[0]
    
# breast_cancer_model_deployment(user_data)
# res = np.round(accuracy_score(y_test,y_pred)*100,2)
# print(np.round(accuracy_score(y_test,y_pred_rf)*100,2),'%')