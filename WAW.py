from flask import Flask, request, redirect, url_for, render_template
import common
app = Flask(__name__)

my_addres = '127.0.0.1:5000'
my_name = 'Warszawa'

baza = {
    1:(u"Zakup słoików",-123,"Finanse"),
    2:(u"Zakup kolumn",-896,"Finanse"),
    3:(u"Zakup starbucksow",-6734,"Finanse"),
    4:(u"Sprzedaż epapierosow",1645,"Finanse"),
    5:(u"Sprzedaż fidget-spinnerow",3213,"Finanse")
    }

@app.route('/local')
def local_database():
    print(baza)
    return str(baza)

@app.route('/global')
def global_database():
    global_dict = {}
    global_dict.update(baza)
    global_dict.update(common.get_global_database(my_addres))
    print(global_dict)
    return str(global_dict)


@app.route('/')
@app.route('/localdatabase')
def local_database_table():
    '''
        shows beautifull table
    '''
    print(baza)
    return render_template('local.html',database = baza, nodename =my_name)

@app.route('/globaldatabase')
def global_database_table():
    '''
    shows beautifull table
    '''
    global_dict = {}
    global_dict.update(baza)
    global_dict.update(common.get_global_database(my_addres))
    print(global_dict)
    return render_template('global.html',database = global_dict, nodename = "All cities")

@app.route('/lastindex')
def last_index():
    return str(max(baza.keys()))

@app.route('/add_data', methods=['POST','GET'])
def add_data():
    print("jestem w adddata")
    if request.method == 'POST':
        print("jestem w poscie")
        # find highest key in whole database
        highest = max(common.get_highest_index_globaly(my_addres), max(baza.keys()))
        # baza[highest + 1] = (u"Sprzedaż ości", 3, "RachunkowOsc")

        id = highest + 1
        opis = request.form["Opis"]
        kwota = int(request.form["Kwota"])
        dzial = request.form["Dzial"]
        baza[id] = (opis,kwota,dzial)
        print('dodalem')
        return redirect(url_for('local_database_table'))
    elif request.method == 'GET':
        print("jestem w gecie")
        return render_template('add_data.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)