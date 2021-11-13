import pandas as pd
from MyPlotLib import MyPlotLib

class Komparator():
    def __init__(self, data):
        self.data = data

    def filter_df(self, categorical_var, numerical_var):
        df_filtered = self.data[[categorical_var, numerical_var]]
        categories = df_filtered[categorical_var].drop_duplicates().values
        df = df_filtered[df_filtered[categorical_var]==categories[0]][numerical_var]
        for category in categories[1:]:
            df = pd.concat([df, df_filtered[df_filtered[categorical_var]==category][numerical_var]], axis=1)
        df.columns = categories
        return df

    def compare_box_plots(self, categorical_var, numerical_var):
        """
        displays a box plot with
        several boxes to compare how the distribution of the numerical variable changes if
        we only consider the subpopulation which belongs to each category.
        """
        df = self.filter_df(categorical_var, numerical_var)
        mlp = MyPlotLib()
        print(df)
        mlp.box_plot(df, df.columns)

    def density(self, categorical_var, numerical_var):
        """
        displays the density of the numerical variable.
        """
        df = self.filter_df(categorical_var, numerical_var)
        mlp = MyPlotLib()
        mlp.density(df, df.columns)
    
    def compare_histograms(self, categorical_var, numerical_var):
        """
        plots the numerical
        variable in a separate histogram for each category
        """
        df = self.filter_df(categorical_var, numerical_var)
        mlp = MyPlotLib()
        mlp.histogram(df, df.columns)


if __name__=="__main__":

    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    kmp = Komparator(data)
    categorical_var = 'Sex'
    numerical_var = 'Height'

    kmp.compare_box_plots(categorical_var, numerical_var)