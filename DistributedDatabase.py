import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from test import make_tree

UPLOAD_FOLDER = 'PycharmProjects/DistributedDatabase/static'
ALLOWED_EXTENSIONS = set(['txt','json', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#
#     return 'Hello World!'\

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(UPLOAD_FOLDER)
            print('---------')
            print()
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    return filename


@app.route('/lista')
def list():
    tree = make_tree(UPLOAD_FOLDER)
    print(tree)
    print(os.getcwd())
    return render_template('list.html', tree=make_tree(UPLOAD_FOLDER))


if __name__ == '__main__':
    app.run()
