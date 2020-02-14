from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.utils import secure_filename
from forms import CreateUserForm, CreateStaffForm, LogInForm, UpdateUserForm, UpdateStaffForm, CreateAnnouncement, ContactUsForm, ShowDetailsForm, PaymentForm, ShippingForm, createtestdataForm, CreateAboutUsForm

from Cart import Cart, addtocartForm
from stockorderForm import CreateStockOrderForm, UpdateStockOrderForm
from itemForm import CreateItemForm, serialcheck
import shelve, User, Item, itemForm, Staff, StockOrder, os, uuid, Announcement, string, random, Cart, ContactUs, Shipping, Payment, Sale, AboutUs
import json

# import os, pygal
# from pygal.style import CleanStyle, LightStyle


UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.from_mapping(
    SECRET_KEY='yeet'
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def retrieveFiles():
    entries = os.listdir(app.config['UPLOAD_FOLDER'])
    fileList = []
    for entry in entries:
        fileList.append(entry)
    return fileList


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cleartestCart', methods=['GET', 'POST'])
def cleartestCart():
    cartDict = {}
    db = shelve.open('storage.db', 'w')
    cartDict = db['Cart']

    cartDict.clear()  # action of removing the record
    db['Cart'] = cartDict  # put back to persistence
    db.close()

    # after we delete successfully
    return redirect(url_for('home'))


@app.route('/invoice')
def invoice():
    cartDict = {}
    db = shelve.open('storage.db', 'r')
    cartDict = db['Cart']
    db.close()

    cartList = []
    for key in cartDict:
        item = cartDict.get(key)
        cartList.append(item)


    shippingDict = {}
    db = shelve.open('storage.db', 'r')
    shippingDict = db['Shipping']
    db.close()

    shippingList = []
    for email in shippingDict:
        shipping = shippingDict.get(email)
        shippingList.append(shipping)


    paymentDict = {}
    db = shelve.open('storage.db', 'r')
    paymentDict = db['Payment']
    db.close()

    paymentList = []
    for cardno in paymentDict:
        shipping = paymentDict.get(cardno)
        paymentList.append(shipping)



    return render_template('invoice.html', cartList=cartList, shippingList=shippingList, paymentList=paymentList)



@app.route('/testcart', methods=['GET', 'POST'])
def testcart():
    global db
    cartDict = {}
    try:
        db = shelve.open('storage.db', 'r')
        cartDict = db['Cart']
    except:
        print("Error")
    finally:
        db.close()

    cartList = []
    for key in cartDict:
        item = cartDict.get(key)
        cartList.append(item)
    return render_template('testcart.html', cartList=cartList, count=len(cartList))


@app.route('/deletetestCart/<cart>/', methods=['GET', 'POST'])
def deletetestCart(cart):
    cartDict = {}
    db = shelve.open('storage.db', 'w')
    cartDict = db['Cart']

    cartDict.pop(cart)  # action of removing the record
    db['Cart'] = cartDict  # put back to persistence
    db.close()

    # after we delete successfully
    return redirect(url_for('testcart'))



# @app.route('/cart', methods=['GET', 'POST'])
# def cart():
#     global db
#     cartDict = {}
#     try:
#         db = shelve.open('storage.db', 'r')
#         cartDict = db['Cart']
#     except:
#         print("Error")
#     finally:
#         db.close()
#
#     cartList = []
#     for key in cartDict:
#         item = cartDict.get(key)
#         cartList.append(item)
#     return render_template('cart.html', cartList=cartList, count=len(cartList))
#
#
# @app.route('/deleteCart/<cart>/', methods=['GET', 'POST'])
# def deleteCart(cart):
#     cartDict = {}
#     db = shelve.open('storage.db', 'w')
#     cartDict = db['Cart']
#
#     cartDict.pop(cart)  # action of removing the record
#     db['Cart'] = cartDict  # put back to persistence
#     db.close()
#
#     # after we delete successfully
#     return redirect(url_for('cart'))


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():

    paymentForm = PaymentForm(request.form)

    if request.method == 'POST' and paymentForm.validate():
        paymentDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            paymentDict = db['Payment']
        except:
            print("Error in retrieving Items from storage.db.")
        payment = Payment.Payment(paymentForm.name.data, paymentForm.cardno.data,
                                    paymentForm.date.data, paymentForm.cvv.data)
        paymentDict[payment.get_name()] = payment
        db['Payment'] = paymentDict
        db.close()
        return redirect(url_for('invoice'))
    return render_template('checkout.html', form=paymentForm)

@app.route('/retrievepayment')
def retrievePayment():
    paymentDict = {}
    db = shelve.open('storage.db', 'r')
    paymentDict = db['Payment']
    db.close()

    paymentList = []
    for cardno in paymentDict:
        shipping = paymentDict.get(cardno)
        paymentList.append(shipping)

    return render_template('retrievepayment.html', paymentList=paymentList)


@app.route('/address', methods=['GET', 'POST'])
def address():
    shippingForm = ShippingForm(request.form)

    if request.method == 'POST' and shippingForm.validate():
        shippingDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            shippingDict = db['Shipping']
        except:
            print("Error in retrieving Items from storage.db.")
        shipping = Shipping.Shipping(shippingForm.fname.data, shippingForm.lname.data,
                                    shippingForm.email.data, shippingForm.hp.data, shippingForm.address.data, shippingForm.address2.data, shippingForm.postal.data)
        shippingDict[shipping.get_email()] = shipping
        db['Shipping'] = shippingDict
        db.close()
        return redirect(url_for('checkout'))
    return render_template('address.html', form=shippingForm)

@app.route('/retrieveShipping')
def retrieveShipping():
    shippingDict = {}
    db = shelve.open('storage.db', 'r')
    shippingDict = db['Shipping']
    db.close()

    shippingList = []
    for email in shippingDict:
        shipping = shippingDict.get(email)
        shippingList.append(shipping)

    return render_template('retrieveShipping.html', shippingList=shippingList)

@app.route('/contactUs', methods=['GET', 'POST'])
def contactUs():
    contactUsForm = ContactUsForm(request.form)

    if request.method == 'POST' and contactUsForm.validate():
        contactDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            contactDict = db['Contact']
        except:
            print("Error in retrieving Items from storage.db.")
        contact = ContactUs.Contact(contactUsForm.fname.data, contactUsForm.lname.data,
                                    contactUsForm.email.data, contactUsForm.text.data)
        contactDict[contact.get_email()] = contact
        db['Contact'] = contactDict
        db.close()
        return redirect(url_for('home'))
    return render_template('contactUs.html', form=contactUsForm)


@app.route('/retrieveContact')
def retrieveContact():
    contactDict = {}
    db = shelve.open('storage.db', 'r')
    contactDict = db['Contact']
    db.close()

    contactList = []
    for email in contactDict:
        contact = contactDict.get(email)
        contactList.append(contact)

    return render_template('retrieveContact.html', contactList=contactList, count=len(contactList))


@app.route('/deleteContact/<email>/', methods=['GET', 'POST'])
def deleteContact(email):
    contactDict = {}
    db = shelve.open('storage.db', 'w')
    contactDict = db['Contact']

    contactDict.pop(email)  # action of removing the record
    db['Contact'] = contactDict  # put back to persistence
    db.close()

    # after we delete successfully
    return redirect(url_for('retrieveContact'))


@app.route('/staffHome')
def staffHome():  # staff Home route
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
    keyList = []
    count = 0
    for key in annDict:  # to display 5 latest announcements
        if count < 5:
            announcement = annDict.get(key)
            annList.append(announcement)
            keyList.append(key)
        else:
            break

        count += 1

    return render_template('staffHome.html', annList=annList, keyList=keyList)



@app.route('/inventory')
def inventory():
    return render_template('viewStock.html')


@app.route('/viewStockOrders')
def viewStockOrders():
    stockorderDict = {}
    db = shelve.open('storage.db', 'r')
    stockorderDict = db['StockOrder']
    db.close()

    stockorderList = []
    for key in stockorderDict:
        stockorder = stockorderDict.get(key)
        stockorderList.append(stockorder)
    return render_template('viewStockOrders.html', stockorderList=stockorderList, count=len(stockorderList))


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


@app.route('/createStockOrder', methods=['GET', 'POST'])
def createStockOrder():
    createStockOrderForm = CreateStockOrderForm(request.form)

    if request.method == 'POST' and createStockOrderForm.validate():
        stockorderDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            stockorderDict = db['StockOrder']
            StockOrder.StockOrder.countID = db['stockordercount']
        except IOError:
            print("IOError")
        except:
            print("Error in retrieving the order from storage.db.")

        stockorder = StockOrder.StockOrder(createStockOrderForm.stockorderDate.data,
                                           createStockOrderForm.shipmentDate.data, "Ordered", "",
                                           createStockOrderForm.stockItemSerial.data,
                                           createStockOrderForm.stockorderQuantity.data)
        print(stockorder.get_stockorderNumber())
        stockorderDict[stockorder.get_stockorderNumber()] = stockorder
        db['StockOrder'] = stockorderDict
        db['stockordercount'] = StockOrder.StockOrder.countID
        print(db['StockOrder'])
        db.close()

        return redirect(url_for('viewStockOrders'))
    return render_template('createStockOrder.html', form=createStockOrderForm)


@app.route('/updateStockOrder/<int:id>/', methods=['GET', 'POST'])
def updateStockOrder(id):
    updateStockOrderForm = UpdateStockOrderForm(request.form)
    quantity = 0
    if request.method == 'POST' and updateStockOrderForm.validate():
        stockorderDict = {}
        db = shelve.open('storage.db', 'w')
        stockorderDict = db['StockOrder']

        stockorder = stockorderDict.get(id)
        stockorder.set_shipmentStatus("Received")
        stockorder.set_receivedDate(updateStockOrderForm.receivedDate.data)
        db['StockOrder'] = stockorderDict
        db.close()
        return redirect(url_for('viewStockOrders'))
    else:
        stockorderDict = {}
        db = shelve.open('storage.db', 'r')
        stockorderDict = db['StockOrder']
        print(stockorderDict)
        db.close()

        stockorder = stockorderDict.get(id)
        print(stockorder)
        updateStockOrderForm.stockorderDate.data = stockorder.get_stockorderDate()
        updateStockOrderForm.shipmentDate.data = stockorder.get_shipmentDate()
        updateStockOrderForm.receivedDate.data = stockorder.get_receivedDate()
        updateStockOrderForm.stockItemSerial.data = stockorder.get_stockItemSerial()
        updateStockOrderForm.stockorderQuantity.data = stockorder.get_stockorderQuantity()

        quantity = stockorder.get_stockorderQuantity()
        itemDict = {}
        db = shelve.open('storage.db', 'w')
        itemDict = db['Items']

        item = itemDict.get(stockorder.get_stockItemSerial())
        item.set_itemQuantity(quantity)
        item.set_itemStockStatus()
        db['Items'] = itemDict
        db.close()

        return render_template('updateStockOrder.html', form=updateStockOrderForm)


@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    createUserForm = CreateUserForm(request.form)

    if request.method == 'POST' and createUserForm.validate():
        print('SimpleApp Ln 115')
        usersDict = {}
        db = shelve.open('storage.db', 'c')
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
                             createUserForm.pw.data, createUserForm.confirmpw.data)
            usersDict[user.get_email()] = user
            db['Users'] = usersDict
            db.close()

        return redirect(url_for('home'))
    return render_template('createUser.html', form=createUserForm)


