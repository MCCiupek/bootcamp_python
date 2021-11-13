import pandas as pd
import scipy
import seaborn
import matplotlib.pyplot as plt


class MyPlotLib():
    """
    This class implements different plotting methods
    """

    @staticmethod
    def histogram(data, features):
        """
        plots one histogram for each numerical feature in
        the list
        """
        df_filtered = data[features]
        df_filtered.hist()

    @staticmethod
    def density(data, features):
        """
        plotss the density curve for each numerical feature in
        the list
        """
        df_filtered = data[features]
        df_filtered.plot.kde()

    @staticmethod
    def pair_plot(data, features):
        """
        plots a matrix of subplots (also called scatter plot
        matrix). On each subplot shows a scatter plot of one numerical variable against
        another one. The main diagonal of this matrix shows simple histograms.
        """
        df_filtered = data[features]
        seaborn.pairplot(df_filtered)
    
    @staticmethod
    def box_plot(data, features):
        """
        displays a box plot for each numerical variable in the
        dataset.
        """
        df_filtered = data[features]
        df_filtered.boxplot()
