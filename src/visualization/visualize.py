import pandas as pd

def create_visualisation_data(data, topic_dic):
    def transform_into_vec(data, topic, name):
        relevant_data = data[["article_year", topic]][data[topic]]
        relevant_data["Topic"] = name
        return relevant_data.drop(topic, axis = 1)
    topic_df_list = []
    for key in topic_dic:
        topic_df_list.append(transform_into_vec(data, topic_dic[key], key))
    all_articles = data[["article_year"]]
    all_articles["Topic"] = "All Publications"
    topic_df_list.append(all_articles)
    result = pd.concat(topic_df_list).rename(columns = {"article_year": "Year"})
    return result