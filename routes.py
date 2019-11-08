from lumper import DataLumper
from adviser import GraphAdviser
from flask import Flask, request, render_template, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def main_route():
    return'Hello World';


@app.route("/test")
def basic_template():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


@app.route('/upload', methods=['POST'])
def data_gunner():
    if not os.path.exists('Data'):
        os.mkdir('Data')
    f = request.files['file']
    f.save('Data/'+f.filename)
    x = DataLumper('Data/'+f.filename)
    df = x.data_frame_loader()
    # TODO: Remove this
    # df = df[:11]
    cat_data, cont_data = x.data_type_explorer()
    print(cat_data)
    print(cont_data)
    from click import pause
    pause()
    y = GraphAdviser(dataframe=df, continous_data=cont_data, categorical_data=cat_data)
    charts = y.output_architect()

    return jsonify(charts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=1024)
