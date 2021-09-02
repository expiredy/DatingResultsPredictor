class UnitsDataHolder:
    def __init__(self, iid, id, gender, idg, condtn, wave, round, position, positin1, order, partner, pid, match,
                 int_corr, samerace, age_o, race_o, pf_o_att, pf_o_sin, pf_o_int, pf_o_fun, pf_o_amb, pf_o_sha,
                 dec_o, attr_o, sinc_o, intel_o, fun_o, amb_o, shar_o, like_o, prob_o, met_o, age, field, field_cd,
                 undergra, mn_sat, tuition, race, imprace, imprelig, from_,
                 zipcode, income, goal, date, go_out, career, career_c, sports, tvsports, exercise, dining, museums,
                 art, hiking, gaming, clubbing, reading, tv, theater, movies, concerts, music, shopping, yoga,
                 exphappy, expnum, attr1_1, sinc1_1, intel1_1, fun1_1, amb1_1, shar1_1, attr4_1, sinc4_1, intel4_1,
                 fun4_1, amb4_1, shar4_1, attr2_1, sinc2_1, intel2_1, fun2_1, amb2_1, shar2_1, attr3_1, sinc3_1,
                 fun3_1, intel3_1, amb3_1, attr5_1, sinc5_1, intel5_1, fun5_1, amb5_1, dec, attr, sinc, intel,
                 fun, amb, shar, like, prob, met, match_es, attr1_s, sinc1_s, intel1_s, fun1_s, amb1_s, shar1_s,
                 attr3_s, sinc3_s, intel3_s, fun3_s, amb3_s, satis_2, length, numdat_2, attr7_2, sinc7_2, intel7_2,
                 fun7_2, amb7_2, shar7_2, attr1_2, sinc1_2, intel1_2, fun1_2, amb1_2, shar1_2, attr4_2, sinc4_2,
                 intel4_2, fun4_2, amb4_2, shar4_2, attr2_2, sinc2_2, intel2_2, fun2_2, amb2_2, shar2_2, attr3_2,
                 sinc3_2, intel3_2, fun3_2, amb3_2, attr5_2, sinc5_2, intel5_2, fun5_2, amb5_2, you_call, them_cal,
                 date_3, numdat_3, num_in_3, attr1_3, sinc1_3, intel1_3, fun1_3, amb1_3, shar1_3, attr7_3, sinc7_3,
                 intel7_3, fun7_3, amb7_3, shar7_3, attr4_3, sinc4_3, intel4_3, fun4_3, amb4_3, shar4_3, attr2_3,
                 sinc2_3, intel2_3, fun2_3, amb2_3, shar2_3, attr3_3, sinc3_3, intel3_3, fun3_3, amb3_3, attr5_3,
                 sinc5_3, intel5_3, fun5_3, amb5_3):
        self.unique_subject_number = iid
        self.subject_id_in_wave = id
        self.gender_id = gender
        self.subject_id_within_gender = idg
        self.condition_of_choice = condtn
        self.dating_wave_id = wave
        self.number_of_met_people = round
        self.met_place_position_number = position
        self.dating_start_position_number = positin1
        self.number_of_data_that_night = order
        self.partner_id_by_night_of_events = partner
        self.iid_number_of_number = pid
        self.is_match_choice = match
        self.correlation_between_participant_and_partner_ratings_of_interests_time_1 = int_corr
        self.is_partners_have_same_rice_choice = samerace
        self.age_of_partner = age_o
        self.race_of_partner = race_o
        self.preferences_of_partner = pf_o_att
        self.decision_of_partner_night_of_even = dec_o
        self.rating_by_partner_night_of_even = attr_o
        self.age = age
        self.name_of_field_of_study = field
        self.coded_field_of_study_id = field_cd
        self.school_grade = undergra
        self.median_SAT_score = mn_sat
        self.tuition_listed_for_each_response_to_undergrad = tuition
        self.human_race_number = race
        self.how_much_caring_for_race = imprace
        self.how_much_caring_for_religious = imprelig
        self.native_country = from_
        self.post_code_od_your_native_country = zipcode
        self.median_household_based_on_zipcode = income
        self.what_is_your_purpose_id = goal
        self.dating_rate_id = date
        self.how_often_go_out_id = go_out
        self.career_name = career
        self.coded_career_name_id = career_c
        self.sports = sports
        self.tvsports = tvsports
        self.excersice = exercise
        self.dining = dining
        self.museums = museums
        self.art = art
        self.hiking = hiking
        self.gaming = gaming
        self.clubbing = clubbing
        self.reading = reading
        self.tv = tv
        self.theater = theater
        self.movies = movies
        self.concerts = concerts
        self.music = music
        self.shopping = shopping
        self.yoga = yoga
        self.rate_your_happiness_expectations = exphappy
        self.rate_expectation_number_of_people_who_will_dating_unit = expnum
        self.pf_o_sin, self.pf_o_int, self.pf_o_fun, self.pf_o_amb, self.pf_o_sha\
            = pf_o_sin, pf_o_int, pf_o_fun, pf_o_amb, pf_o_sha,
        self.sinc_o, self.intel_o, self.fun_o, self.amb_o, self.shar_o, self.like_o, self.prob_o, self.met_o\
            = sinc_o, intel_o, fun_o, amb_o, shar_o, like_o, prob_o, met_o

        self.attr1_1, self.sinc1_1, self.intel1_1, self.fun1_1, self.amb1_1, self.shar1_1, self.attr4_1,\
        self.sinc4_1, self.intel4_1, self.fun4_1, self.amb4_1, self.shar4_1, self.attr2_1, self.sinc2_1,\
        self.intel2_1, self.fun2_1, self.amb2_1, self.shar2_1, self.attr3_1, self.sinc3_1, self.fun3_1, self.intel3_1,\
        self.amb3_1, self.attr5_1, self.sinc5_1, self.intel5_1, self.fun5_1, self.amb5_1, self.dec, self.attr,\
        self.sinc, self.intel, self.fun, self.amb, self.shar, self.like, self.prob, self.met, self.match_es,\
        self.attr1_s, self.sinc1_s, self.intel1_s, self.fun1_s, self.amb1_s, self.shar1_s, self.attr3_s, self.sinc3_s,\
        self.intel3_s, self.fun3_s, self.amb3_s, self.satis_2, self.length, self.numdat_2, self.attr7_2, self.sinc7_2,\
        self.intel7_2, self.fun7_2, self.amb7_2, self.shar7_2, self.attr1_2, self.sinc1_2, self.intel1_2, self.fun1_2,\
        self.amb1_2, self.shar1_2, self.attr4_2, self.sinc4_2, self.intel4_2, self.fun4_2, self.amb4_2, self.shar4_2,\
        self.attr2_2, self.sinc2_2, self.intel2_2, self.fun2_2, self.amb2_2, self.shar2_2, self.attr3_2, self.sinc3_2,\
        self.intel3_2, self.fun3_2, self.amb3_2, self.attr5_2, self.sinc5_2, self.intel5_2, self.fun5_2, self.amb5_2,\
        self.you_call, self.them_cal, self.date_3, self.numdat_3, self.num_in_3, self.attr1_3, self.sinc1_3,\
        self.intel1_3, self.fun1_3, self.amb1_3, self.shar1_3, self.attr7_3, self.sinc7_3, self.intel7_3, self.fun7_3,\
        self.amb7_3, self.shar7_3, self.attr4_3, self.sinc4_3, self.intel4_3, self.fun4_3, self.amb4_3, self.shar4_3,\
        self.attr2_3, self.sinc2_3, self.intel2_3, self.fun2_3, self.amb2_3, self.shar2_3, self.attr3_3, self.sinc3_3,\
        self.intel3_3, self.fun3_3, self.amb3_3, self.attr5_3, self.sinc5_3, self.intel5_3, self.fun5_3, self.amb5_3\
            = attr1_1, sinc1_1, intel1_1, fun1_1, amb1_1, shar1_1, attr4_1, sinc4_1, intel4_1,\
                 fun4_1, amb4_1, shar4_1, attr2_1, sinc2_1, intel2_1, fun2_1, amb2_1, shar2_1, attr3_1, sinc3_1,\
                 fun3_1, intel3_1, amb3_1, attr5_1, sinc5_1, intel5_1, fun5_1, amb5_1, dec, attr, sinc, intel,\
                 fun, amb, shar, like, prob, met, match_es, attr1_s, sinc1_s, intel1_s, fun1_s, amb1_s, shar1_s,\
                 attr3_s, sinc3_s, intel3_s, fun3_s, amb3_s, satis_2, length, numdat_2, attr7_2, sinc7_2, intel7_2,\
                 fun7_2, amb7_2, shar7_2, attr1_2, sinc1_2, intel1_2, fun1_2, amb1_2, shar1_2, attr4_2, sinc4_2,\
                 intel4_2, fun4_2, amb4_2, shar4_2, attr2_2, sinc2_2, intel2_2, fun2_2, amb2_2, shar2_2, attr3_2,\
                 sinc3_2, intel3_2, fun3_2, amb3_2, attr5_2, sinc5_2, intel5_2, fun5_2, amb5_2, you_call, them_cal,\
                 date_3, numdat_3, num_in_3, attr1_3, sinc1_3, intel1_3, fun1_3, amb1_3, shar1_3, attr7_3, sinc7_3,\
                 intel7_3, fun7_3, amb7_3, shar7_3, attr4_3, sinc4_3, intel4_3, fun4_3, amb4_3, shar4_3, attr2_3,\
                 sinc2_3, intel2_3, fun2_3, amb2_3, shar2_3, attr3_3, sinc3_3, intel3_3, fun3_3, amb3_3, attr5_3,\
                 sinc5_3, intel5_3, fun5_3, amb5_3


class DatingWaveDataHolder:
    pass