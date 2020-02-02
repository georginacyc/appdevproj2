import shelve

from wtforms import Form, StringField, SelectField, validators, ValidationError, IntegerField, DateField

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


class CreateStockOrderForm(Form):
    stockorderNumber = StockOrder.get_stockorderNumber
    stockorderDate = DateField("Order Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    shipmentDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    shipmentStatus = "Ordered"
    receivedDate = "-"
    stockItemSerial = StringField("Item Serial", [validators.DataRequired(), Iserialcheck])
    stockorderQuantity = IntegerField("Order Quantity", [validators.DataRequired()])


class UpdateStockOrderForm(Form):
    stockorderNumber = StockOrder.stockorderN
    stockorderDate = DateField("Order Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y',render_kw={'disabled':''})
    shipmentDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y',render_kw={'disabled':''})
    shipmentStatus = SelectField("Shipment Status", [validators.DataRequired()],choices=[('Received', 'Received')], render_kw={"placeholder": "Ordered"})
    receivedDate = DateField("Received Date ( d-m-Y )", [validators.DataRequired()], format='%d-%m-%Y')
    stockItemSerial = StringField("Item Serial", [validators.DataRequired(), Iserialcheck],render_kw={'disabled':''})
    stockorderQuantity = IntegerField("Order Quantity", [validators.DataRequired()],render_kw={'disabled':''})
