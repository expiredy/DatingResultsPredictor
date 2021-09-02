import numpy
import tensorflow as tf
import json
from DictKeyConfig import *
from StructureObjects import UnitsDataHolder
import matplotlib.pyplot as plt

all_data_keys = [IID_KEY, ID_KEY, GENDER_KEY, IDG_KEY, CONDTN_KEY, WAVE_KEY, ROUND_KEY,
                 POSITION_KEY, POSITIN1_KEY, ORDER_KEY, PARTNER_KEY, PID_KEY, MATCH_KEY,
                 INT_CORR_KEY, SAMERACE_KEY, AGE_O_KEY, RACE_O_KEY, PF_O_ATT_KEY,
                 PF_O_SIN_KEY, PF_O_INT_KEY, PF_O_FUN_KEY, PF_O_AMB_KEY, PF_O_SHA_KEY,
                 DEC_O_KEY, ATTR_O_KEY, SINC_O_KEY, INTEL_O_KEY, FUN_O_KEY, AMB_O_KEY,
                 SHAR_O_KEY, LIKE_O_KEY, PROB_O_KEY, MET_O_KEY, AGE_KEY, FIELD_KEY,
                 FIELD_CD_KEY, UNDERGRA_KEY, MN_SAT_KEY, TUITION_KEY, RACE_KEY, IMPRACE_KEY,
                 IMPRELIG_KEY, FROM_KEY, ZIPCODE_KEY, INCOME_KEY, GOAL_KEY, DATE_KEY,
                 GO_OUT_KEY, CAREER_KEY, CAREER_C_KEY, SPORTS_KEY, TVSPORTS_KEY,
                 EXERCISE_KEY, DINING_KEY, MUSEUMS_KEY, ART_KEY, HIKING_KEY, GAMING_KEY,
                 CLUBBING_KEY, READING_KEY, TV_KEY, THEATER_KEY, MOVIES_KEY, CONCERTS_KEY,
                 MUSIC_KEY, SHOPPING_KEY, YOGA_KEY, EXPHAPPY_KEY, EXPNUM_KEY, ATTR1_1_KEY,
                 SINC1_1_KEY, INTEL1_1_KEY, FUN1_1_KEY, AMB1_1_KEY, SHAR1_1_KEY, ATTR4_1_KEY,
                 SINC4_1_KEY, INTEL4_1_KEY, FUN4_1_KEY, AMB4_1_KEY, SHAR4_1_KEY, ATTR2_1_KEY,
                 SINC2_1_KEY, INTEL2_1_KEY, FUN2_1_KEY, AMB2_1_KEY, SHAR2_1_KEY, ATTR3_1_KEY,
                 SINC3_1_KEY, FUN3_1_KEY, INTEL3_1_KEY, AMB3_1_KEY, ATTR5_1_KEY, SINC5_1_KEY,
                 INTEL5_1_KEY, FUN5_1_KEY, AMB5_1_KEY, DEC_KEY, ATTR_KEY, SINC_KEY, INTEL_KEY,
                 FUN_KEY, AMB_KEY, SHAR_KEY, LIKE_KEY, PROB_KEY, MET_KEY, MATCH_ES_KEY,
                 ATTR1_S_KEY, SINC1_S_KEY, INTEL1_S_KEY, FUN1_S_KEY, AMB1_S_KEY, SHAR1_S_KEY,
                 ATTR3_S_KEY, SINC3_S_KEY, INTEL3_S_KEY, FUN3_S_KEY, AMB3_S_KEY, SATIS_2_KEY,
                 LENGTH_KEY, NUMDAT_2_KEY, ATTR7_2_KEY, SINC7_2_KEY, INTEL7_2_KEY, FUN7_2_KEY,
                 AMB7_2_KEY, SHAR7_2_KEY, ATTR1_2_KEY, SINC1_2_KEY, INTEL1_2_KEY, FUN1_2_KEY,
                 AMB1_2_KEY, SHAR1_2_KEY, ATTR4_2_KEY, SINC4_2_KEY, INTEL4_2_KEY, FUN4_2_KEY,
                 AMB4_2_KEY, SHAR4_2_KEY, ATTR2_2_KEY, SINC2_2_KEY, INTEL2_2_KEY, FUN2_2_KEY,
                 AMB2_2_KEY, SHAR2_2_KEY, ATTR3_2_KEY, SINC3_2_KEY, INTEL3_2_KEY, FUN3_2_KEY,
                 AMB3_2_KEY, ATTR5_2_KEY, SINC5_2_KEY, INTEL5_2_KEY, FUN5_2_KEY, AMB5_2_KEY,
                 YOU_CALL_KEY, THEM_CAL_KEY, DATE_3_KEY, NUMDAT_3_KEY, NUM_IN_3_KEY,
                 ATTR1_3_KEY, SINC1_3_KEY, INTEL1_3_KEY, FUN1_3_KEY, AMB1_3_KEY, SHAR1_3_KEY,
                 ATTR7_3_KEY, SINC7_3_KEY, INTEL7_3_KEY, FUN7_3_KEY, AMB7_3_KEY, SHAR7_3_KEY,
                 ATTR4_3_KEY, SINC4_3_KEY, INTEL4_3_KEY, FUN4_3_KEY, AMB4_3_KEY, SHAR4_3_KEY,
                 ATTR2_3_KEY, SINC2_3_KEY, INTEL2_3_KEY, FUN2_3_KEY, AMB2_3_KEY, SHAR2_3_KEY,
                 ATTR3_3_KEY, SINC3_3_KEY, INTEL3_3_KEY, FUN3_3_KEY, AMB3_3_KEY, ATTR5_3_KEY,
                 SINC5_3_KEY, INTEL5_3_KEY, FUN5_3_KEY, AMB5_3_KEY]
