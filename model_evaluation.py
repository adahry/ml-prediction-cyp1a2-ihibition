# -*- coding: utf-8 -*-
"""model_evaluation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MY4bS6yoDgIx5jKOU0EnjDFkIRIGw0EK
"""

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import matplotlib.pyplot as plt

def score_dataframe(test_dataset, model):
  cols = ['pred', 'real']
  df = pd.DataFrame(columns=cols, index=range(len(test_dataset)))

  for i, batch in enumerate(test_dataset):

      pred = model(batch.x.float(), batch.edge_index,batch.edge_attr ,batch.batch)

      #df.loc[i].pred = pred[0].tolist()
      df.loc[i].real = batch.y.tolist()


      if pred[0].tolist()[0] < 0.5:
        df.loc[i].pred = [0.0]
      else:
        df.loc[i].pred = [1.0]

  return df


def accuracy(df):
  good = 0
  all = len(df)
  for i in range(len(df)):
    if df.loc[i].pred == df.loc[i].real:
      good += 1

  print('accuracy:', round(good/all *100, 2) , '%')


def plot_conf_matrix(df):
  cm = confusion_matrix(df['real'].values.tolist(), df['pred'].values.tolist())
  disp = ConfusionMatrixDisplay(confusion_matrix=cm)
  disp.plot(cmap=plt.cm.summer)
  plt.show()