@app.route('/retrieveUsers')
def retrieveUsers():
    usersDict = {}
    db = shelve.open('storage.db', 'r')
    usersDict = db['Users']
    db.close()

    usersList = []
    for email in usersDict:
        user = usersDict.get(email)
        usersList.append(user)

    return render_template('retrieveUsers.html', usersList=usersList, count=len(usersList))


@app.route('/updateUser/<email>/', methods=['GET', 'POST'])
def updateUser(email):
    updateUserForm = UpdateUserForm(request.form)

    if request.method == 'POST' and updateUserForm.validate():


        userDict = {}
        db = shelve.open('storage.db', 'w')
        try:
            userDict = db['Users']
        except:
            print("Error in retrieving User from storage.db")
        user = userDict.get(email)
        user.set_firstName(updateUserForm.firstName.data)
        user.set_lastName(updateUserForm.lastName.data)
        user.set_gender(updateUserForm.gender.data)
        user.set_email(updateUserForm.email.data)
        userDict[email] = user
        db['Users'] = userDict

        db.close()

        return redirect(url_for('retrieveUsers'))
    else:
        userDict = {}
        db = shelve.open('storage.db', 'r')
        userDict = db['Users']
        db.close()
        user = userDict.get(email)
        updateUserForm.firstName.data = user.get_firstName()
        updateUserForm.lastName.data = user.get_lastName()
        updateUserForm.gender.data = user.get_gender()
        updateUserForm.email.data = user.get_email()

        return render_template('updateUser.html', form=updateUserForm)


