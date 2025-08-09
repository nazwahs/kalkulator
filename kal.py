from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def kalkulator():
    ekspresi = request.form.get("ekspresi", "")
    tombol = request.form.get("angka")
    hasil = ""

    if tombol == "C":
        ekspresi = ""
    elif tombol == "DEL":
        ekspresi = ekspresi[:-1]
    elif tombol == "=":
        try:
            hasil = str(eval(ekspresi))
        except:
            hasil = "ERROR"
    elif tombol:
        ekspresi += tombol

    return render_template("index.html", ekspresi=ekspresi, hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
