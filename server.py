from flask import Flask,render_template, request,redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/components')
def components():
    return render_template('components.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/<string:username>')
def hello_world1(username=None):
    return render_template('username.html',name=username)

@app.route('/<string:username>/<int:post_id>')
def user_id(username=None,post_id=None):
    return render_template('id.html',name=username,user_id=post_id)

@app.route('/whoareyou')
def about1():
    return render_template('about1.html')

@app.route('/liketospeak')
def contact1():
    return render_template('contact1.html')

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file = database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong.Try again'