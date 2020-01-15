import shelve

from wtforms import Form, StringField, SelectField, validators, ValidationError, FloatField,DateField

import invoiceclass
from invoiceclass import Invoice

def Iserialcheck(form, field,):
    global invoiceDict
    db = shelve.open('storage.db', 'c')
    try:
        invoiceDict = db['Invoice']
        invoiceclass.Invoice.countID = db['Invoicecount']
    except:
        print("Error in retrieving Invoice from storage.db.")
    if field.data in invoiceDict:
        pass
    else:
        raise ValidationError('Item Serial not found')


class CreateInvoiceForm(Form):
    invoiceNumber = Invoice.invoiceN
    invoiceDate = DateField("Invoice Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')
    shipmentDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')
    shipmentStatus = SelectField("Shipment Status", [validators.DataRequired()],choices=[('', 'Select'), ('Shipped', 'Shipped'), ('Received', 'Received')],default='')
    receivedDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')
    itemSerial = StringField("Item Serial",[validators.DataRequired(),Iserialcheck])


class EditInvoiceForm(Form):
    pass
