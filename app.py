from flask import Flask, render_template, request
import model


app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/bball"> Men's Basketball </a></li>
        </ul>
    '''

# @app.route('/bball')
# def bball():
#     return render_template("seasons.html", seasons=model.get_bball_seasons())

#Update bball
@app.route('/bball', methods=['GET', 'POST'])
def bball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_bball_seasons(sortby, sortorder)
    else:
        seasons = model.get_bball_seasons()

    return render_template("seasons.html", seasons=seasons)

@app.route('/football', methods=['GET', 'POST'])
def fball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_fball_seasons(sortby, sortorder)
    else:
        seasons = model.get_fball_seasons()

    return render_template("seasons.html", seasons=seasons)

# @app.route('/hello', methods=['GET', 'POST']) #allows us to handle the route if someone puts it directily into the prowser or as a post

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
    else:
        firstname = ''
        lastname = ''

    return render_template("hello.html", firstname=firstname, lastname=lastname)

if __name__ == '__main__':
    model.init_bball()
    model.init_fball()
    #print(model.get_bball_seasons())
    app.run(debug=True)


#app.py will stay ignorant of the data storage part found in Model.py
