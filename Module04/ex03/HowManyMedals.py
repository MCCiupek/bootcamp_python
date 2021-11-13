import pandas as pd

def howManyMedals(df, name):
    df_filtered = df[df['Name']==name][['Year', 'Medal']]
    df_filtered = df_filtered.replace(['Gold', 'Silver', 'Bronze'], ['G', 'S', 'B'])
    df_count = df_filtered.value_counts().rename_axis(['Year', 'Medal']).reset_index(name='Count')
    df_pivot = pd.pivot_table(df_count, index=df_count['Medal'].values, columns=df_count['Year'].values, fill_value=0)['Count']
    df_pivot = df_pivot.reindex(index=['G','S','B'])
    return df_pivot.to_dict()

if __name__=='__main__':
    
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    from HowManyMedals import howManyMedals
    print(howManyMedals(data, 'Kjetil Andr Aamodt'))