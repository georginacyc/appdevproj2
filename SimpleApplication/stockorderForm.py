import shelve

from wtforms import Form, StringField, SelectField, validators, ValidationError, IntegerField, DateField
import datetime
from StockOrder import StockOrder


def Iserialcheck(form, field):

    itemDict = {}
    db = shelve.open('storage.db', 'r')
    itemDict = db['Items']
    if field.data in itemDict:
        pass
    else:
        raise ValidationError('Serial number does not exist')
    db.close()

def checkquantity(form,field):
    if field.data>0:
        pass
    else:
        raise ValidationError("Quantity must be more than 0")

class CreateStockOrderForm(Form):
    stockorderNumber = StockOrder.get_stockorderNumber
    stockorderDate = DateField("Order Date ( d-m-Y )", [validators.DataRequired()],default=datetime.date.today, format='%d-%m-%Y')
    shipmentDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    shipmentStatus = "Ordered"
    receivedDate = "-"
    stockItemSerial = StringField("Item Serial", [validators.DataRequired(), Iserialcheck])
    stockorderQuantity = IntegerField("Order Quantity", [validators.DataRequired(),checkquantity])


class UpdateStockOrderForm(Form):
    stockorderNumber = StockOrder.stockorderN
    stockorderDate = DateField("Order Date ( d-m-Y )", render_kw={'disabled':''})
    shipmentDate = DateField("Shipment Date ( d-m-Y )", render_kw={'disabled':''})
    shipmentStatus = "Received"
    receivedDate = DateField("Received Date ( d-m-Y )", [validators.DataRequired()], default=datetime.date.today, format='%d-%m-%Y')
    stockItemSerial = StringField("Item Serial", render_kw={'disabled':''})
    stockorderQuantity = IntegerField("Order Quantity", render_kw={'disabled':''})
