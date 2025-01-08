from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return ''

@app.route('/Strong/<int:score>')
def  Strong(score):
    return 'your BMI is good and your weight is perfect for your height maintain your fittness like this only and your BMI score is'+str(score)


@app.route('/Weak/<int:score>')
def  Weak(score):
    return 'your BMI is not less so please work on your body and be fit and your BMI score is'+str(score)\
    
@app.route('/BMI/<int:marks>')
def  BMI(marks):
    results=''
    if marks>=85:
        results='Strong'

    else:
        results='Weak'

    return redirect(url_for(results,score=marks))


if __name__=='__main__':
    app.run(debug=True)