@app.route('/deleteUser/<email>/', methods=['GET', 'POST'])
def deleteUser(email):
    usersDict = {}
    db = shelve.open('storage.db', 'w')
    usersDict = db['Users']

    usersDict.pop(email)  # action of removing the record
    db['Users'] = usersDict  # put back to persistence
    db.close()

    # after we delete successfully
    return redirect(url_for('retrieveUsers'))


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


@app.route('/createItem', methods=['GET', 'POST'])
def createItem():
    createItemForm = CreateItemForm(request.form)

    if request.method == 'POST' and createItemForm.validate():
        itemsDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            itemsDict = db['Items']
            Item.Item.countID = db['itemcount']
        except:
            print("Error in retrieving Items from storage.db.")
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
            filename = secure_filename(str(createItemForm.itemSerial.data + ".jpg"))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            item = Item.Item(createItemForm.itemSerial.data, createItemForm.itemName.data,
                             createItemForm.itemCategory.data, createItemForm.itemGender.data,
                             createItemForm.itemCost.data, createItemForm.itemPrice.data,
                             createItemForm.itemDescription.data)
            itemsDict[item.get_itemSerial()] = item
            db['Items'] = itemsDict
            db['itemcount'] = Item.Item.countID
            db.close()

        return redirect(url_for('itempage'))
    return render_template('createItem.html', form=createItemForm)


