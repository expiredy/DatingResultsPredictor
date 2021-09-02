import tensorflow as tf
import numpy
import requests
import matplotlib.pyplot as plt


RANDOM_NP = numpy.random
TESTING_DATA_SET_PATH = "SpeedDatingData.csv"

LEARNING_RATE = 0.02
TRAINING_EPOCHS = 3000

display_step = 50

def get_data_from_excel_file(data_path):
    import pandas
    parsed_data = pandas.read_csv(data_path)
    return parsed_data


data_set = get_data_from_excel_file(TESTING_DATA_SET_PATH)