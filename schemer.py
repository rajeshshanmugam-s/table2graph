### Note: This file is not part of the project


import matplotlib.pyplot as plt
import seaborn as sns


def univariate_piechart_maker(df, column):
    fig = plt.clf()
    g_1 = df[column].groupby(df[column]).count()
    plt.pie(g_1, labels=g_1.index)
    plt.savefig('charts/'+column + '_Univariate_piechat.png')


def univariate_histogram_maker(df, column):
    fig = plt.clf()
    sns_plot = sns.distplot(df[column], kde=False)
    fig = sns_plot.get_figure()
    fig.savefig('charts/'+column + '_Univariate_histogram.png')


def univariate_barchart_maker(df, column):
    fig = plt.clf()
    g_1 = df[column].groupby(df[column]).count()
    sns_plot = sns.barplot(x=g_1.index, y=g_1)
    fig = sns_plot.get_figure()
    fig.savefig('charts/'+column + '_Univariate_barchart.png')


def univariate_boxplot_maker(df, column):
    fig = plt.clf()
    sns_plot = sns.boxplot(df[column])
    fig = sns_plot.get_figure()
    fig.savefig('charts/'+column + '_Univariate_boxplot.png')


def univariate_line_plot_maker(df, column):
    sns_plot = sns.lineplot(data= df[column])
    fig = sns_plot.get_figure()
    fig.savefig('charts/' + column + '_Univariate_lineplot.png')


def bivariate_scatterplot_maker(df, x, y):
    fig = plt.clf()
    sns_plot = sns.scatterplot(df[x],df[y])
    fig = sns_plot.get_figure()
    fig.savefig('charts/' + x + '_' +y +'_Bivariate_scatterplot.png')


def bivariate_histogram_maker(df, x, y):
    fig = plt.clf()
    plt.hist([df[x], df[y]])
    plt.legend([x, y])
    plt.savefig('charts/' + x + '_' +y +'_Bivariate_histogram.png')


def bivariate_line_plot_maker(df, x, y):
    sns_plot = sns.lineplot(x=df[x], y=df[y])
    fig = sns_plot.get_figure()
    fig.savefig('charts/' + x + '_' + y + '_Biivariate_lineplot.png')