@app.route('/updateItem/<id>/', methods=['GET', 'POST'])
def updateItem(id):
    updateItemForm = CreateItemForm(request.form)
    if request.method == 'POST' and updateItemForm.validate():
        itemDict = {}
        db = shelve.open('storage.db', 'w')
        itemDict = db['Items']

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
            filename = secure_filename(str(updateItemForm.itemSerial.data + ".jpg"))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        item = itemDict.get(id)
        item.set_itemName(updateItemForm.itemName.data)
        item.set_itemSerial(updateItemForm.itemSerial.data)
        item.set_itemCategory(updateItemForm.itemCategory.data)
        item.set_itemGender(updateItemForm.itemGender.data)
        item.set_itemCost(updateItemForm.itemCost.data)
        item.set_itemPrice(updateItemForm.itemPrice.data)
        item.set_itemDescription(updateItemForm.itemDescription.data)
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
        updateItemForm.itemDescription.data = item.get_itemDescription()
        return render_template('updateItem.html', form=updateItemForm)


@app.route('/customerDemo')  # route to show customer analytics/demographic
def customerDemo():
    femCount = 0
    maleCount = 0

    usersDict = {}
    ageList = []

    db = shelve.open('storage.db', 'c')
    usersDict = db["Users"]

    for x in usersDict.values():  # for loop through dictionary to count gender
        if x.get_gender() == "F" or x.get_gender() == "Female":
            femCount += 1
        elif x.get_gender() == "M" or x.get_gender() == "Male":
            maleCount += 1

    for x in usersDict.values():  # for loop to get a list of all the ages of our customers
        dob = str(x.get_DOB())  # str the dob to be able to .split()
        splitted = dob.split("-")
        year = splitted[0]  # retrieve year

        age = 2020 - int(year)  # get age

        ageList.append(age)

    pie = pygal.Pie(style=LightStyle)  # creating pie chart
    pie.title = "Proportion of Male and Female Customers"  # title of pie chart
    pie.add("Female", femCount)  # adds "Female" as an attribute of the chart and its count
    pie.add("Male", maleCount)  # adds "Male" as an attribute of the chart and its count
    pie = pie.render_data_uri()  # renders chart

    ageCount = {}  # dictionary to hold count of individual ages
    for x in ageList:  # x = age
        ageCount[x] = ageCount.get(x, 0) + 1  # plus one to the value of the key, creating it with value zero if key does not exist

    pie2 = pygal.Pie(style=CleanStyle)  # creating pie chart
    pie2.title = "Proportion of Customer Ages"  # title
    for age, count in ageCount.items():  # for loop to add an attribute for every unique age
        age = str(age)  # str age to overcome a problem with .render_data_uri()
        pie2.add(age, count)  # adds attribute and count
    pie2 = pie2.render_data_uri()  # render

    return render_template("customerDemo.html", chart = pie, chart2 = pie2)



