import joblib
import pandas as pd
import numpy as np

encoder = joblib.load('model/encoder.joblib')
model = joblib.load('model/model.joblib')


encode_columns = ['BusinessTravel', 'Department', 'EducationField', 'JobRole', 'MaritalStatus']


def preprocessing(data_df: pd.DataFrame):
   test_encoded_data = encoder.transform(data_df[encode_columns])
   test_data_df = pd.DataFrame(test_encoded_data, columns=encoder.get_feature_names_out(encode_columns))
   return test_data_df

def predict(data_df: pd.DataFrame):
   test_data_df = preprocessing(data_df)
   
   data_df.drop(encode_columns, axis=1, inplace=True)
   test_df = pd.concat([data_df.reset_index(drop=True), test_data_df.reset_index(drop=True)], axis=1)

   result = model.predict_proba(test_df)

   label = ['No', 'Yes']
   print("Probability", result)
   print(f"Attrition : {label[np.argmax(result)]}")



# source data from external example
data_to_predict = {
   'Age': 38,
   'BusinessTravel': 'Travel_Frequently',
   'DailyRate': 1444,
   'Department': 'Human Resources',
   'DistanceFromHome': 1,
   'Education': 4,
   'EducationField': 'Other',
   'EnvironmentSatisfaction': 4,
   'Gender': 1,
   'HourlyRate': 88,
   'JobInvolvement': 3,
   'JobLevel': 1,
   'JobRole': 'Human Resources',
   'JobSatisfaction': 2,
   'MaritalStatus': 'Married',
   'MonthlyIncome': 2991,
   'MonthlyRate': 5224,
   'NumCompaniesWorked': 0,
   'OverTime': 1,
   'PercentSalaryHike': 11,
   'PerformanceRating': 3,
   'RelationshipSatisfaction': 2,
   'StockOptionLevel': 1,
   'TotalWorkingYears': 7,
   'TrainingTimesLastYear': 2,
   'WorkLifeBalance': 3,
   'YearsAtCompany': 6,
   'YearsInCurrentRole': 2,
   'YearsSinceLastPromotion': 3,
   'YearsWithCurrManager': 1,
} 

data_df = pd.DataFrame(data_to_predict, index=[0])


# start to predict
predict(data_df)