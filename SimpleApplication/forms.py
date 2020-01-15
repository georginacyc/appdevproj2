from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
class CreateUserForm(Form):
    firstName = StringField("First Name",[validators.Length(min=1, max=150),validators.DataRequired()])
    lastName = StringField("last Name",[validators.Length(min=1, max=150),validators.DataRequired()])
    membership=RadioField("Membership",choices=[("F","Fellow"),("S","Senior"),("P","Professional")],default="F")
    gender = SelectField('Gender', [validators.DataRequired()],choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],default='')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateItemForm(Form):
    itemName=StringField("Item Name", [validators.Length(min=1, max=150),validators.DataRequired()])
    itemCategory=SelectField("Item Type",[validators.DataRequired()],choices=[('', 'Select'),("T","Top"),("B","Bottom")],default=" ")
    itemGender = SelectField('Item Gender', [validators.DataRequired()],choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],default='')
    itemSerial = TextAreaField('Item Serial', [validators.DataRequired()])
    itemCost = TextAreaField('Item Cost',[validators.DataRequired()])

class CreateStaffForm(Form):
    fname = StringField("First Name", [validators.DataRequired(), validators.Length(min=1, max=150)])
    lname = StringField("Last Name", [validators.DataRequired(), validators.Length(min=1, max=150)])
    gender = SelectField("Gender", [validators.DataRequired()], choices=[("", "Select"), ("F", "Female"), ("M", "Male")], default = "")
    hp = StringField("Contact Number", [validators.DataRequired()])
    # dob = DateField("Date of Birth", [validators.DataRequired()], format='%d-%m-%Y')
    # password =  PasswordField("Password", [validators.DataRequired()])
    address = TextAreaField("address", [validators.DataRequired()])