@app.route('/createStaff', methods=['GET', 'POST'])
def createStaff():
    createStaffForm = CreateStaffForm(request.form)

    if request.method == 'POST' and createStaffForm.validate():
        staffDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            Staff.Staff.count = int(db['staffCount'])
            staffDict = db['Staff']
        except:
            print("Error in retrieving Staff from storage.db.")
        staff = Staff.Staff(createStaffForm.fname.data, createStaffForm.lname.data, createStaffForm.gender.data,
                            createStaffForm.hp.data, createStaffForm.dob.data, createStaffForm.password.data,
                            createStaffForm.address.data, createStaffForm.type.data)

        staffDict[staff.get_eID()] = staff  # creates a key value pair in staffDict to "register" staff. key is Employee ID, value is staff object
        db['Staff'] = staffDict  # put dict back in persistence
        db['staffCount'] = Staff.Staff.count  # since eID is unique and incremental, count is saved back into persistence

        db.close()
        return redirect(url_for('staffAccounts'))  # for admin to look at staff accounts, to check that staff account is created successfully
    return render_template('createStaff.html', form=createStaffForm)


@app.route('/updateStaff/<int:eID>', methods=['GET', 'POST'])
def updateStaff(eID):
    updateStaffForm = UpdateStaffForm(request.form)
    eID2 = str(eID).zfill(6)  # eID is 6 digits long, so first few accounts will have leading zeroes. This is to fill the leading zeroes
    if request.method == 'POST' and updateStaffForm.validate():
        staffDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            staffDict = db['Staff']
        except:
            print("Error in retrieving Staff from storage.db.")

        staff = staffDict.get(eID2)  # gets staff object that admin is updating

        # updates the following fields
        staff.set_fname(updateStaffForm.fname.data)
        staff.set_lname(updateStaffForm.lname.data)
        staff.set_gender(updateStaffForm.gender.data)
        staff.set_hp(updateStaffForm.hp.data)
        staff.set_address(updateStaffForm.address.data)
        staff.set_type(updateStaffForm.type.data)

        # checks if admin wants to reset the password of staff account
        if updateStaffForm.resetpass.data == True:
            hp = staff.get_hp()

            # format of pw = staff first name and last 4 digits of hp
            newpass = staff.get_fname() + hp[-4:]

            # sets the new password
            staff.set_password(newpass)

            print("Successfully resetted password. New password is", newpass)

        # puts newly updated staff object back into persistence
        staffDict[staff.get_eID()] = staff
        db['Staff'] = staffDict
        db.close()
        return redirect(url_for('staffAccounts'))

    else:
        staffDict = {}
        db = shelve.open('storage.db', 'r')
        staffDict = db['Staff']
        db.close()

        # retrieves staff object in question
        staff = staffDict.get(eID2)
        # sets fields of form
        updateStaffForm.fname.data = staff.get_fname()
        updateStaffForm.lname.data = staff.get_lname()
        updateStaffForm.gender.data = staff.get_gender()
        updateStaffForm.hp.data = staff.get_hp()
        updateStaffForm.dob.data = staff.get_dob()
        updateStaffForm.address.data = staff.get_address()
        updateStaffForm.type.data = staff.get_type()

        return render_template('updateStaff.html', form=updateStaffForm)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LogInForm(request.form)
    field1 = False
    field2 = False
    field3 = False
    field4 = False

    if request.method == 'POST' and loginForm.validate():
        email = loginForm.email.data  # retrieves email from login form
        emailSplit = email.split("@")  # splits email for staff account check
        domain = emailSplit[1]  # gets domain of emaill

        userDict = {}
        try:
            db = shelve.open('storage.db', 'c')
        except:
            print("Unable to retrieve storage.db")

        if domain == "monoqlo.com":  # checks if email is company issued
            try:
                userDict = db['Staff']
            except:
                print("Error in retrieving Staff from storage.db")

            for user, object in userDict.items():  # loops through each key value pair in staffDict
                if user == emailSplit[0]:  # since staff objects are stored with eID as key, which is the first half of their email, we check if emailSplit[0] matches the key
                    field1 = True
                    if object.get_password() == loginForm.password.data:  # if eID matches, this checks password
                        field2 = True
                        session["email"] = email  # sets session email as given email
                        session["name"] = object.get_fname()  # sets staff first name in session
                        session["type"] = object.get_type()  # sets staff account type in session

        else:
            print("User account.")
            try:
                userDict = db['Users']
            except:
                print("Error in retrieving User from storage.db")
            finally:
                for user, object in userDict.items():
                    if user == email:
                        field3 = True
                        print("1")
                        if object.get_pw() == loginForm.password.data:
                            field4 = True
                            session["useremail"] = email
                            session["username"] = object.get_firstName()

        if field1 == True and field2 == True:  # if staff login passes both email and password, they will be redirected to staffHome
            print("Successfully logged in!")
            return redirect(url_for('staffHome'))
        elif field3 == True and field4 == True:
            db.close()
            return redirect(url_for('home'))
        elif field1 == False and field2 == True or field3 == False and field4 == True:  # invalid email entered
            print("Invalid Email.")
        elif field1 == True and field2 == False or field3 == True and field4 == False:  # invalid password
            print("Invalid Password.")
        else:  # both fields invalid
            print("Invalid credentials. Please try again.")

    return render_template('login.html', form=loginForm)


