from flask import Flask, render_template, request, redirect, url_for
from forms import CreateUserForm
from itemForm import CreateItemForm, serialcheck
import shelve, User, itemclass, itemForm

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
    return render_template('inventory.html')


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
    return redirect(url_for(itempage))


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
            item = itemclass.Item(createItemForm.itemName.data, createItemForm.itemCategory.data,
                                  createItemForm.itemGender.data, createItemForm.itemSerial.data, createItemForm.itemCost.data,createItemForm.itemPrice.data)
            itemsDict[item.get_itemSerial()] = item
            db['Items'] = itemsDict
            db['itemcount']=itemclass.Item.countID
            print(db['Items'])
            db.close()
            return redirect(url_for('itempage'))
        return redirect(url_for('itempage'))
    return render_template('itemCreation.html', form=createItemForm)


@app.route('/createNewReport')
def createNewReport():
    return render_template('create.html')

@app.route('/salesReports')
def salesReports():
    return render_template('salesReports.html')

if __name__ == '__main__':
    app.run()
