from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

import invoiceclass
from forms import CreateUserForm, CreateStaffForm, LogInForm
from invoiceForm import CreateInvoiceForm
from itemForm import CreateItemForm, serialcheck
import shelve, User, itemclass, itemForm, staffClass, os, uuid

UPLOAD_FOLDER='templates/includes/productimages'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def retrieveFiles():
    entries = os.listdir(app.config['UPLOAD_FOLDER'])
    fileList = []
    for entry in entries:
        fileList.append(entry)
    return fileList

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')


@app.route('/staffHome')
def staffHome():
    return render_template('staffHome.html')


@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/viewinvoices')
def viewInvoices():
    return redirect(url_for('inventory'))

@app.route('/createInvoice',methods=['GET','POST'])
def createInvoice():
    createInvoiceForm = CreateInvoiceForm(request.form)

    if request.method == 'POST' and createInvoiceForm.validate():
        invoiceDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            invoiceDict = db['Invoice']
            invoiceclass.Invoice.countID = db['Invoicecount']
        except:
            print("Error in retrieving Invoice from storage.db.")
        invoice = invoiceclass.Invoice(createInvoiceForm.invoiceNumber.data,createInvoiceForm.invoiceDate.data,createInvoiceForm.shipmentDate.data,createInvoiceForm.shipmentStatus.data,createInvoiceForm.receivedDate.data)
        invoiceDict[invoice.get_invoiceCount()] = invoice
        db['Invoice'] = invoiceDict
        db['invoicecount']=invoiceclass.Invoice.countID
        print(db['Invoice'])
        db.close()

        return redirect(url_for('inventory'))
    return render_template('createInvoice.html', form=createInvoiceForm)

@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    createUserForm = CreateUserForm(request.form)

    if request.method == 'POST' and createUserForm.validate():
        usersDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            usersDict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")
            user = User.User(createUserForm.firstName.data, createUserForm.lastName.data,
                             createUserForm.membership.data, createUserForm.gender.data, createUserForm.remarks.data)
            usersDict[user.get_userID()] = user
            db['Users'] = usersDict
            db.close()
            return redirect(url_for('retrieveUsers'))
        return redirect(url_for('home'))
    return render_template('createUser.html', form=createUserForm)

@app.route('/deleteItem/<int:id>/',methods=['GET','POST'])
def deleteItem(id):

    itemDict = {}
    db  = shelve.open("storage.db","w")
    itemDict =db["Items"]

    itemDict.pop(id) #action of removing the record
    db["Items"] = itemDict #put back to persistence
    db.close()

    #after we delete succesfully
    return redirect(url_for('itempage'))

@app.route('/updateItem/<int:id>/',methods=['GET','POST'])
def updateItem(id):
    updateItemForm = CreateItemForm(request.form)
    if request.method == 'POST' and updateItemForm.validate():
        itemDict = {}
        db = shelve.open('storage.db', 'w')
        itemDict = db['Items']

        item = itemDict.get(id)
        item.set_itemName(updateItemForm.itemName.data)
        item.set_itemSerial(updateItemForm.itemSerial.data)
        item.set_itemCategory(updateItemForm.itemCategory.data)
        item.set_itemGender(updateItemForm.itemGender.data)
        item.set_itemCost(updateItemForm.itemCost.data)
        item.set_itemPrice(updateItemForm.itemPrice.data)

        db['Items'] = itemDict
        db.close()
        return redirect(url_for('itempage'))
    else:
        itemDict = {}
        db = shelve.open('storage.db', 'r')
        itemDict = db['Items']
        db.close()

        item = itemDict.get(id)
        updateItemForm.itemName.data = item.get_itemName()
        updateItemForm.itemSerial.data = item.get_itemSerial()
        updateItemForm.itemCategory.data = item.get_itemCategory()
        updateItemForm.itemGender.data = item.get_itemGender()
        updateItemForm.itemCost.data = item.get_itemCost()
        updateItemForm.itemPrice.data = item.get_itemPrice()
        return render_template('updateItem.html',form=updateItemForm)

@app.route('/itempage')
def itempage():
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    for key in itemDict:
        item = itemDict.get(key)
        itemList.append(item)
    return render_template('itempage.html', itemList=itemList, count=len(itemList))

@app.route('/cart')
def cart():
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    for key in itemDict:
        item = itemDict.get(key)
        itemList.append(item)
    return render_template('cart.html', itemList=itemList, count=len(itemList))

@app.route('/viewItem')
def viewItem():
    return render_template('itempage.html')


@app.route('/itemCreation', methods=['GET', 'POST'])
def itemCreation():
    createItemForm = CreateItemForm(request.form)

    if request.method == 'POST' and createItemForm.validate():
        itemsDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            itemsDict = db['Items']
            itemclass.Item.countID = db['itemcount']
        except:
            print("Error in retrieving Items from storage.db.")
        item = itemclass.Item(createItemForm.itemSerial.data,createItemForm.itemName.data,createItemForm.itemCategory.data, createItemForm.itemGender.data, createItemForm.itemCost.data,createItemForm.itemPrice.data)
        itemsDict[item.get_itemSerial()] = item
        db['Items'] = itemsDict
        db['itemcount']=itemclass.Item.countID
        print(db['Items'])
        db.close()

        def upload_file():
            if request.method == 'POST':
                # check if the post request has the file part
                if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['file']
                # if user does not select file, browser also
                # submit an empty part without filename
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)

                    # added uuid to make the filename unique. Otherwise, file with same names will override.
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid4()) + filename))

                    return render_template('itemCreation.html', fileList=retrieveFiles())
            return render_template('home.html', fileList=retrieveFiles())
        return redirect(url_for('itempage'))
    return render_template('itemCreation.html', form=createItemForm)



@app.route('/createStaff', methods=['GET', 'POST'])
def createStaff():
    createStaffForm = CreateStaffForm(request.form)

    if request.method == 'POST' and createStaffForm.validate():
        staffDict = {}
        db = shelve.open('storage.db', 'w')
        try:
            staffDict = db['Staff']
        except:
            print("Error in retrieving Staff from storage.db.")
        staff = staffClass.Staff(createStaffForm.fname.data,createStaffForm.lname.data, createStaffForm.gender.data,createStaffForm.hp.data, createStaffForm.dob.data, createStaffForm.password.data, createStaffForm.address.data)

        staffDict[staff.get_email()] = staff
        db['Staff'] = staffDict
        db.close()
        return redirect(url_for('staffAccount'))
    return render_template('createStaff.html', form=createStaffForm)

@app.route('/staffAccount')
def staffAccount():
    render_template('staffAccount.html')

# @app.route('/tempLogin', method=['GET', 'POST'])
# def login():
#     loginForm = LogInForm(request.form)
#
#     if request.method == 'POST' and loginForm.validate():



@app.route('/createNewReport')
def createNewReport():
    return render_template('create.html')

@app.route('/salesReports')
def salesReports():
    return render_template('salesReports.html')



if __name__ == '__main__':
    app.run()
