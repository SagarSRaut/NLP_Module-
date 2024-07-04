






@app.route('/')
def student():
    return render_template('spamdetector.html')
@app.route('/spamfinder',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        data=dict(request.form)
        messag=tfidf.transform([data['message']])
        data['result']=classifier.predict(message)[0]
        return render_template('read.html',data=data)
if __name__=='__main__':
    app.run(debug=True)