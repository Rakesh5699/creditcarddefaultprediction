from flask import Flask,request,render_template,Response
import pickle
import pandas as pd
from training_Validation_Insertion import train_validation
from trainingModel import trainModel
from prediction_Validation_Insertion import pred_validation
from predictFromModel import prediction
import sklearn

# model creation
model = pickle.load(open("SingleValueModels/rfc.pkl","rb"))

app = Flask(__name__,template_folder="templates")

@app.route('/',methods=['POST','GET'])
def Home():
    return render_template('index.html') 

@app.route("/SinglValuePrediction",methods=['POST','GET'])
def SinglValuePrediction():
    prediction_list = []
    gender = ""
    
    if request.method == "POST":
        #getting values
        limit_bal = float(request.form["cardlimit"])
        sex = int(request.form["Gender"])
        education = int(request.form["education"])
        marital = int(request.form["marital"])
        age = int(request.form["age"])
        PAY_1 = int(request.form["repay_sep"])
        PAY_2 = int(request.form["repay_aug"])
        PAY_3 = int(request.form["repay_july"])
        PAY_4 = int(request.form["repay_june"])
        PAY_5 = int(request.form["repay_may"])
        PAY_6 = int(request.form["repay_april"])
        BILL_AMT1 = float(request.form["bill_sep"])
        BILL_AMT2 = float(request.form["bill_aug"])
        BILL_AMT3 = float(request.form["bill_july"])
        BILL_AMT4 = float(request.form["bill_june"])
        BILL_AMT5 = float(request.form["bill_may"])
        BILL_AMT6 = float(request.form["bill_april"])
        PAY_AMT1 = float(request.form["paid_sep"])
        PAY_AMT2 = float(request.form["paid_aug"])
        PAY_AMT3 = float(request.form["paid_july"])
        PAY_AMT4 = float(request.form["paid_june"])
        PAY_AMT5 = float(request.form["paid_may"])
        PAY_AMT6 = float(request.form["paid_april"])
        # storing in list to predict
        prediction_list = [limit_bal,sex,education,marital,age,PAY_1,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]

        final_prediction = model.predict([prediction_list])[0]
        print(final_prediction)
        if sex == 1:
            gender = "He"
        else :
            gender = "She"
            print(final_prediction)
        if final_prediction == 1:
            return render_template('singlevalueprediction.html',neg_result="Oops!, "+gender+" will be defaulter for next month")
        else:
            return render_template('singlevalueprediction.html',pos_result="Hurry!, "+gender+" will not be a defaulter for next month")

    else:
        return render_template('singlevalueprediction.html')


@app.route("/Prediction", methods=['POST', 'GET'])
def Prediction():
    try:
        if request.method == "POST":
            if request.form is not None:
                path = request.form['filepath']
                # object initialization for prediction ingestion
                pred_val = pred_validation(path)
                pred_val.prediction_validation()  # calling the prediction_validation function
                # object initialization for Prediction
                pred = prediction(path)
                path = pred.predictionFromModel()  # predicting for dataset present in database
                return Response(path)
        else:
            return render_template("prediction.html")

    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)


@app.route("/Training", methods=['POST', 'GET'])
def Training():
    try:
        if request.method == "POST":
            path = request.form['filepath']
            if len(path) == 0:
                return Response("Please Enter a Path to do Training..!!")
            elif path == "Training_Batch_Files":
                # object initialization for training ingestion
                train_valObj = train_validation(path)
                train_valObj.train_validation()  # calling the training_validation
                # object initialization for model training
                trainModelObj = trainModel()
                trainModelObj.trainingModel()  # training the model for the files in the table
                return Response("Default File Training completed successfully")
            else:
                train_valObj = train_validation(path)  # object initialization
                train_valObj.train_validation()  # calling the training_validation
                trainModelObj = trainModel()  # object initialization
                trainModelObj.trainingModel()  # training the model for the files in the table
                return Response("Training completed successfully By Using " + path)
        else:
            return render_template("training.html")
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)



@app.route("/Predictionscsvtohtml")
def Predictionscsvtohtml():
    try:
        data = pd.read_csv("Prediction_Output_File/Predictions.csv")
        return render_template("result.html", tables=[data.to_html(columns=["Predictions"])], titles=[''])
    except:
        return render_template("prediction.html",Error="Do Predication to see Prediction..!")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port=6001)



