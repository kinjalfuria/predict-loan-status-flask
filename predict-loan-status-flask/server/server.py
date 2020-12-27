from flask import Flask, request, jsonify, render_template


import pickle
import json
import numpy as np
import os

__data_columns = ['applicantincome', 'coapplicantincome', 'loanamount', 'gender_female', 'gender_male', 'married_no',
                   'married_yes', 'dependents_0', 'dependents_1','dependents_2', 'dependents_3+', 'education_graduate',
                   'education_not graduate', 'self_employed_no', 'self_employed_yes', 'loan_amount_term_12.0',
                   'loan_amount_term_36.0', 'loan_amount_term_60.0', 'loan_amount_term_84.0', 'loan_amount_term_120.0',
                   'loan_amount_term_180.0', 'loan_amount_term_240.0','loan_amount_term_300.0',
                   'loan_amount_term_360.0', 'loan_amount_term_480.0', 'credit_history_0.0',
                   'credit_history_1.0', 'property_area_rural', 'property_area_semiurban', 'property_area_urban']
__model = None


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    path = os.path.dirname(__file__)
    artifacts = os.path.join(path, "artifacts"),



    # with open(artifacts[0] + "/columns.json", "r") as f:
    #     __data_columns = json.load(f)['data_columns']
    #     print("data columns", __data_columns)

    global __model
    if __model is None:
        with open(artifacts[0] + "/loan_prediction_model.pickle", 'rb') as f:
            __model = pickle.load(f)
        print("loading saved artifacts...done")


# def get_data_columns():
#     return __data_columns


load_saved_artifacts()


# if __name__ == '__main__':
    # load_saved_artifacts()


def predict_loan_status_func(applicant_income, co_income, loan_amount, gender, married, dependents,
                             edu, emp, loan_term, credit_hist, property_area):

    loc_index1 = __data_columns.index(gender.lower())
    loc_index2 = __data_columns.index(married.lower())
    loc_index3 = __data_columns.index(dependents.lower())
    loc_index4 = __data_columns.index(edu.lower())
    loc_index5 = __data_columns.index(emp.lower())
    loc_index6 = __data_columns.index(loan_term.lower())
    loc_index7 = __data_columns.index(credit_hist.lower())
    loc_index8 = __data_columns.index(property_area.lower())

    x = np.zeros(len(__data_columns))
    x[0] = applicant_income
    x[1] = co_income
    x[2] = loan_amount


    if loc_index1 >= 0:
        x[loc_index1] = 1

    if loc_index2 >= 0:
        x[loc_index2] = 1

    if loc_index3 >= 0:
        x[loc_index3] = 1

    if loc_index4 >= 0:
        x[loc_index4] = 1

    if loc_index5 >= 0:
        x[loc_index5] = 1

    if loc_index6 >= 0:
        x[loc_index6] = 1

    if loc_index7 >= 0:
        x[loc_index7] = 1

    if loc_index8 >= 0:
        x[loc_index8] = 1

    print("data columns printing")
    print(__data_columns)

    return __model.predict([x])[0]


print(predict_loan_status_func(10000, 0, 115.0, "Gender_Female", "Married_No", "Dependents_0",
                               "Education_Graduate", "Self_Employed_No", "Loan_Amount_Term_60.0",
                               "Credit_History_1.0", "Property_Area_Semiurban"))

    
app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")


@app.route('/hello')
def hello():
    return "Hi Checking!!"


@app.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        return render_template("app.html")


@app.route('/predict_status', methods=['POST'])
def predict_status():
    applicant_income = int(request.form['applicant_income'])
    co_income = float(request.form['co_income'])
    loan_amount = float(request.form['loan_amount'])
    gender = request.form['gender']
    married = request.form['married']
    dependents = request.form['dependents']
    edu = request.form['edu']
    emp = request.form['emp']
    loan_term = request.form['loan_term']
    credit_hist = request.form['credit_hist']
    property_area = request.form['property_area']


    response3 = predict_loan_status_func(applicant_income, co_income, loan_amount, gender, married, dependents, edu, emp, loan_term, credit_hist, property_area)

    resultk = str(response3)
    result = jsonify({'loan_status': resultk})

    return result


if __name__ == "__main__":
    print("Starting Python Flask Server For Loan Status Prediction...")
    load_saved_artifacts()
    app.run()


