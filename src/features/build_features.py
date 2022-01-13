import itertools
import re

import pandas as pd


def find_columns(data, regex):
    columns = [x for x in data.columns.tolist() if re.match(regex, x)]
    columns.sort()
    return columns


def check_columns(columns, dict_list):
    category_dic = {}
    for d in dict_list:
        category_dic.update(d)
    already_assigned_list = list(itertools.chain.from_iterable(list(category_dic.values())))
    not_used_columns = [x for x in columns if x not in already_assigned_list]
    if not not_used_columns:
        print("All columns of this topic are assigned.")
    else:
        print(not_used_columns)


def find_citation_key_topics(data, dict_list):
    category_dic = {}
    for d in dict_list:
        category_dic.update(d)
    citation_key_dic = {}
    for key in category_dic:
        data_column_of_interest = data[["citation_key"] + category_dic[key]]
        data_of_interest = data_column_of_interest[data_column_of_interest[category_dic[key]].notna().any(axis=1)]
        relevant_articles = data_of_interest.citation_key.drop_duplicates()
        citation_key_dic[key] = key + " & \cite{" + ', '.join(relevant_articles.values.tolist()) + "}\\"
    return citation_key_dic

def analyse_dimension(data, topic):
    print("Summary of the hypothesis decisions")
    print(data.groupby(topic).size())
    print("\n")
    print("Summary of the influence of the survey country")
    print(pd.crosstab(data['survey_country'],data[topic],margins = False))
    print("\n")
    print("Summary of the influence of the survey operator")
    print(pd.crosstab(data['survey_operator'],data[topic],margins = False))
    print("\n")
    print("Summary of the influence of the survey year")
    print(pd.crosstab(data['survey_year'],data[topic],margins = False))
    print("\n")
    print("Summary of the influence of an design adapted for mobile devices")
    print(pd.crosstab(data['survey_design_mobile_adapted'],data[topic],margins = False))
    print("\n")
    print("Summary of the influence of the survey population")
    print(pd.crosstab(data['survey_population'],data[topic],margins = False))
    print("\n")