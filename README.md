# **💳Credit Card Default Prediction**

In this project i have created a  web app with predictive model for credit card default Prediction. Which is will help banks and loan lenders to predict whether customers will default 
the credit card payment or not, so the bank or respective departments can take 
necessary action, based on the model's predictions. The UI is made to be user-friendly 
so that the user will not need much knowledge of any tools but will just need the 
information for results

![image](https://user-images.githubusercontent.com/75267160/181108154-0479f193-fde4-412b-a6cf-86869c5e5b6a.png)

<br>

### 🔒**PROBLEM STATEMENT**

Financial threats are displaying a trend about the credit risk of commercial banks 
as the incredible improvement in the financial industry has arisen. In this way, one of 
the biggest threats faces by commercial banks is the risk prediction of credit clients. 
The goal is to predict the probability of credit default based on credit card owner's
characteristics and payment history.
### 🔑**PROPOSED SOLUTION**

The solution proposed here is a Credit card default Prediction model can be 
implemented to perform above mention use case. ln this case, we have to enter the 
last six months bill amounts , paid amounts, payment status, credit limit, personal 
details. Based on the above details model predicts we whether customers will default the credit card payment or not

## 🎯**Overview**
This is a classification model for a most common dataset, Credit Card defaulter prediction. Prediction of the next month credit card defaulter based on demographic and last six months behavioral data of customers.


## 🏷️**Dataset Information**
Our dataset ‘**Default of Credit Card Clients Dataset**’ consists of informations about transactions from April 2005 to September 2005 of 30000 clients who were credit holders in a bank in Taiwan. This dataset has binary response variable ‘default.payment.next.month’ that takes the value 1 if the corresponding client has default payment and 0 otherwise. Out of 30000 clients 6636(22.12%) were with default payment. There are 23 other independent or explanatory variables:

* ID: ID of each client
* LIMIT_BAL: Amount of given credit in NT dollars (includes individual and 
family/supplementary = credit) 
* SEX: Gender (1=male, 2=female) 
* EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 
6=unknown) MARRIAGE: Marital status (1=married, 2=single, 3=others) 
* AGE: Age in years 
* PAY_1: Repayment status in September 2005 (-1=pay duly, 1=payment delay for one 
month, 2=payment delay for two months, … 8=payment delay for eight months,9=payment delay for nine months and above) 
* PAY_2: Repayment status in August 2005 (scale same as above) 
* PAY_3: Repayment status in July 2005 (scale same as above) 
* PAY_4: Repayment status in June 2005 (scale same as above) 
* PAY_5: Repayment status in May 2005 (scale same as above) 
* PAY_6: Repayment status in April 2005 (scale same as above) 
* BILL_AMT1: Amount of bill statement in September 2005 (NT dollar) 
* BILL_AMT2: Amount of bill statement in August 2005 (NT dollar) 
* BILL_AMT3: Amount of bill statement in July 2005 (NT dollar) 
* BILL_AMT4: Amount of bill statement in June 2005 (NT dollar) 
* BILL_AMT5: Amount of bill statement in May 2005 (NT dollar) 
* BILL_AMT6: Amount of bill statement in April 2005 (NT dollar) 
* PAY_AMT1: Amount of previous payment in September 2005 (NT dollar) 
* PAY_AMT2: Amount of previous payment in August 2005 (NT dollar) 
* PAY_AMT3: Amount of previous payment in July 2005 (NT dollar)

[Click here for DataSet](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)


## 🔎**Technical Aspect**

This project is divided into three part:

 1. Single Value Prediction:
    * Trained a RandomForestClassifier classification model to predict defaulter with **84% accuracy**. 
    * This is work when user used single value prediction feature. 
 2. Training:
    * When ever batch files recived from clients. dataset will validate and cleaned and then dataset first into clusters gropu. 
    * Based on number of clusters that many models will be created and store the models for prediction purpose.
 3. Prediction:
    * When client enter prediction dataset batch file paths. first it will validate and cleaned. 
    * Then it will go for preiction with saved models. Finally predictions will show to client.
 4. Deplyement :
    * CI/CD pipline was created by using github and heroku. 

## 📝Project  Pipline 
1. Batch files
2. Data validation
3. Data Transformation
4. Data Inserstion
5. Data Preprocessing 
6. Model creation 
7. Hyper parameter tunning.
8. Model Evaluation 
9. Deployment(CI/CD)
 
## ⚙️Architecture
<img width="639" alt="architecture" src="https://user-images.githubusercontent.com/75267160/181072348-cf703fc6-05ae-4ebb-8830-a5c38d6d5981.png">

## ⚒️Tools used 

<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://heroku.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a> <a href="https://symfony.com" target="_blank" rel="noreferrer">  </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a> </p>

