from wtforms import Form, StringField, SelectField, validators, ValidationError, FloatField, TextAreaField,RadioField


def serialcheck(form,field):
    if len(field.data) == 10:
        if field.data[-2] == 'T' or field.data[-2] == 'B':
            if field.data[-1] == 'M' or field.data[-1] == 'F':
                return field.data
            else:
                raise ValidationError('Last character must be Item Gender (M/F) ')
        else:
            raise ValidationError('2nd last character must be Item Category (T/B)')
    else:
        raise ValidationError('Item Serial must be 10 characters - 8 digits + Item Category + Gender')


class CreateItemForm(Form):
    itemName = StringField("Item Name",[validators.Length(min=1, max=150),validators.DataRequired()])
    itemSerial = StringField("Item Serial",[validators.DataRequired(),serialcheck])
    itemCategory = RadioField("Category",[validators.DataRequired()],choices=[('Tops', 'Tops'), ('Bottoms', 'Bottoms')])
    itemGender = RadioField("Gender", [validators.DataRequired()],choices=[('F', 'Female'), ('M', 'Male')])
    itemCost = FloatField("Item Cost",[validators.DataRequired()])
    itemPrice = FloatField("Item Price",[validators.DataRequired()])
    itemDescription = TextAreaField("Item Description",[validators.DataRequired()])
    itemQuantity = 0

