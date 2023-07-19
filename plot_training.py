# -*- coding: utf-8 -*-
"""plot_training.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qsa4dOh4n9LuTLn8U1NCyZ3BCYB7-ylU
"""

import matplotlib.pyplot as plt

def plot_training(train_loss, val_loss):
  plt.plot(train_loss, label= 'training')
  plt.plot(val_loss, label= 'validation')
  plt.xlabel('epoch')
  plt.ylabel('loss')
  plt.legend()