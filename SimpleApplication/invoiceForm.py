import shelve

from wtforms import Form, StringField, SelectField, validators, ValidationError, IntegerField, DateField

import Item
from Invoice import Invoice


def Iserialcheck(form, field):

    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    if field.data in itemDict:
        pass
    else:
        raise ValidationError('Item Serial not found')
    db.close()


class CreateInvoiceForm(Form):
    invoiceNumber = Invoice.invoiceN
    invoiceDate = DateField("Invoice Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    shipmentDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    itemSerial = StringField("Item Serial", [validators.DataRequired(), Iserialcheck])
    orderQuantity = IntegerField("Order Quantity", [validators.DataRequired()])


class UpdateInvoiceForm(Form):
    shipmentStatus = SelectField("Shipment Status", [validators.DataRequired()],choices=[('', 'Select'),('Ordered', 'Ordered'), ('Shipped', 'Shipped'), ('Received', 'Received')], default='')
    receivedDate = DateField("Received Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
