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

        charts = [{'data': self.univariate_analysis(),
                  'analysis_name': 'Univariant Analysis',
                  'analysis_type': 'Univariant analysis',
                  },
                 {'data': self.bivariate_analysis(),
                  'analysis_name': 'Bivariate Analysis',
                  'analysis_type': 'Bivariate analysis',
                  }]

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

        for feature in self.categorical_data:
            piechart.append(helper.data_organiser(feature=feature, df=self.df, chart='piechart'))
            plotter.univariate_piechart_maker(self.df, feature)
            barchart.append(helper.data_organiser(feature=feature, df=self.df, chart='barchart'))
            plotter.univariate_barchart_maker(self.df, feature)
            # scatter_plot.append(helper.data_organiser(feature=feature, df=self.df, aggregate='count'))

        for feature in self.continous_data:
            histogram.append(helper.data_organiser(feature=feature, df=self.df, chart='Hstogram'))
            plotter.univariate_histogram_maker(self.df, feature)
            # scatter_plot.append(helper.data_organiser(feature=feature, df=self.df, aggregate='Feature values'))
            # TODO: Check with frontend for boxplot whether they need quartile values or data .
            box_plot.append(helper.data_organiser(feature=feature, df=self.df, chart='BoxPlot'))
            plotter.univariate_boxplot_maker(self.df, feature)

            #TODO: Need to add a logic for Date column. Damo bro said we can ask that from User end.

            # line_plot.append(helper.data_organiser(feature=feature, df=self.df, chart='LinePlot'))
            # plotter.univariate_line_plot_maker(df=self.df, column=feature)

        univariate_charts = []

        univariate_charts.append({'chart_type':'piechart',
                                  'chart_data': piechart})
        # 'Need to reconsider the Histogrqam'
        univariate_charts.append({'chart_type': 'Barchart',
                                  'chart_data': barchart})
        univariate_charts.append({'chart_type': 'Boxplot',
                                  'chart_data': box_plot})
        univariate_charts.append({'chart_type': 'Histogram',
                                  'chart_data': histogram})
        # univariate_charts.append({'chart_type': 'Lineplot',
        #                           'chart_data': line_plot})

        return univariate_charts


    # @property
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

        for x_feature in self.categorical_data:
            for y_feature in self.continous_data:
                if x_feature != y_feature:
                    scatter_plot.append(helper.data_organiser(df=self.df, chart='Ordinalscatterplot', x_feature=x_feature,
                                                              y_feature=y_feature))
                    plotter.bivariate_scatterplot_maker(df=self.df, x=x_feature, y=y_feature)
                    barchart.append(helper.data_organiser(df=self.df, chart='Barchart', x_feature=x_feature,
                                                          y_feature=y_feature))
                    line_chart.append(helper.data_organiser(df=self.df, chart='linechart', x_feature=x_feature,
                                                            y_feature=y_feature))
        # for x_feature in self.continous_data:
        #     for y_feature in self.categorical_data:
        #         dot_plot.append(helper.data_organiser(df=self.df, aggregate='Feature Values', x_feature=x_feature,
        #                                               y_feature=y_feature))

        for x_feature in self.continous_data:
            for y_feature in self.continous_data:
                if x_feature != y_feature:
                    histogram.append(helper.data_organiser(df=self.df, chart='Histogram', x_feature=x_feature,
                                                           y_feature=y_feature))
                    plotter.bivariate_histogram_maker(df=self.df, x=x_feature, y=y_feature)
                    scatter_plot.append(helper.data_organiser(df=self.df, chart='scatterplot', x_feature=x_feature,
                                                              y_feature=y_feature))
                    plotter.bivariate_scatterplot_maker(df=self.df, x=x_feature, y=y_feature)
                    line_chart.append(helper.data_organiser(df=self.df, chart='linechart', x_feature=x_feature,
                                                            y_feature=y_feature))
                    plotter.bivariate_line_plot_maker(df=self.df, x=x_feature, y=y_feature)

        bivariate_charts = []
        bivariate_charts.append({'chart_type':'scatter plot',
                                 'chart_data': scatter_plot})
        bivariate_charts.append({'chart_type': 'Histogram',
                                 'chart_data': histogram})
        bivariate_charts.append({'chart_type': 'Line Chart',
                                 'chart_data': line_chart})
        bivariate_charts.append({'chart_type': 'Bar chart',
                                 'chart_data': barchart})


        #TODO: Think both dot plot and scatter are giving the same kind of graphs

        return bivariate_charts
