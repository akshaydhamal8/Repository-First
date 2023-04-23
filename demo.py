


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/add",methods = ['POST','GET'])
def addition():
    if request.method == 'POST':
        formdata = request.form
        print(formdata)

        try:
            num1 = int(formdata.get('n1'))
            num2 = int(formdata.get('n2'))
        except:
            # return "addition function invoked....."
            return render_template('add.html', ans = "Invalid Input")
        else:
            result = num1 + num2
            return render_template('add.html' , ans=result)
    return render_template('add.html')
if __name__ == '__main__':
     app.run(debug=True)





