def create_data_set(df, topic):
    interesting_columns = ["survey_year","survey_participants_number",
                           "survey_country", "survey_operator",
                           "survey_population","survey_design_mobile_adapted", ]
    interesting_columns.append(topic)
    df_columns = df[interesting_columns]
    df_of_interest = df_columns[df_columns[topic].notna()]
    write_location = "../data/processed/" + topic + ".xlsx"
    df_of_interest.to_excel(write_location, index=False)
    return df_of_interest