## 🗂Documentation

[High Level Documentation(HLD)](https://github.com/Rakesh5699/creditcarddefaultprediction/blob/main/All%20Project%20Documents/HLD.pdf)

[Low Level Documentation(LLD))](https://github.com/Rakesh5699/creditcarddefaultprediction/blob/main/All%20Project%20Documents/LLD.pdf)

[Architecture Design](https://github.com/Rakesh5699/creditcarddefaultprediction/blob/main/All%20Project%20Documents/architecture%20design.pdf)

[Deatail Project Report(DPR)](https://github.com/Rakesh5699/creditcarddefaultprediction/blob/main/All%20Project%20Documents/Deatail%20Project%20Report.pdf)

[Wireframe_Documentaion](https://github.com/Rakesh5699/creditcarddefaultprediction/blob/main/All%20Project%20Documents/Wireframe_Documentaion.pdf)



## 🖼Create Virtual Environment:
Best practice of working on project is when we are working on any project it is recommended and safe to create env for that project. By using below command create a conda env
```
conda create -n creditcarddefaulprediction python=3.7
conda activate creditcarddefaulprediction 
```


## 📲Installation
After creating enviorment we need to run below command to install the required packages and libraries to run this project without any issue.
```
pip install -r requirements.txt
```
## 🗃Github repositoy :
We need to create a github repository. Please [click](https://docs.github.com/en/get-started/quickstart/create-a-repo) here to know how to create a github repository.


## 💻Environment Variables

To run this project as a CI/CD pipeline, you will need to add the following environment variables to CI/CD platform 

`HEROKU_EMAIL `

`HEROKU_API_KEY` 

`HEROKU_API_NAME`

## Deployment

To deploy this project we just need to push our code to our github repositoy.


```
git init 
git add .
git commit -m "first commit" 
git branch -M main 
git remote add origin <your_repo_https_link>
git push -u origin main 
```



## 📍Directory Tree

```
Credit-Card-Default-Predictions
│
├───.github
│   └───workflows
│           main.yaml
│
├───.idea
│   │   .gitignore
│   │   creditcarddefault.iml
│   │   misc.xml
│   │   modules.xml
│   │   vcs.xml
│   │   workspace.xml
│   │
│   └───inspectionProfiles
│           profiles_settings.xml
│           Project_Default.xml
│
├───.ipynb_checkpoints
│       Credit Card Default -checkpoint.ipynb
│
├───All Project Documents
│       architecture design.pdf
│       Deatail Project Report.pdf
│       HLD.pdf
│       LLD.pdf
│       Project demo video.mp4
│       Wireframe_Documentaion.pdf
│
├───application_logging
│   │   logger.py
│   │
│   └───__pycache__
│           logger.cpython-36.pyc
│           logger.cpython-37.pyc
│
├───best_model_finder
│   │   tuner.py
│   │
│   └───__pycache__
│           tuner.cpython-36.pyc
│           tuner.cpython-37.pyc
│
├───DataTransformation_Prediction
│   │   DataTransformationPrediction.py
│   │
│   └───__pycache__
│           DataTransformationPrediction.cpython-36.pyc
│           DataTransformationPrediction.cpython-37.pyc
│
├───DataTransform_Training
│   │   DataTransformation.py
│   │
│   └───__pycache__
│           DataTransformation.cpython-36.pyc
│           DataTransformation.cpython-37.pyc
│
├───DataTypeValidation_Insertion_Prediction
│   │   DataTypeValidationPrediction.py
│   │
│   └───__pycache__
│           DataTypeValidationPrediction.cpython-36.pyc
│           DataTypeValidationPrediction.cpython-37.pyc
│
├───DataTypeValidation_Insertion_Training
│   │   DataTypeValidation.py
│   │
│   └───__pycache__
│           DataTypeValidation.cpython-36.pyc
│           DataTypeValidation.cpython-37.pyc
│
├───data_ingestion
│   │   data_loader.py
│   │   data_loader_prediction.py
│   │
│   └───__pycache__
│           data_loader.cpython-36.pyc
│           data_loader.cpython-37.pyc
│           data_loader_prediction.cpython-36.pyc
│           data_loader_prediction.cpython-37.pyc
│
├───data_preprocessing
│   │   clustering.py
│   │   preprocessing.py
│   │
│   └───__pycache__
│           clustering.cpython-36.pyc
│           clustering.cpython-37.pyc
│           preprocessing.cpython-36.pyc
│           preprocessing.cpython-37.pyc
│           preprocessing_pred.cpython-36.pyc
│
├───file_operations
│   │   file_methods.py
│   │
│   └───__pycache__
│           file_methods.cpython-36.pyc
│           file_methods.cpython-37.pyc
│
├───models
│   ├───KMeans
│   │       KMeans.sav
│   │
│   ├───XGBoost0
│   │       XGBoost0.sav
│   │
│   ├───XGBoost1
│   │       XGBoost1.sav
│   │
│   ├───XGBoost2
│   │       XGBoost2.sav
│   │
│   └───XGBoost3
│           XGBoost3.sav
│
├───PredictionArchivedBadData
│   ├───BadData_2020-02-19_165637
│   ├───BadData_2020-02-19_173611
│   ├───BadData_2020-04-12_215100
│   │       creditCardFraud_28011961_12.csv
│   │       creditCardFraud_28011963_120213.csv
│   │
│   └───BadData_2022-07-26_230649
│           creditCardFraud_28011961_12.csv
│           creditCardFraud_28011963_120213.csv
│
├───Prediction_Batch_files
│       creditCardFraud_28011960_120210.csv
│       creditCardFraud_28011961_12.csv
│       creditCardFraud_28011962_120212.csv
│       creditCardFraud_28011963_120213.csv
│
├───Prediction_Database
│       Prediction.db
│
├───Prediction_FileFromDB
│       InputFile.csv
│
├───Prediction_Logs
│       columnValidationLog.txt
│       DataBaseConnectionLog.txt
│       dataTransformLog.txt
│       DbInsertLog.txt
│       DbTableCreateLog.txt
│       ExportToCsv.txt
│       GeneralLog.txt
│       missingValuesInColumn.txt
│       nameValidationLog.txt
│       Prediction_Log.txt
│
├───Prediction_Output_File
│       Predictions.csv
│
├───Prediction_Raw_Data_Validation
│   │   predictionDataValidation.py
│   │
│   └───__pycache__
│           predictionDataValidation.cpython-36.pyc
│           predictionDataValidation.cpython-37.pyc
│
├───Prediction_Raw_Files_Validated
│       sample.txt
│
├───preprocessing_data
│       K-Means_Elbow.PNG
│
├───SingleValueModels
│       rfc.pkl
│
├───SinglrValuePredictionLogs
│       SingleValuePredictionLogs.txt
│
├───static
│   ├───images
│   │       github.png
│   │       image4.gif
│   │       linkden.jpg
│   │       logo.jpg
│   │
│   └───styles
│           style.css
│
├───templates
│       index.html
│       prediction.html
│       result.html
│       singlevalueprediction.html
│       training.html
│
├───TrainingArchiveBadData
│   ├───BadData_2022-07-18_191749
│   │       CreditFraud_28011960_120210.xlsx
│   │       file_seperator.ipynb
│   │
│   └───BadData_2022-07-26_220500
│           CreditFraud_28011960_120210.xlsx
│           file_seperator.ipynb
│
├───Training_Batch_Files
│       creditCardFraud_28011960_120210.csv
│       creditCardFraud_28011961_120211.csv
│       creditCardFraud_28011962_120212.csv
│       creditCardFraud_28011963_120213.csv
│       creditCardFraud_28011964_120214.csv
│       CreditFraud_28011960_120210.xlsx
│       file_seperator.ipynb
│
├───Training_Database
│       Training.db
│
├───Training_FileFromDB
│
├───Training_Logs
│       columnValidationLog.txt
│       DataBaseConnectionLog.txt
│       dataTransformLog.txt
│       DbInsertLog.txt
│       DbTableCreateLog.txt
│       ExportToCsv.txt
│       GeneralLog.txt
│       missingValuesInColumn.txt
│       ModelTrainingLog.txt
│       nameValidationLog.txt
│       valuesfromSchemaValidationLog.txt
│
├───Training_Raw_data_validation
├───Training_Raw_files_validated
│   app.py
│   Credit Card Default .ipynb
│   Dockerfile
│   predictFromModel.py
│   prediction_Validation_Insertion.py
│   Procfile
│   requirements.txt
│   schema_prediction.json
│   schema_training.json
│   trainingModel.py
│   Training_Main_Log.txt
│   training_Validation_Insertion.py
│   tree.txt
│   UCI_Credit_Card.csv
```
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/Rakesh5699?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kasarla-rakesh-268b181b9)


## 🎎Team 

[Rakesh Kasarla](https://github.com/Rakesh5699?tab=repositories)


## 🎀Credits
The datasets has been provided by Kaggle. The original dataset can be found here at the UCI Machine Learning Repository. This project wouldn't have been possible without this dataset.

## ✒️Acknowledgement
A very special thanks to [ineuron.ai](https://ineuron.ai/) for providing opportunity like this. In this intenship i leanrt so many things. 


## 💻Application Link 

[Click here](https://creditcarddefault5699.herokuapp.com/)










