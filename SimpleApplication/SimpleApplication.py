from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from forms import CreateUserForm, CreateStaffForm, LogInForm, UpdateStaffForm, CreateAnnouncement
from invoiceForm import CreateInvoiceForm
from itemForm import CreateItemForm, serialcheck
import shelve, User, Item, itemForm, Staff, Invoice, os, uuid, Announcement


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')


@app.route('/staffHome')
def staffHome():
    return render_template('staffHome.html')


@app.route('/inventory')
def inventory():
    invoiceDict = {}
    db = shelve.open('storage.db', 'r')
    invoiceDict = db['Invoice']
    db.close()

    invoiceList = []
    for key in invoiceDict:
        invoice = invoiceDict.get(key)
        invoiceList.append(invoice)
    return render_template('inventory.html', invoiceList=invoiceList, count=len(invoiceList))


@app.route('/viewinvoices')
def viewInvoices():
    return render_template('inventory.html')


@app.route('/viewStock')
def viewStock():
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    for key in itemDict:
        item = itemDict.get(key)
        itemList.append(item)
    return render_template('viewStock.html', itemList=itemList, count=len(itemList))


@app.route('/createInvoice', methods=['GET', 'POST'])
def createInvoice():
    createInvoiceForm = CreateInvoiceForm(request.form)

    if request.method == 'POST' and createInvoiceForm.validate():
        invoiceDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            invoiceDict = db['Invoice']
            Invoice.Invoice.countID = db['invoicecount']
        except IOError:
            print("IOError")
        except:
            print("Error in retrieving Invoice from storage.db.")


        invoice = Invoice.Invoice(createInvoiceForm.invoiceDate.data, createInvoiceForm.shipmentDate.data,
                                       createInvoiceForm.shipmentStatus.data, createInvoiceForm.receivedDate.data, )
        invoiceDict[invoice.get_invoiceCount()] = invoice
        db['Invoice'] = invoiceDict
        db['invoicecount'] = Invoice.Invoice.countID
        print(db['Invoice'])
        db.close()

        return redirect(url_for('inventory'))
    return render_template('createInvoice.html', form=createInvoiceForm)


@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    createUserForm = CreateUserForm(request.form)

    if request.method == 'POST' and createUserForm.validate():
        print('SimpleApp Ln 115')
        usersDict = {}
        db = shelve.open('storage.db', 'w')
        try:
            print('SimpleApp Ln 119')
            usersDict = db['Users']
        except IOError:
            print("IOError")
        except:
            print("Error in retrieving Users from storage.db.")
        finally:
            user = User.User(createUserForm.firstName.data, createUserForm.lastName.data,
                             createUserForm.DOB.data, createUserForm.gender.data, createUserForm.email.data,
                             createUserForm.pw.data,createUserForm.confirmpw.data )
            usersDict[user.get_userID()] = user
            db['Users'] = usersDict
            db.close()
        # return redirect(url_for('retrieveUsers'))
        return redirect(url_for('home'))
    return render_template('createUser.html', form=createUserForm)


@app.route('/retrieveUsers')
def retrieveUsers():
    usersDict = {}
    db = shelve.open('storage.db', 'r')
    usersDict = db['Users']
    db.close()

    usersList = []
    for key in usersDict:
        user = usersDict.get(key)
        usersList.append(user)

    return render_template('retrieveUsers.html', usersList=usersList, count=len(usersList))


@app.route('/deleteItem/<id>/', methods=['GET', 'POST'])
def deleteItem(id):
    itemDict = {}
    db = shelve.open("storage.db", "w")
    itemDict = db["Items"]

    itemDict.pop(id)  # action of removing the record
    db["Items"] = itemDict  # put back to persistence
    db.close()

    # after we delete succesfully
    return redirect(url_for('itempage'))


@app.route('/updateItem/<id>/', methods=['GET', 'POST'])
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
        return render_template('updateItem.html', form=updateItemForm)


