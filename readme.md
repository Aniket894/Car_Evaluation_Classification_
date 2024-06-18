# Car Evaluation Project Documentation


## Table of Contents

Introduction

Problem Statement

Dataset Description

Project Workflow

Data Preprocessing (EDA)

Model Building

Model Evaluation

References



## Introduction

This project aims to evaluate the acceptability of cars based on various attributes using the Car Evaluation dataset. 

The goal is to build a machine learning model that can predict the acceptability of a car given its features.


## Problem Statement

Given a set of car attributes, predict whether the car is acceptable, unacceptable, good, or very good.

The target variable is the acceptability of the car, and the features include various car characteristics.


## Dataset Description

The Car Evaluation dataset contains 1728 instances and 7 attributes. The attributes are as follows:

Buying: buying price (v-high, high, med, low)

Maint: maintenance price (v-high, high, med, low)

Doors: number of doors (2, 3, 4, 5-more)

Persons: capacity in terms of persons to carry (2, 4, more)

Lug_boot: the size of luggage boot (small, med, big)

Safety: estimated safety of the car (low, med, high)

Class: car acceptability (unacc, acc, good, v-good)




## Project Workflow

Data Preprocessing (EDA)

Feature Engineering

Model Building

Model Evaluation




## Data Preprocessing (EDA)

Data preprocessing involves read csv file of car_evaluation.csv 

Encoded the categorical columns using label encoder 

Split the data set into independent and dependent features 

Split the features into train_test_split



## Model Building

Several machine learning models will be built and compared, including  Logistic Regression, Decision Trees, Random Forest, Gradient Boosting and XGboost 



## Model Evaluation

The performance of the models is evaluated based on accuracy and classification reports.

You can see different models accuracy in this bar chart.

Gradient Boosting Classifier Top in the chart with a bar of 97% accuracy.

![download (2)](https://github.com/Aniket894/Car_Evaluation_Classification_/assets/134599961/e82c32de-b49e-4c07-b859-0ce8d95f995b)



## References

Car Evaluation Dataset: https://archive.ics.uci.edu/dataset/19/car+evaluation


## Flask File Structure

flask_app/

│

└── notebooks

│         ├── Evaluation_Bar_Chart.jpg
    
│         ├── Car_Evaluation.ipynb
    
│         └── gradient.pkl

├── app.py

├── templates/

│         ├── index.html

│         └── results.html

├── static/

│         └── styles.css


