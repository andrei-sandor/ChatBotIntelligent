import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import numpy
import joblib
from sklearn.model_selection import train_test_split


dataset = pd.read_csv("grades_csv.csv")
print(dataset)

#### Linear regression
X = pd.DataFrame()
X["Exam2"] = dataset["exam2"]

y = pd.DataFrame()
y['course_grade'] = dataset['course_grade']

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model_linear_regression = tf.keras.Sequential([layers.Dense(units=1)])
model_linear_regression.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),loss='mse')
history = model_linear_regression.fit(X_train,y_train,batch_size=16,epochs=101,validation_split=0.3,verbose=False)

joblib.dump(model_linear_regression, 'regression_model_grade2.joblib')

#### Regression DNN
X = pd.DataFrame()
X["Exam2"] = dataset["exam2"]

y = pd.DataFrame()
y['course_grade'] = dataset['course_grade']

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model_dnn = keras.Sequential([
  layers.Dense(64, activation='relu'),
  layers.Dense(64, activation='relu'),
  layers.Dense(1)
])

model_dnn.compile(loss='mean_absolute_error',
            optimizer=tf.keras.optimizers.Adam(0.001))

history = model_dnn.fit(X_train,y_train,batch_size=16,epochs=101,validation_split=0.3,verbose=False)

joblib.dump(model_dnn, 'model_dnn_grade2.joblib')

#### DNN part 2
X = pd.DataFrame()
X["Exam2"] = dataset["exam2"]

y = pd.DataFrame()
y['course_grade'] = dataset['course_grade']

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


model_dnn2 = tf.keras.Sequential([
      tf.keras.layers.Dense(64, activation='relu'),
      tf.keras.layers.Dense(32, activation='sigmoid'),
      tf.keras.layers.Dense(16, activation='sigmoid'),
      tf.keras.layers.Dense(8, activation='relu'),
      layers.Dense(1)


  ])

model_dnn2.compile(loss='mean_absolute_error',
            optimizer=tf.keras.optimizers.Adam(0.001),
                metrics=[keras.metrics.CategoricalAccuracy()])


history = model_dnn2.fit(X_train,y_train,batch_size=16,epochs=101,validation_split=0.3,verbose=False)
print(history)

joblib.dump(model_dnn2, 'model_dnn2_grade2.joblib')