@app.route('/itempage')
def itempage():
    global db
    itemDict = {}
    try:
        db = shelve.open('storage.db', 'r')
        itemDict = db['Items']
    except:
        print("whip")
    finally:
        db.close()

    itemList = []
    for key in itemDict:
        item = itemDict.get(key)
        itemList.append(item)
    return render_template('itempage.html', itemList=itemList, count=len(itemList))


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
            Item.Item.countID = db['itemcount']
        except:
            print("Error in retrieving Items from storage.db.")
        item = Item.Item(createItemForm.itemSerial.data, createItemForm.itemName.data,
                              createItemForm.itemCategory.data, createItemForm.itemGender.data,
                              createItemForm.itemCost.data, createItemForm.itemPrice.data)
        itemsDict[item.get_itemSerial()] = item
        db['Items'] = itemsDict
        db['itemcount'] = Item.Item.countID
        db.close()

        return redirect(url_for('itempage'))
    return render_template('itemCreation.html', form=createItemForm)


@app.route('/createStaff', methods=['GET', 'POST'])
def createStaff():
    createStaffForm = CreateStaffForm(request.form)

    if request.method == 'POST' and createStaffForm.validate():
        staffDict = {}
        try:
            db = shelve.open('storage.db', 'c')
            Staff.Staff.count = db['staffCount']
            staffDict = db['Staff']
        except:
            print("Error in retrieving Staff from storage.db.")
        staff = Staff.Staff(createStaffForm.fname.data, createStaffForm.lname.data, createStaffForm.gender.data,
                                 createStaffForm.hp.data, createStaffForm.dob.data, createStaffForm.password.data,
                                 createStaffForm.address.data, createStaffForm.type.data)

        staffDict[staff.get_eID()] = staff
        db['Staff'] = staffDict
        db['staffCount'] = Staff.Staff.count

        db.close()
        return redirect(url_for('staffAccounts'))
    return render_template('createStaff.html', form=createStaffForm)


@app.route('/updateStaff/<int:eID>', methods=['GET', 'POST'])
def updateStaff(eID):
    updateStaffForm = UpdateStaffForm(request.form)
    eID2 = str(eID).zfill(6)
    if request.method == 'POST' and updateStaffForm.validate():
        staffDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            staffDict = db['Staff']
        except:
            print("Error in retrieving Staff from storage.db.")

        staff = staffDict.get(eID2)
        staff.set_fname(updateStaffForm.fname.data)
        staff.set_lname(updateStaffForm.lname.data)
        staff.set_gender(updateStaffForm.gender.data)
        staff.set_hp(updateStaffForm.hp.data)
        staff.set_address(updateStaffForm.address.data)
        staff.set_type(updateStaffForm.type.data)

        staffDict[staff.get_eID()] = staff
        db['Staff'] = staffDict
        db.close()
        return redirect(url_for('staffAccounts'))

    else:
        staffDict = {}
        db = shelve.open('storage.db', 'r')
        staffDict = db['Staff']
        db.close()

        staff = staffDict.get(eID2)
        updateStaffForm.fname.data = staff.get_fname()
        updateStaffForm.lname.data = staff.get_lname()
        updateStaffForm.gender.data = staff.get_gender()
        updateStaffForm.hp.data = staff.get_hp()
        updateStaffForm.address.data = staff.get_address()
        updateStaffForm.type.data = staff.get_type()

        return render_template('updateStaff.html', form=updateStaffForm)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LogInForm(request.form)
    field1 = False
    field2 = False

    if request.method == 'POST' and loginForm.validate():
        email = loginForm.email.data
        email = email.split("@")
        domain = email[1]

        userDict = {}
        logged = {}
        try:
            db = shelve.open('storage.db', 'c')
        except:
            print("Unable to retrieve storage.db")

        if domain == "monoqlo.com":
            try:
                userDict = db['Staff']
                db['Logged'] = {}
            except:
                print("Error in retrieving Staff from storage.db")
            for user, object in userDict.items():
                if user == email[0]:
                    field1 = True
                    if object.get_password() == loginForm.password.data:
                        field2 = True
                        logged[email[0]] = object.get_fname()

        else:
            print("User account.")

        if field1 == True and field2 == True:
            db['Logged'] = logged
            db.close()
            print("Successfully logged in!")
            return redirect(url_for('staffHome'))
        elif field1 == True and field2 == False:
            print("Invalid Email.")
        elif field1 == False and field2 == True:
            print("Invalid Password.")
        else:
            print("Invalid credentials. Please try again.")


    return render_template('login.html', form=loginForm)


