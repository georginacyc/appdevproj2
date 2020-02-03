from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, DateField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import EqualTo
import datetime

class CreateUserForm(Form):
    firstName = StringField("First Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Lily"})
    lastName = StringField("Last Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Doe"})
    DOB = DateField("Date of Birth", [validators.DataRequired()], format='%d-%m-%Y', render_kw={"placeholder": "DD-MM-YYYY"})
    gender = SelectField('Gender', [validators.DataRequired()],choices=[("", "Select"),('M', 'Male'), ('F', 'Female')],default='')
    email= EmailField('Email', [validators.InputRequired()])
    pw = PasswordField("Password", [validators.InputRequired(), EqualTo('confirmpw', message="Passwords must match.")])
    confirmpw = PasswordField("Confirm Password")

class UpdateUserForm(Form):
    firstName = StringField("First Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Lily"})
    lastName = StringField("Last Name",[validators.Length(min=1, max=150),validators.DataRequired()],render_kw={"placeholder": "Doe"})
    gender = RadioField('Gender', [validators.DataRequired()],choices=[('M', 'Male'), ('F', 'Female')],default='')




class CreateStaffForm(Form):
    fname = StringField("First Name", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "John"})
    lname = StringField("Last Name", [validators.InputRequired(), validators.Length(min=1, max=150)], render_kw={"placeholder": "Doe"})
    gender = SelectField("Gender", [validators.DataRequired()], choices=[("", "Select"), ("F", "Female"), ("M", "Male")], default = "")
    hp = StringField("Contact Number", [validators.InputRequired()], render_kw={"placeholder": "65500999"})
    dob = DateField("Date of Birth", [validators.DataRequired()], format='%d/%m/%Y', render_kw={"placeholder": "DD/MM/YYYY"})
    password =  PasswordField("Password", [validators.InputRequired(), EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField("Confirm Password")
    address = TextAreaField("Address", [validators.InputRequired()])
    type = RadioField("Account Type", [validators.DataRequired()], choices=[("Staff","Staff"), ("Admin", "Admin")], default="Staff")

class UpdateStaffForm(Form):
    fname = StringField("First Name", [validators.Length(min=1, max=150)], render_kw={"placeholder": "John"})
    lname = StringField("Last Name", [validators.Length(min=1, max=150)], render_kw={"placeholder": "Doe"})
    gender = SelectField("Gender", choices=[("", "Select"), ("F", "Female"), ("M", "Male")], default = "")
    hp = StringField("Contact Number", render_kw={"placeholder": "65500999"})
    address = TextAreaField("Address")
    type = RadioField("Account Type", choices=[("Staff","Staff"), ("Admin", "Admin")], default="Staff")

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
    text = StringField("Inquiries",[validators.Length(min=1, max=500),validators.DataRequired()],render_kw={"placeholder": "Didn't receive order..."})
