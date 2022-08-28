import csv
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:page_name>")
def pages(page_name):
    return render_template(page_name)

def write_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open("Database.csv" , mode="a",newline="") as database:
        csv_writer = csv.writer(database)
        csv_writer.writerow([email,subject,message])

@app.route("/submit_form" , methods=["POST" , "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("Thankyou.html")
        except:
            return "Data didn't save"
    else:
        return "something went wrong"