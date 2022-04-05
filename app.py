from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/greeting/<user>')
def greeting(user):
    return render_template('greeting.html',name=user)

if __name__  =='__main__':  
    app.run(debug = True)