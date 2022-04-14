import csv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    ip_address = db.Column(db.TEXT)
    wrs_name = db.Column(db.TEXT)
    MAC = db.Column(db.TEXT)
    user = db.Column(db.TEXT)
    departments = db.Column(db.TEXT)
    mthb = db.Column(db.TEXT)
    cpu = db.Column(db.TEXT)
    ram = db.Column(db.TEXT)
    video = db.Column(db.TEXT)
    displays = db.Column(db.TEXT)
    hdd = db.Column(db.INTEGER)
    os_version = db.Column(db.TEXT)
    nomachine = db.Column(db.TEXT)
    additional_info = db.Column(db.TEXT)


db.create_all()


@app.route('/')
def index():
    users = User.query
    return render_template('bootstrap_table.html', title='CGF',
                           users=users)


# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['ip_address', 'wrs_name', 'MAC', 'user', 'departments', 'mthb', 'cpu', 'ram', 'video',
#                      'displays', 'hdd', 'os_version', 'nomachine', 'additional_info'])
#     writer.writerow(['ip_address','wrs_name'])
#         writer.writerow(
#             [i.ip_address, i.wrs_name, i.MAC, i.user, i.departments, i.mthb,
#              i.cpu, i.ram, i.video, i.displays, i.hdd, i.os_version, i.nomachine,
#              i.additional_info])
# with open(path, 'w') as csvfile:


if __name__ == '__main__':
    app.run()
