import utils as helper
import schemer as plotter


class GraphAdviser:
    # TODO: Check for connecting loading pandas df directly from here
    def __init__(self, continous_data, categorical_data, dataframe):
        self.continous_data = continous_data
        self.categorical_data = categorical_data
        self.df = dataframe

    def output_architect(self):
        '''
        Architect the dict from the Univariate and Bultivariate Analysis
        :return: Dict of Univariate and Multivariate
        '''
        charts = {}
        univariate_charts = self.univariate_analysis()
        bivariate_charts = self.bivariate_analysis
        charts['Univariate Charts'] = univariate_charts
        charts['Bivariate Charts'] = bivariate_charts
        return charts

    def univariate_analysis(self):
        '''
        Based on the type of data, Which type of chart is going to be suggested.
        :return: Dict with chart Names.
        '''
        histogram = []
        piechart = []
        barchart = []
        # scatter_plot = []
        box_plot = []
        line_plot = []

        univariate_charts = {}

        for feature in self.categorical_data:
            piechart.append(helper.data_organiser(feature=feature, df=self.df, aggregate='count'))
            plotter.univariate_piechart_maker(self.df, feature)
            barchart.append(helper.data_organiser(feature=feature, df=self.df, aggregate='count'))
            plotter.univariate_barchart_maker(self.df, feature)
            # scatter_plot.append(helper.data_organiser(feature=feature, df=self.df, aggregate='count'))

        for feature in self.continous_data:
            histogram.append(helper.data_organiser(feature=feature, df=self.df, aggregate='Feature Values'))
            plotter.univariate_histogram_maker(self.df, feature)
            # scatter_plot.append(helper.data_organiser(feature=feature, df=self.df, aggregate='Feature values'))
            box_plot.append(helper.data_organiser(feature=feature, df=self.df, aggregate='Feature values'))
            plotter.univariate_boxplot_maker(self.df, feature)
            line_plot.append(helper.data_organiser(feature=feature, df=self.df, aggregate='Feature Values'))
            plotter.univariate_line_plot_maker(df=self.df, column=feature)

        univariate_charts['Piechart'] = {'Feature': piechart}
        'Need to reconsider the Histogrqam'
        univariate_charts['Histogram'] = {'Feature': histogram}
        univariate_charts['Barchart'] = {'Feature': barchart}
        univariate_charts['Box Plot'] = {'Feature': box_plot}
        # univariate_charts['Scatter plot'] = {'Feature': scatter_plot}
        univariate_charts['Line Plot'] = {'Feature':line_plot}

        return univariate_charts


    @property
    def bivariate_analysis(self):
        '''
        Based on the type of Data charts are recommended
        :return: Dict with Chart Names
        '''
        scatter_plot = []
        barchart =[]
        histogram = []
        dot_plot = []
        line_chart = []

        bivariate_charts = {}

        for x_feature in self.categorical_data:
            for y_feature in self.continous_data:
                if x_feature != y_feature:
                    scatter_plot.append(helper.data_organiser(df=self.df, aggregate='X Feature Values', x_feature=x_feature,
                                                              y_feature=y_feature))
                    plotter.bivariate_scatterplot_maker(df=self.df, x=x_feature, y=y_feature)
                    barchart.append(helper.data_organiser(df=self.df, aggregate='X Feature Values', x_feature=x_feature,
                                                          y_feature=y_feature))
                    line_chart.append(helper.data_organiser(df=self.df, aggregate='X Feature Values', x_feature=x_feature,
                                                        y_feature=y_feature))
        # for x_feature in self.continous_data:
        #     for y_feature in self.categorical_data:
        #         dot_plot.append(helper.data_organiser(df=self.df, aggregate='Feature Values', x_feature=x_feature,
        #                                               y_feature=y_feature))

        for x_feature in self.continous_data:
            for y_feature in self.continous_data:
                if x_feature != y_feature:
                    histogram.append(helper.data_organiser(df=self.df, aggregate='Feature Values', x_feature=x_feature,
                                                           y_feature=y_feature))
                    plotter.bivariate_histogram_maker(df=self.df, x=x_feature, y=y_feature)
                    scatter_plot.append(helper.data_organiser(df=self.df, aggregate='Feature Values', x_feature=x_feature,
                                                              y_feature=y_feature))
                    plotter.bivariate_scatterplot_maker(df=self.df, x=x_feature, y=y_feature)
                    line_chart.append(helper.data_organiser(df=self.df, aggregate='Feature Values', x_feature=x_feature,
                                                            y_feature=y_feature))
                    plotter.bivariate_line_plot_maker(df=self.df, x=x_feature, y=y_feature)

        bivariate_charts['Scatter_Plot'] ={'Feature': scatter_plot}
        bivariate_charts['Histogram'] = {'Feature': histogram}
        #TODO: Think both dot plot and scatter are giving the same kind of graphs
        # bivariate_charts['Dot Plot'] = {'Feature': dot_plot}
        bivariate_charts['Line Chart'] = {'Feature': line_chart}
        bivariate_charts['Bar Chart'] = {'Feature': barchart}

        return bivariate_charts
