""" Function for the creation of helpful datasets
"""


def create_data_set(df, topic):
    """ Create data set for further analyses of specific dimensions.

    :param df: Dataframe containing all dimension and all articles
    :param topic: Topic of interest
    :return: Dataframe containing all meta data and the results for the topic for the concerned articles
    """
    interesting_columns = ["survey_year", "survey_participants_number", "survey_country", "survey_operator",
                           "survey_population", "survey_design_mobile_adapted", topic]
    df_columns = df[interesting_columns]
    df_of_interest = df_columns[df_columns[topic].notna()]
    write_location = "../data/processed/" + topic + ".xlsx"
    df_of_interest.to_excel(write_location, index=False)
    return df_of_interest
