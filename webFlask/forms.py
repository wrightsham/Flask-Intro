from flask_wtf import FlaskForm
from webFlask import app
from wtforms import StringField, DateField, SubmitField, RadioField, SelectField


class BestSellersForm(FlaskForm):
    category = RadioField('Select a Category:',
                          choices=[('combined-print-and-e-book-fiction', '----  Fiction Books  ----'),
                                   ('combined-print-and-e-book-nonfiction', '- Non-fiction Books -'),
                                   ('young-adult-hardcover', '- Young Adult Books -')],
                          default='combined-print-and-e-book-fiction')
    timeFrame = DateField('Select a date (must be YYYY/MM/DD):', format='%Y/%m/%d')
    submit = SubmitField("Submit")


class BookReviewsForm(FlaskForm):
    bookTitle = SelectField('Select a Book:',
                            choices=[('big+little+lies', 'Big Little Lies by Liane Moriarty'),
                                     ('eclipse&author=Stephenie%20Meyer', 'Eclipse by Stephanie Mayer'),
                                     ('to+kill+a+mockingbird', 'To Kill a Mockingbird'),
                                     ('the+stars+beneath+our+feet', 'The Stars Beneath Our Feet'),
                                     ('all+the+light+we+cannot+see', 'All the Light We Cannot See')])
    submit = SubmitField("Submit")
