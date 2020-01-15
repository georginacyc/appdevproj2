import shelve

from wtforms import Form, StringField, SelectField, validators, ValidationError, IntegerField, DateField

import itemclass
from invoiceclass import Invoice


def Iserialcheck(form, field):
    itemsDict = {}
    db = shelve.open('storage.db', 'r')
    try:
        itemsDict = db['Items']
        itemclass.Item.countID = db['itemcount']
    except:
        print("Error in retrieving Items from storage.db.")
    if field.data in itemsDict:
        pass
    else:
        raise ValidationError('Item Serial not found')
    db.close()


class CreateInvoiceForm(Form):
    invoiceNumber = Invoice.invoiceN
    invoiceDate = DateField("Invoice Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    shipmentDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    shipmentStatus = SelectField("Shipment Status", [validators.DataRequired()],choices=[('', 'Select'), ('Shipped', 'Shipped'), ('Received', 'Received')], default='')
    receivedDate = DateField("Received Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    itemSerial = StringField("Item Serial", [validators.DataRequired(), Iserialcheck])
    orderQuantity = IntegerField("Order Quantity", [validators.DataRequired])


class EditInvoiceForm(Form):
    pass
