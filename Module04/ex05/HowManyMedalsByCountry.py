import pandas as pd
import sys


def howManyMedalsByCountry(df, country):
    """
    returns a dictionary of dictionaries
    giving the number and type of medal for each competition where the country delegation
    earned medals.
    """
    try:
        if not any(df['Team'].str.contains(country)):
            print("Error: Country not found: {0}".format(country))
            return None
        df_filtered = df[df['Team'].str.contains(country)][['Team', 'Year', 'Medal', 'Event']]
        df_filtered = df_filtered.replace(['Gold', 'Silver', 'Bronze'], ['G', 'S', 'B'])
        df_filtered =  df_filtered.drop_duplicates(subset=['Event', 'Medal'])
        df_filtered = df_filtered[df_filtered['Medal'].notna()][['Year', 'Medal']]
        df_count = df_filtered.value_counts().rename_axis(['Year', 'Medal']).reset_index(name='Count')
        df_pivot = pd.pivot_table(df_count, index=df_count['Medal'].values, columns=df_count['Year'].values, fill_value=0)['Count']
        df_pivot = df_pivot.reindex(index=['G','S','B'])
        return df_pivot.to_dict()
    except Exception as err:
        sys.stderr.write("Error: {0}: {1}".format(type(err).__name__, err))


if __name__=="__main__":

    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    # loader.display(data, 12)

    print(howManyMedalsByCountry(data, 'Italy'))
