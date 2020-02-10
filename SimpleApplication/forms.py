from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, DateField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import EqualTo
import datetime

class CreateUserForm(Form):
    firstName = StringField("First Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Lily"})
    lastName = StringField("Last Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Doe"})
    DOB = DateField("Date of Birth", [validators.DataRequired()], format='%d-%m-%Y', render_kw={"placeholder": "DD-MM-YYYY"})
    gender = RadioField('Gender', [validators.InputRequired()],choices=[('M', 'Male'), ('F', 'Female'),('O', 'Others')],default='')
    email= EmailField('Email', [validators.InputRequired()])
    pw = PasswordField("Password", [validators.InputRequired(), EqualTo('confirmpw', message="Passwords must match.")])
    confirmpw = PasswordField("Confirm Password")

class UpdateUserForm(Form):
    firstName = StringField("First Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Lily"})
    lastName = StringField("Last Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Doe"})
    gender = RadioField('Gender', [validators.DataRequired()],choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')],default='')
    email= EmailField('Email', [validators.InputRequired()])


class CreateStaffForm(Form):
    fname = StringField("First Name", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "John"})
    lname = StringField("Last Name", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "Doe"})
    gender = RadioField("Gender", [validators.DataRequired()], choices=[("Female", "Female"), ("Male", "Male")], default = "")
    hp = StringField("Contact Number", [validators.InputRequired()], render_kw={"placeholder": "65500999"})
    dob = DateField("Date of Birth", [validators.DataRequired()], format='%d/%m/%Y', render_kw={"placeholder": "DD/MM/YYYY"})
    password =  PasswordField("Password", [validators.InputRequired(), EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField("Confirm Password")
    address = TextAreaField("Address", [validators.InputRequired()])
    type = RadioField("Account Type", [validators.DataRequired()], choices=[("Staff","Staff"), ("Admin", "Admin")], default="Staff")

class UpdateStaffForm(Form):
    fname = StringField("First Name", [validators.Length(min=1, max=150)], render_kw={"placeholder": "John"})
    lname = StringField("Last Name", [validators.Length(min=1, max=150)], render_kw={"placeholder": "Doe"})
    gender = StringField("Gender", render_kw={'readonly': True})
    hp = StringField("Contact Number", render_kw={"placeholder": "65500999"})
    dob = DateField("Date of Birth", format='%d/%m/%Y', render_kw={'readonly': True})
    address = TextAreaField("Address")
    type = RadioField("Account Type", choices=[("Staff","Staff"), ("Admin", "Admin")], default="Staff")
    resetpass = BooleanField("Reset Password")

class ShowDetailsForm(Form):
    name = StringField("Name", [validators.Length(min=1, max=150)], render_kw={'readonly': True})
    type = StringField("Account Type", render_kw={'readonly': True})
    gender = StringField("Gender", render_kw={'readonly': True})
    dob = DateField("Date of Birth", format='%d/%m/%Y', render_kw={'readonly': True})
    hp = StringField("Contact Number", render_kw={'readonly': True})
    address = TextAreaField("Address", render_kw={'readonly': True})
    oldpass = PasswordField("Current Password", [validators.InputRequired()])
    newpass =  PasswordField("New Password", [validators.InputRequired(), EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField("Confirm New Password")

class LogInForm(Form):
    email = EmailField("Email", [validators.InputRequired()], render_kw={"placeholder": "johndoe@domain.com"})
    password = PasswordField("Password", [validators.InputRequired()], render_kw={"placeholder": "password"})

class CreateAnnouncement(Form):
    date = DateField("Date", [validators.DataRequired()], format='%d/%m/%Y', default=datetime.date.today, render_kw={'readonly': True})
    title = StringField("Title", [validators.DataRequired(), validators.Length(min=1, max=150)])
    description = TextAreaField("Description (Optional)", default="")

class ContactUsForm(Form):
    fname = StringField("First Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Lily"})
    lname = StringField("Last Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Doe"})
    email= EmailField('Email', [validators.InputRequired()])
    text = TextAreaField("Inquiries",[validators.Length(min=1, max=500),validators.DataRequired()],render_kw={"placeholder": "Didn't receive order..."})

class PaymentForm(Form):
    name = StringField("Name",[validators.Length(min=1, max=150),validators.DataRequired()])
    cardno= StringField('Card Number', [validators.InputRequired(), validators.Length(min=16, max=16)],render_kw={"placeholder": "0000 0000 0000 0000"})
    date = StringField("Valid Thru",[validators.Length(min=5, max=5),validators.DataRequired()],render_kw={"placeholder": "MM/YY"})
    cvv = StringField("CVV / CVC *",[validators.Length(min=3, max=3),validators.DataRequired()])

class ShippingForm(Form):
    fname = StringField("First Name", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "John"})
    lname = StringField("Last Name", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "Doe"})
    email= EmailField('Email', [validators.InputRequired()])
    hp = StringField("Contact Number", [validators.InputRequired()], render_kw={"placeholder": "65500999"})
    address = StringField("Address 1", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "1 Ang Mo Kio Ave"})
    address2 = TextAreaField("Address 2(Optional)", default="")
    postal = StringField("Postal Code", [validators.InputRequired()], render_kw={"placeholder": "544915"})

class createtestdataForm(Form):
    saleDate = DateField("Order Date ( d-m-Y )", format='%d-%m-%Y')
    saleAmt = StringField("Sale Amt")

class CreateAboutUsForm(Form):
    aboutUsName = StringField("Name", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "John"})
    aboutUsRole = StringField("Role", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "CEO"})


