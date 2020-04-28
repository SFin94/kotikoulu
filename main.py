# Entry and exit point for the app
from flask import Flask, render_template, request, redirect, url_for

# Create app instance
app = Flask(__name__)

# start form (specifies location and place)
@app.route('/')
def home():
    return render_template('index.html')


# Form page for knowledge calls
@app.route('/knowcall', methods=['POST', 'GET'])
def know_call_form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        ageRange = request.form['agerange']
        subjects = request.form['subjects']
        return redirect(url_for('showcall',
                                name=name,
                                email=email,
                                ageRange=ageRange,
                                subjects=subjects))
    return render_template('form_call.html')


# View submitted form info
@app.route('/showcall', methods=['GET'])
def show_call():
    name = request.args.get('name')
    email = request.args.get('email')
    ageRange = request.args.get('ageRange')
    subjects = request.args.get('subjects')
    return render_template('show_call.html',
                            name=name,
                            email=email,
                            ageRange=ageRange,
                            subjects=subjects)

# # Form page for knowledge provider
# @app.route('/knowledgeResponse')
# def knowResponseForm():
#      return render_template('knowResponse_form.html')


if __name__ == "__main__":
    app.run(debug=True)

# KAUBE form tutorials
# @app.route('/form')
# def form():
#     return render_template('form.html')

# # [START submitted]
# @app.route('/submitted', methods=['POST'])
# def submitted_form():
#     name = request.form['name']
#     email = request.form['email']
#     site = request.form['site_url']
#     comments = request.form['comments']

#     # [END submitted]
#     # [START render_template]
#     return render_template(
#         'submitted_form.html',
#         name=name,
#         email=email,
#         site=site,
#         comments=comments)
#     # [END render_template]
