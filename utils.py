import json


def json_builder(df, feature=None):
    '''
    Builds the JSON from the DataFrame for the Columns.
    :param df: DataFrame
    :param feature: Column Name
    :return:
    '''
    # if feature:
    #     feature = json.loads(df.to_json())
    #     return feature
    # else:
    df = json.loads(df.to_json())
    return df


def data_organiser(aggregate, df, x_feature=None, y_feature=None, feature=None):

    if feature:
        feature_data = json_builder(df[feature])
        df_data = {'Name': feature,
                   'Aggregate': aggregate,
                   'Data': feature_data}

    else:
        if x_feature != y_feature:
            feature_data = json_builder(df[[x_feature,y_feature]])
        else:
            feature_data = json_builder(df[x_feature])

        df_data = {'X_Feature': x_feature,
                   'Y_Feature': y_feature,
                   'Aggregate': aggregate,
                   'Data': feature_data}
    return df_data
