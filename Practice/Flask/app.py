from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def welcome():
    if request.method=="POST":
        return redirect(url_for('finalmarks'))
    return render_template('home.html')
    
@app.route("/index")
def home():
    return "index"

@app.route("/about_me")
def about():
    return "issa me mario"


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/success/<int:score>')
def result(score):
    res=""
    if score >=70:
        res="PASS"
    else :
        res = "FAILED"

    exp = {"score":score, "res":res}
    return render_template('result.html',result=res)


@app.route('/finalsub',methods = ["POST","GET"])
def finalmarks():
    total_marks = 0
    if request.method=="POST":
        math = int(request.form['math'])
        sci = int(request.form['sci'])
        java = int(request.form['java'])

        total_marks = int((math+sci+java)/3)   
    else:
        return render_template('getres.html')
    return redirect(url_for('result', score = total_marks))

    

if __name__=="__main__":
    app.run()