print([key.upper() + "_KEY" for key in all_data_keys])

RANDOM_NP = numpy.random
TESTING_DATA_SET_PATH = "SpeedDatingData.xls"
PARSED_DATA_SET_SAVING_PATH = "SpeedDatingData.json"

LEARNING_RATE = 0.02
TRAINING_EPOCHS = 3000

display_step = 50


def get_data_from_excel_file(data_path, force_data_set_update=False):
    try:
        with open(PARSED_DATA_SET_SAVING_PATH, "r") as fp:
            if not force_data_set_update:
                return json.load(fp)
            raise BaseException
    except BaseException:
        import pandas
        parsed_data = pandas.read_excel(data_path)
        np_sorted_parsed_data = {element_key: parsed_data[element_key].values for element_key in all_data_keys}
        with open(PARSED_DATA_SET_SAVING_PATH, "w") as fp:
            data = {key: np_sorted_parsed_data[key].ravel().tolist() for key in all_data_keys}
            fp.write(json.dumps(data))
        return data


def link_current_data_set_to_units(data_set):
    for unit_id in range(len(data_set[all_data_keys[0]])):
        yield UnitsDataHolder(*[data_set[key][unit_id] for key in all_data_keys])


data_set = get_data_from_excel_file(TESTING_DATA_SET_PATH)
tf.compat.v1.disable_eager_execution()
units = list(link_current_data_set_to_units(data_set))
print(units)
vectors_data_set = {}
for key in all_data_keys:
    data_type_from_set = str(list(set([type(element) for element in data_set[key]]))[0]).replace("<class '", "")\
        .replace("'>", "")
    vectors_data_set[key] = {MAIN_NP_DATA_KEY: numpy.asarray(data_set[key]),
                             TENSORFLOW_PLACE_HOLDER_KEY: tf.compat.v1.placeholder(
                             data_type_from_set.replace("int", "float").replace("str", "string")),
                             NEURON_WEIGHT_KEY: tf.Variable(RANDOM_NP.randn(), name="weight"),
                             NEURON_BIAS_KEY: tf.Variable(RANDOM_NP.randn(), name="bias")}

n_samples = vectors_data_set[all_data_keys[0]][MAIN_NP_DATA_KEY].shape[0]
print(n_samples)

initialized_variables = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as current_session:
    current_session.run(initialized_variables)
    for unit_id in range(len(units)):
        final_data_set = units[unit_id].get_data_of_unit_for_match()
        estimated_data_set = units[unit_id].get_units_score()