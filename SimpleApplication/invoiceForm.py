from wtforms import Form, StringField, SelectField, validators, ValidationError, FloatField,DateField

class CreateInvoiceForm(Form):
    invoiceNumber = StringField("Invoice Number",[validators.Length(min=1, max=150),validators.DataRequired()])
    invoiceDate = DateField("Invoice Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')
    shipmentDate = DateField("shipment Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')
    shipmentStatus = "To be shipped"
    receivedDate = DateField("shipment Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')

class EditInvoiceForm(Form):
    pass
