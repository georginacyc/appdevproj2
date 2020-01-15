from wtforms import Form, StringField, SelectField, validators, ValidationError, FloatField,DateField

class CreateInvoiceForm(Form):
    invoiceDate = DateField("Invoice Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')
    shipmentDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')
    shipmentStatus = SelectField("Shipment Status", [validators.DataRequired()],choices=[('', 'Select'), ('Shipped', 'Shipped'), ('Received', 'Received')],default='')
    receivedDate = DateField("Shipment Date ( d-m-Y )", [validators.DataRequired()],format='%d-%m-%Y')

class EditInvoiceForm(Form):
    pass
