from lumper import DataLumper
from adviser import GraphAdviser
from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/upload')
def data_gunner():
    if not os.path.exists('Data'):
        os.mkdir('Data')
    f = request.files['file']
    f.save('Data/'+f.filename)
    x = DataLumper('Data/'+f.filename)
    df = x.data_frame_loader()
    # TODO: Remove this
    df = df[:11]
    cat_data, cont_data = x.data_type_explorer()
    y = GraphAdviser(dataframe=df, continous_data=cont_data, categorical_data=cat_data)
    charts = y.output_architect()

    return charts


@app.route('/')
def test():
    return'Hello World'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6000)
