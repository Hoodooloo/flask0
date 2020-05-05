import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/amanbday")
def aman():
    title = "IsItAmanBDay"
    now = datetime.datetime.now()
    aman_bday = now.month == 9 and now.day == 22
    return render_template("in.html", aman_bday=aman_bday, title=title)


@app.route("/dharmbday")
def dharm():
    title = "IsItDharmBDay"
    now = datetime.datetime.now()
    dharm_bday = now.month == 9 and now.day == 22
    return render_template("dh.html", dharm_bday=dharm_bday, title=title)


@app.route("/pragatibday")
def pragati():
    title = "IsItPragatiBDay"
    now = datetime.datetime.now()
    pragati_bday = now.month == 9 and now.day == 28
    return render_template("prag.html", pragati_bday=pragati_bday, title=title)


@app.route("/bhaskarbday")
def bhaskar():
    title = "IsItBhaskarBDay"
    now = datetime.datetime.now()
    bhaskar_bday = now.month == 4 and now.day == 24
    return render_template("hodolo.html", bhaskar_bday=bhaskar_bday, title=title)


if __name__ == "__main__":
    app.run(debug=True)