@app.route('/logout')
def logout():  # when users logout, session storages are cleared and they are redirected back home.html
    try:
        session["email"] = ""
        session["name"] = ""
        session["type"] = ""
        session["useremail"] = ""
        session["username"] = ""
        print("logged out")
    except:
        print("No user logged in, or some other error lol")

    return redirect(url_for('home'))


@app.route('/staffAccounts')
def staffAccounts():  # lists staff accounts
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
def deleteStaff(eID):  # delete staff from persistence
    staffDict = {}
    db = shelve.open("storage.db", "w")
    staffDict = db["Staff"]

    eID2 = str(eID).zfill(6)  # fills eID just in case
    staffDict.pop(eID2)  # action of removing the record
    db["Staff"] = staffDict  # put back to persistence
    db.close()

    # after we delete successfully
    return redirect(url_for('staffAccounts'))


@app.route('/staffAccountDetails', methods=['GET', 'POST'])
def staffAccountDetails():  # for normal staff to see their own account details
    showDetailsForm = ShowDetailsForm(request.form)

    email = session["email"]  # retrieves staff's email

    split = email.split("@")
    eID = split[0]  # gets eID from email

    staffDict = {}
    db = shelve.open('storage.db', 'r')
    staffDict = db['Staff']
    staff = staffDict.get(eID)  # retrieves their object

    if request.method == "POST" and showDetailsForm.validate():  # if they choose to change their password
        if showDetailsForm.oldpass.data == staff.get_password():  # checks to see if they can enter their current password for security measures
            print("Successfully changed password!")
            staff.set_password(showDetailsForm.newpass.data)  # sets new password

            staffDict[eID] = staff  # puts updated staff object back into storage
            db["Staff"] = staffDict
            db.close()

            return redirect(url_for('logout'))  # logs them out to let them log in with their new password

    else:
        #  sets fields of form
        showDetailsForm.name.data = staff.get_fname() + " " + staff.get_lname()
        showDetailsForm.type.data = staff.get_type()
        showDetailsForm.gender.data = staff.get_gender()
        showDetailsForm.dob.data = staff.get_dob()
        showDetailsForm.hp.data = staff.get_hp()
        showDetailsForm.address.data = staff.get_address()

    return render_template('staffAccountDetails.html', form=showDetailsForm)


