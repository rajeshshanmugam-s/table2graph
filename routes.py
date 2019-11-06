from lumper import DataLumper
from adviser import GraphAdviser
from flask import Flask, request, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def main_route():
    return'Hello World';

@app.route("/test")
def basic_template():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route('/uploader')
def sample():
    if not os.path.exists('Data'):
        os.mkdir('Data')
    f = request.files['file']
    f.save('Data/'+f.filename)
    return 'File Saved'

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

    return json.dumps(charts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=1024)