@app.before_request
def accountCheck():
    user = {}
    staffs = {}

    admin = False

    try:
        db = shelve.open('storage.db', 'r')
        user = db['Logged']
        staffs = db['Staff']
        db.close()
    except:
        print("Error in retrieving storage.db")

    if user != {}:
        staff = list(user.keys())[0]
        for id, name in user.items():
            for key, object in staffs.items():
                if id == key:
                    if object.get_type == "Admin":
                        pass

    else:
        print("No user signed in")



@app.route('/logout')
def logout():
    dict = {}
    try:
        db = shelve.open('storage.db', 'r')
        db['Logged'] = dict
        db.close()
    except:
        print("No user logged in, or some other error lol")

    return redirect(url_for('home'))


@app.route('/staffAccounts')
def staffAccounts():
    staffDict = {}

    try:
        db = shelve.open("storage.db", "r")
        staffDict = db["Staff"]
    except:
        print("db error")
    else:
        db.close()

    #  loop through dict to save in list
    staffList = []
    for key in staffDict:
        staff = staffDict.get(key)
        staffList.append(staff)

    return render_template("staffAccounts.html", staffList=staffList, count=len(staffList))


@app.route('/deleteStaff/<int:eID>', methods=['GET', 'POST'])
def deleteStaff(eID):
    staffDict = {}
    db = shelve.open("storage.db", "w")
    staffDict = db["Staff"]

    eID2 = str(eID).zfill(6)
    staffDict.pop(eID2)  # action of removing the record
    db["Staff"] = staffDict  # put back to persistence
    db.close()

    # after we delete succesfully
    return redirect(url_for('staffAccounts'))


@app.route('/createAnnouncement', methods=['GET', 'POST'])
def createAnnouncement():
    createAnnouncementForm = CreateAnnouncement(request.form)

    if request.method == 'POST' and createAnnouncementForm.validate():
        annDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            annDict = db['Announcements']
            Announcement.Announcement.count = db['annCount']
        except:
            print("Error in retrieving Staff from storage.db.")
        announcement = Announcement.Announcement(createAnnouncementForm.date.data, createAnnouncementForm.title.data, createAnnouncementForm.description.data)

        annDict[Announcement.Announcement.count] = announcement
        db['Announcements'] = annDict
        db['annCount'] = Announcement.Announcement.count
        db.close()
        return redirect(url_for('retrieveAnnouncements'))
    return render_template('createAnnouncement.html', form=createAnnouncementForm)


@app.route('/retrieveAnnouncements')
def retreiveAnnouncements():
    annDict = {}

    try:
        db = shelve.open("storage.db", "r")
        annDict = db["Announcements"]
    except:
        print("db error")
    else:
        db.close()

    #  loop through dict to save in list
    annList = []
    for key in annDict:
        announcement = annDict.get(key)
        annList.append(announcement)

    return render_template("retrieveAnnouncements.html", annList=annList)


@app.route('/createNewReport')
def createNewReport():
    return render_template('create.html')


@app.route('/salesReports')
def salesReports():
    return render_template('salesReports.html')


@app.route('/catalogueHis')
def catalogueHis():
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    for key in itemDict:
        item = itemDict.get(key)
        itemList.append(item)
    return render_template('catalogueHis.html', itemList=itemList, count=len(itemList))


@app.route('/itemDetails/<id>/', methods=['GET', 'POST'])
def itemDetails(id):
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    item = itemDict.get(id)
    itemList.append(item)
    return render_template('itemDetails.html', itemList=itemList, count=len(itemList))


if __name__ == '__main__':
    app.run()