@app.route('/createAnnouncement', methods=['GET', 'POST'])
def createAnnouncement():  # for admin to create announcement
    createAnnouncementForm = CreateAnnouncement(request.form)

    if request.method == 'POST' and createAnnouncementForm.validate():
        annDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            annDict = db['Announcements']
            Announcement.Announcement.count = int(db["annCount"])
        except:
            print("Error in retrieving Staff from storage.db.")

        # creates announcement object
        announcement = Announcement.Announcement(createAnnouncementForm.date.data, createAnnouncementForm.title.data)
        announcement.set_description(createAnnouncementForm.description.data)

        annDict[Announcement.Announcement.count] = announcement  # puts it into dict, with count as key

        sort = dict(sorted(annDict.items(), key=lambda x: x[0], reverse=True))  # sorts dict so that the most recent one will be first for retrieving purposes

        db['Announcements'] = sort
        db['annCount'] = Announcement.Announcement.count  # saves count so that future announcements can be sorted
        db.close()
        return redirect(url_for('retrieveAnnouncements'))
    return render_template('createAnnouncement.html', form=createAnnouncementForm)


@app.route('/retrieveAnnouncements')
def retrieveAnnouncements():  # to display announcements for admin
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


@app.route('/retrieveNormalAnnouncements')
def retrieveNormalAnnouncements():  # to display announcements for normal staff
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

    return render_template("retrieveNormalAnnouncements.html", annList=annList)


@app.before_request
def deleteDict():  # to use for deletion of any persistence
    dict = {}
    # db = shelve.open("storage.db", "w")
    # db["Shipping"] = dict
    #db["Items"] = dict
    #db["StockOrder"] = dict
    #db["stockordercount"] = dict
    # # db["staffCount"] = dict
    # db.close()
    # print("Cleared")


@app.route('/deleteAnnouncement/<int:id>', methods=['GET', 'POST'])
def deleteAnnouncement(id):  # for admin to delete annnouncements
    annDict = {}
    db = shelve.open("storage.db", "w")
    annDict = db["Announcements"]

    annDict.pop(id)  # action of removing the record
    db["Announcements"] = annDict  # put back to persistence
    db.close()

    # after we delete successfully
    return redirect(url_for('retrieveAnnouncements'))

@app.route('/salesReports', methods=["GET"])
def salesReports():
    try:
        db = shelve.open("storage.db", "r")
        salesDict = db["Sales"]
    except:
        print("db error")
    else:
        db.close()

    salesList = []
    for key in salesDict:
        sales = salesDict.get(key)
        salesList.append(sales)

    from datetime import datetime, timedelta
    date_chart = pygal.Line(x_label_rotation=20)
    date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
    datetime(2020, 2, 9),
    datetime(2020, 2, 10),
    datetime(2020, 2,11)])
    date_chart.add("Sales", [136, 207, 57])
    date_chart.render()
    return render_template('salesReports.html', date_chart=date_chart, salesList=salesList)

