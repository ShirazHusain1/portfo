
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
#print (__name__)

@app.route("/")
def hello_world():
    #return "<p>Hello, Shira!</p>"
    return render_template('./index.html')

# @app.route("/thankyou.html/<username>")
# def hello_world2(username='husain'):
#     return render_template('./thankyou.html', name=username)

@app.route("/<string:page_name>")
def html_page(page_name):
    #return "<p>Hello, Shira!</p>"
    return render_template(page_name)

def write_to_file(data):
    with open ('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
        #file = database.write("you are right there")
        print("write to file is working")

def write_to_csv(data):
    with open ('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        print("write to CSV is working")
        
# # @app.route("/<username>")
# # def hello_world(username=None):
# #     return render_template('index.html', name=username)

# # @app.route("/<username>/<int:post_id>")
# # def hello_world(username=None, post_id=None):
# #     return render_template('index.html', name=username, post_id=post_id)

# @app.route("/about.html")
# def about():
#     #return "<p>Hello, Shira!</p>"
#     return render_template('./about.html')

# @app.route("/contact.html")
# def contact():
#     #return "<p>Hello, Shira!</p>"
#     return render_template('./contact.html')

# @app.route("/works.html")
# def works():
#     #return "<p>Hello, Shira!</p>"
#     return render_template('./works.html')

# @app.route("/work.html")
# def work():
#     #return "<p>Hello, Shira!</p>"
#     return render_template('./work.html')

# @app.route("/components.html")
# def components():
#     #return "<p>Hello, Shira!</p>"
#     return render_template('./components.html')



# @app.route("/Home")
# def Home():
#     return "<p>Hello, Shiraz, You are at Home now</p>"

# @app.route("/Aboutme")
# def Aboutme():
#     return "<p>Hello, Shiraz, This is about you</p>"

# Get means send and Post means save

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:    
            #data = request.form['email']
            name = request.form['subject']
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            write_to_file(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong. Try again'

    #return render_template('login.html', error=error)
    #return "form submitted Hoooray"