""" Functions for analysis of literature
"""

import itertools
import re

import pandas as pd


def find_columns(data, regex):
    """ Find columns matching a regular expression

    :param data: Dataframe containing all dimension and all articles
    :param regex: Regular expression describing the dimensions of interest
    :return: A list of dimensions covered in the dataframe matching the regular expression
    """
    columns = [x for x in data.columns.tolist() if re.match(regex, x)]
    columns.sort()
    return columns


def check_columns(columns, dict_list):
    """ Check if all columns of a topic are assigned to a dictionary

    :param columns: List of columns that need to be assigned
    :param dict_list: List of dictionaries that assign columns to dimensions
    """
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
    """ Assigns citation keys to topics from a list of dictionaries

    :param data: Dataframe containing all dimension and all articles
    :param dict_list:  List of dictionaries that assign columns to dimensions
    :return: Dictionary that assigns each dimension the matching citation keys
    """
    category_dic = {}
    for d in dict_list:
        category_dic.update(d)
    citation_key_dic = {}
    for key in category_dic:
        data_column_of_interest = data[["citation_key"] + category_dic[key]]
        data_of_interest = data_column_of_interest[data_column_of_interest[category_dic[key]].notna().any(axis=1)]
        relevant_articles = data_of_interest.citation_key.drop_duplicates()
        citation_key_dic[key] = key + " & \\cite{" + ', '.join(relevant_articles.values.tolist()) + "}\\"
    return citation_key_dic


def analyse_dimension(data, topic):
    """ Summarize the meta dimensions and results for a given hypothesis

    :param data:  Dataframe containing all dimension and all articles
    :param topic: Dimension that should be analysed
    """
    print("Summary of the hypothesis decisions")
    print(data.groupby(topic).size())
    print("\n")
    print("Summary of the influence of the survey country")
    print(pd.crosstab(data['survey_country'], data[topic], margins=False))
    print("\n")
    print("Summary of the influence of the survey operator")
    print(pd.crosstab(data['survey_operator'], data[topic], margins=False))
    print("\n")
    print("Summary of the influence of the survey year")
    print(pd.crosstab(data['survey_year'], data[topic], margins=False))
    print("\n")
    print("Summary of the influence of an design adapted for mobile devices")
    print(pd.crosstab(data['survey_design_mobile_adapted'], data[topic], margins=False))
    print("\n")
    print("Summary of the influence of the survey population")
    print(pd.crosstab(data['survey_population'], data[topic], margins=False))
    print("\n")
