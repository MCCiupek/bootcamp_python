import pandas as pd
import sys

class SpatioTemporalData():
    def __init__(self, df):
        try:
            self.df = df[['Year', 'City']].drop_duplicates()
        except Exception as err:
            sys.stderr.write("Error: {0}: {1}".format(type(err).__name__, err))
            sys.exit()
    
    def when(self, location):
        """
        takes a location as an argument and returns a list containing the
        years where games were held in the given location
        """
        return self.df[self.df['City']==location]['Year'].values

    def where(self, date):
        """
         takes a date as an argument and returns the location where the
        Olympics took place in the given year
        """
        return self.df[self.df['Year']==date]['City'].values


if __name__=="__main__":

    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    sp = SpatioTemporalData(data)
    print(sp.where(1896))

    print(sp.where(2016))

    print(sp.when('Athina'))

    print(sp.when('Paris'))