import pandas as pd 

def proportionBySport(df, year, sport, gender):
    df_filtered = df[df['Sport']==sport]
    df_filtered = df_filtered[df_filtered['Year']==year][['Sex', 'Year', 'Sport']]
    return df_filtered[df_filtered['Sex']==gender].shape[0] / df_filtered.shape[0]

if __name__=='__main__':
    
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    from ProportionBySport import proportionBySport

    print(proportionBySport(data, 2004, 'Tennis', 'F'))
    print(proportionBySport(data, 2016, 'Basketball', 'F'))