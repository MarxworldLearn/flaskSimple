from flask import Flask, Response, send_from_directory, send_file, request
import csv
import codecs
import pandas as pd


app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def index():
    return send_file("static/index.html")


@app.route("/static/<path:path>")
def send_report(path):
    return send_from_directory("static", path)


@app.route("/uploadCSVOld", methods=["POST"])
def upload_file():
    # Get the uploaded file from the request
    uploaded_file = request.files["file"]
    print(uploaded_file.name)
    stream = codecs.iterdecode(uploaded_file.stream, "utf-8")

    reader = csv.reader(stream, delimiter=",")
    for row in csv.reader(stream, dialect=csv.excel):
        if row:
            print(row)
            # Do something with the row here
    return "File read successfully"


@app.route("/uploadCSV", methods=["POST"])
def upload_filePanda():
    # Get the uploaded file from the request
    uploaded_file = request.files["file"]
    print(uploaded_file.name)

    df = pd.read_csv(uploaded_file)
    print(df)
    json_data = df.to_json(indent=4, orient="records")  # convert to json
    print(json_data)

    return "File read successfully"


if __name__ == "__main__":  # pragma: no cover
    app.run(port=8080)
