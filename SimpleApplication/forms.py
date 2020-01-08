from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
class CreateUserForm(Form):
    firstName = StringField("First Name",[validators.Length(min=1, max=150),validators.DataRequired()])
    lastName = StringField("last Name",[validators.Length(min=1, max=150),validators.DataRequired()])
    membership=RadioField("Membership",choices=[("F","Fellow"),("S","Senior"),("P","Professional")],default="F")
    gender = SelectField('Gender', [validators.DataRequired()],choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],default='')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateItemForm(Form):
    itemName=StringField("Item Name", [validators.Length(min=1, max=150),validators.DataRequired()])
    itemType=RadioField("Item Type",choices=[("T","Top"),("B","Bottom")],default="T")
    itemGender = SelectField('Gender', [validators.DataRequired()],choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],default='')
    itemSerial = TextAreaField('Remarks', [validators.Optional()])
