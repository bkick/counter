from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='secret'
@app.route('/')
def index():
	if 'counter' in session.keys():
		session['counter']+=1
		print('has session attribute')
	else:
		session['counter']=0
		print('NO session attribute')
		
	print(session['counter'])
	return render_template("index.html")

	
@app.route('/reset', methods=['POST'])
def reset():
    session['counter']=0
    return redirect('/')
@app.route('/2', methods=['POST'])
def add():
    session['counter']+=1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)