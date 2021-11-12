import pandas as pd

class FileLoader(object):
    
    @staticmethod
    def load(path):
        df = pd.read_csv(path)
        print("Loading dataset of dimensions {0} x {1}".format(*df.shape))
        return df

    @staticmethod
    def display(df, n):
        print(df[:n])


if __name__=='__main__':

    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../data/athlete_events.csv")
    loader.display(data, 12)