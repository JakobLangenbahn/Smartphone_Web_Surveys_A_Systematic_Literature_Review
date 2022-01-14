""" Function for the preperation of visualisations
"""

import pandas as pd


def create_visualisation_data(data, topic_dic):
    """ Preperation of visualisation data

    :param data: Dataframe containing all dimension and all articles
    :param topic_dic: Dictionary with topics
    :return: Data for visualition
    """

    def transform_into_vec(data, topic, name):
        """

        :param data: Dataframe containing all dimension and all articles
        :param topic: Specific topic that should be assigned a year vector
        :param name: Assigned name for the topic
        :return: Vector containing the publication years for a topic
        """
        relevant_data = data[["article_year", topic]][data[topic]]
        relevant_data["Topic"] = name
        return relevant_data.drop(topic, axis=1)

    topic_df_list = []
    for key in topic_dic:
        topic_df_list.append(transform_into_vec(data, topic_dic[key], key))
    all_articles = data[["article_year"]]
    all_articles["Topic"] = "All Publications"
    topic_df_list.append(all_articles)
    result = pd.concat(topic_df_list).rename(columns={"article_year": "Year"})
    return result