@app.route('/catalogueHis')
def catalogueHis():
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    itemTopsList = []
    itemBotsList = []
    for key in itemDict:
        if key[9] == "M":
            item = itemDict.get(key)
            itemList.append(item)
            if key[8] == "T":
                itemTopsList.append(item)
            elif key[8] == "B":
                itemBotsList.append(item)
    return render_template('catalogueHis.html', itemList=itemList, itemTopsList=itemTopsList,
                           itemBotsList=itemBotsList, count=len(itemList))


@app.route('/catalogueHers')
def catalogueHers():
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    itemTopsList = []
    itemBotsList = []
    for key in itemDict:
        if key[9] == "F":
            item = itemDict.get(key)
            itemList.append(item)
            if key[8] == "T":
                itemTopsList.append(item)
            elif key[8] == "B":
                itemBotsList.append(item)
    return render_template('catalogueHers.html', itemList=itemList, itemTopsList=itemTopsList,
                           itemBotsList=itemBotsList, count=len(itemList))


@app.route('/catalogueItemDetailsHis/<id>/', methods=['GET', 'POST'])
def itemDetailsHis(id):
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    item = itemDict.get(id)
    itemList.append(item)

    serial = item.get_itemSerial()
    addtocart = addtocartForm(request.form)
    if request.method == 'POST' and addtocart.validate():
        cartDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            cartDict = db['Cart']
            print("created")
        except:
            print("Error in retrieving cart from storage db.")
        cartDict[serial] = item
        db['Cart'] = cartDict
        print(cartDict.keys())
        db.close()

    return render_template('catalogueItemDetailsHis.html', itemList=itemList, count=len(itemList))


@app.route('/catalogueItemDetailsHers/<id>/', methods=['GET', 'POST'])
def itemDetailsHers(id):
    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    db.close()

    itemList = []
    item = itemDict.get(id)
    itemList.append(item)

    serial = item.get_itemSerial()
    addtocart = addtocartForm(request.form)
    if request.method == 'POST' and addtocart.validate():
        cartDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            cartDict = db['Cart']
            print("created")
        except:
            print("Error in retrieving cart from storage db.")
        cartDict[serial] = item
        db['Cart'] = cartDict
        print(cartDict.keys())
        db.close()
    return render_template('catalogueItemDetailsHers.html', itemList=itemList, count=len(itemList))

@app.route('/createtestdata', methods=['GET', 'POST'])
def createtestdata():
    CreatetestdataForm=createtestdataForm(request.form)

    if request.method == 'POST':
        salesDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            salesDict = db['Sales']
        except IOError:
            print("IOError")
        except:
            print("Error in retrieving the order from storage.db.")

        sale = Sale.Sale(CreatetestdataForm.saleDate.data, CreatetestdataForm.saleAmt.data)
        salesDict[sale.get_saleDate()]=[sale.get_saleAmt()]
        db['Sales'] = salesDict
        print(db['Sales'])
        db.close()
    return render_template('createtestdata.html', form=CreatetestdataForm)

@app.route('/createAboutUs', methods=['GET', 'POST'])
def createAboutUs():
    createAboutUsForm=CreateAboutUsForm(request.form)

    if request.method == 'POST':
        aboutUsDict = {}
        db = shelve.open('storage.db', 'c')
        try:
            aboutUsDict = db['AboutUs']
        except IOError:
            print("IOError")
        except:
            print("Error in retrieving the info from storage.db.")
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
            filename = secure_filename(str(createAboutUsForm.name.data + ".jpg"))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            aboutUs = AboutUs.AboutUs(createAboutUsForm.name.data, createAboutUsForm.itemName.data)
            aboutUs[aboutUs.get_aboutUsName()] = aboutUs
            db['AboutUs'] = aboutUsDict
            db.close()

    return render_template('/createAboutUs.html', form=createAboutUsForm)

@app.route('/aboutUs',methods=['GET'])
def aboutUs():
    aboutUsDict = {}
    db = shelve.open('storage.db', 'r')
    aboutUsDict = db['AboutUs']
    db.close()

    PersonList=[]
    for key in aboutUsDict:
        person=aboutUsDict.get(key)
        PersonList.append(person)

    return render_template('aboutUs.html',list=PersonList)
if __name__ == '__main__':
    app.run()
