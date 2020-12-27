import pickle
import json
import numpy as np
import os

__data_columns = None
__model = None


def predict_loan_status_func(applicant_income, co_income, loan_amount, gender, married, dependents,
                             edu, emp, loan_term, credit_hist, property_area):



    loc_index4 = __data_columns.index(edu.lower())
    loc_index5 = __data_columns.index(emp.lower())
    loc_index6 = __data_columns.index(loan_term.lower())
    loc_index7 = __data_columns.index(credit_hist.lower())
    loc_index8 = __data_columns.index(property_area.lower())
    loc_index2 = __data_columns.index(married.lower())
    loc_index3 = __data_columns.index(dependents.lower())
    loc_index1 = __data_columns.index(gender.lower())

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

    print(loc_index1)
    print("Above gneder")

    return __model.predict([x])[0]


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    path = os.path.dirname(__file__)
    artifacts = os.path.join(path, "artifacts"),

    # with open("./artifacts/columns.json", "r") as f:
    #    __data_columns = json.load(f)['data_columns']

    # global __model
    # if __model is None:
    #     with open('./artifacts/loan_prediction_model.pickle', 'rb') as f:
    #         __model = pickle.load(f)
    # print("loading saved artifacts...done")

    with open(artifacts[0] + "/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open(artifacts[0] + "/loan_prediction_model.pickle", 'rb') as f:
            __model = pickle.load(f)
        print("loading saved artifacts...done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print("Result is:")
    print(predict_loan_status_func(10000, 0, 115000.0, "Gender_Male", "Married_No", "Dependents_0",
                                   "Education_Graduate", "Self_Employed_No", "Loan_Amount_Term_60.0",
                                   "Credit_History_1.0", "Property_Area_Semiurban"))
