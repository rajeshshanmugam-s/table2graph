from lumper import DataLumper
from adviser import GraphAdviser
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def main():
    x = DataLumper('train.csv')
    df = x.data_frame_loader()
    df = df[:11]
    cat_data, cont_data = x.data_type_explorer()
    print(cat_data)
    print(cont_data)
    y = GraphAdviser(dataframe=df, continous_data=cont_data, categorical_data=cat_data)
    charts = y.output_architect()

    return charts


if __name__ == '__main__':
    app.run(debug=True)
