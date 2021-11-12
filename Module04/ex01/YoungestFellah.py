def youngestfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
    Returns:
        dct: dictionary with 2 keys for female and male athlete.
    """
    df_y = df[df['Year'] == year][['Sex', 'Age']]
    df_yf = df_y[df_y['Sex'] == 'F']
    df_ym = df_y[df_y['Sex'] == 'M']
    return {'f': df_yf.min()['Age'], 'm': df_ym.min()['Age']}

if __name__=='__main__':

    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../data/athlete_events.csv")
    loader.display(data, 12)

    from YoungestFellah import youngestfellah
    print(youngestfellah(data, 2004))
    print(youngestfellah(data, 1991))