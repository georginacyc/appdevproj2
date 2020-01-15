from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, DateField, PasswordField
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
    fname = StringField("First Name", [validators.DataRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "John"})
    lname = StringField("Last Name", [validators.DataRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "Doe"})
    gender = SelectField("Gender", [validators.DataRequired()], choices=[("", "Select"), ("F", "Female"), ("M", "Male")], default = "")
    hp = StringField("Contact Number", [validators.DataRequired()], render_kw={"placeholder": "65500999"})
    dob = DateField("Date of Birth", [validators.DataRequired()], format='%d-%m-%Y', render_kw={"placeholder": "12-03-2001"})
    password =  PasswordField("Password", [validators.DataRequired()])
    # password =  PasswordField("Password", [validators.DataRequired(), EqualTo('confirm', message='Passwords must match')])
    # confirm = PasswordField("Confirm Password")
    address = TextAreaField("Address", [validators.DataRequired()])

class LogInForm(Form):
    # email = Email("Email", [validators.InputRequired()], render_kw={"placeholder": "johndoe@domain.com"})
    password = PasswordField("Password", [validators.InputRequired()], render_kw={"placeholder": "password"})

