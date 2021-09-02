import tensorflow as tf
import numpy
import tensorflow as tf
import json
from StructureObjects import UnitsDataHolder
from DictKeyConfig import *
import matplotlib.pyplot as plt

all_data_keys = ["iid", "id", "gender", "idg", "condtn", "wave", "round", "position", "positin1", "order", "partner",
                 "pid", "match", "int_corr", "samerace", "age_o", "race_o", "pf_o_att", "pf_o_sin", "pf_o_int",
                 "pf_o_fun", "pf_o_amb", "pf_o_sha", "dec_o", "attr_o", "sinc_o", "intel_o", "fun_o", "amb_o",
                 "shar_o", "like_o", "prob_o", "met_o", "age", "field", "field_cd", "undergra", "mn_sat", "tuition",
                 "race", "imprace", "imprelig", "from", "zipcode", "income", "goal", "date", "go_out", "career",
                 "career_c", "sports", "tvsports", "exercise", "dining", "museums", "art", "hiking", "gaming",
                 "clubbing", "reading", "tv", "theater", "movies", "concerts", "music", "shopping", "yoga", "exphappy",
                 "expnum", "attr1_1", "sinc1_1", "intel1_1", "fun1_1", "amb1_1", "shar1_1", "attr4_1", "sinc4_1",
                 "intel4_1", "fun4_1", "amb4_1", "shar4_1", "attr2_1", "sinc2_1", "intel2_1", "fun2_1", "amb2_1",
                 "shar2_1", "attr3_1", "sinc3_1", "fun3_1", "intel3_1", "amb3_1", "attr5_1", "sinc5_1", "intel5_1",
                 "fun5_1", "amb5_1", "dec", "attr", "sinc", "intel", "fun", "amb", "shar", "like", "prob", "met",
                 "match_es", "attr1_s", "sinc1_s", "intel1_s", "fun1_s", "amb1_s", "shar1_s", "attr3_s", "sinc3_s",
                 "intel3_s", "fun3_s", "amb3_s", "satis_2", "length", "numdat_2", "attr7_2", "sinc7_2", "intel7_2",
                 "fun7_2", "amb7_2", "shar7_2", "attr1_2", "sinc1_2", "intel1_2", "fun1_2", "amb1_2", "shar1_2",
                 "attr4_2", "sinc4_2", "intel4_2", "fun4_2", "amb4_2", "shar4_2", "attr2_2", "sinc2_2", "intel2_2",
                 "fun2_2", "amb2_2", "shar2_2", "attr3_2", "sinc3_2", "intel3_2", "fun3_2", "amb3_2", "attr5_2",
                 "sinc5_2", "intel5_2", "fun5_2", "amb5_2", "you_call", "them_cal", "date_3", "numdat_3", "num_in_3",
                 "attr1_3", "sinc1_3", "intel1_3", "fun1_3", "amb1_3", "shar1_3", "attr7_3", "sinc7_3", "intel7_3",
                 "fun7_3", "amb7_3", "shar7_3", "attr4_3", "sinc4_3", "intel4_3", "fun4_3", "amb4_3", "shar4_3",
                 "attr2_3", "sinc2_3", "intel2_3", "fun2_3", "amb2_3", "shar2_3", "attr3_3", "sinc3_3", "intel3_3",
                 "fun3_3", "amb3_3", "attr5_3", "sinc5_3", "intel5_3", "fun5_3", "amb5_3"]

RANDOM_NP = numpy.random
TESTING_DATA_SET_PATH = "SpeedDatingData.xls"
PARSED_DATA_SET_SAVING_PATH = "SpeedDatingData.json"

LEARNING_RATE = 0.02
TRAINING_EPOCHS = 3000

display_step = 50


def get_data_from_excel_file(data_path, force_data_set_update=False):
    try:
        with open(PARSED_DATA_SET_SAVING_PATH, "r") as fp:
            return json.load(fp)
    except BaseException:
        import pandas
        parsed_data = pandas.read_excel(data_path)
        np_sorted_parsed_data = {element_key: parsed_data[element_key].values for element_key in all_data_keys}
        with open(PARSED_DATA_SET_SAVING_PATH, "w") as fp:
            data = {key: np_sorted_parsed_data[key].ravel().tolist() for key in all_data_keys}
            fp.write(json.dumps(data))
        return data


data_set = get_data_from_excel_file(TESTING_DATA_SET_PATH)


for key in all_data_keys:
    data_type_from_set = str(list(set([type(element) for element in data_set[key]])))
    print(data_type_from_set)
    vectors_data_set = {key: {MAIN_NP_DATA: numpy.asarray(data_set[key]),
                              TENSORFLOW_PLACE_HOLDER: tf.placeholder(data_type_from_set)}}
