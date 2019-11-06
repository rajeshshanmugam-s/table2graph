import json
import pandas as pd


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
    df = json.loads(df.to_json(orient='records'))
    return df


def data_organiser(chart, df, x_feature=None, y_feature=None, feature=None):

    if feature:
        if chart == 'piechart' or chart == 'barchart':
            x_feature_data, y_feature_data = groupby_frame_generator(df,feature)
            df_data = {
                'Title': feature,
                'Label': {'x': feature,
                          'y': 'Count'},
                'values': {'x': x_feature_data,
                           'y': y_feature_data},
                'Legends': {0: feature,
                            1: 'Count'}
            }

    else:
        if x_feature != y_feature:
            x_feature_data = json_builder(df[x_feature])
            y_feature_data = json_builder(df[y_feature])

            df_data = {
                'Title': x_feature+'vs'+y_feature,
                'Label': {'x':x_feature,
                          'y':y_feature},
                'values': {'x': x_feature_data,
                           'y': y_feature_data},
                'Legends':{0: x_feature,
                           1: y_feature}
            }
    return df_data


def groupby_frame_generator(df,feature=None,x_feature=None, y_feature=None):
    if feature:
        df = pd.DataFrame({'count':df.groupby(df[feature]).size()}).reset_index()
        x_value = json_builder(df,feature=feature)
        y_value = json_builder(df, feature='count')
        return x_value, y_value