from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ChooseCount(FlaskForm):
    count_of_player = SelectField(
        'Выберите количество игроков',
        coerce=int,
        choices=[1, 2, 3, 4],
        render_kw={'class': 'form-select',
                   'aria-label': "Default select example"}
    )
    name1 = StringField("Имя 1-ого игрока: ", validators=[DataRequired(), Length(max=15)], default="Player_1")
    name2 = StringField("Имя 2-ого игрока: ", validators=[DataRequired(), Length(max=15)], default="Player_2")
    name3 = StringField("Имя 3-ого игрока: ", validators=[DataRequired(), Length(max=15)], default="Player_3")
    name4 = StringField("Имя 4-ого игрока: ", validators=[DataRequired(), Length(max=15)], default="Player_4")
    submit = SubmitField("Начать игру", render_kw={'class': "btn btn-primary"})


class Review(FlaskForm):
    name = StringField("Ваше имя: ", validators=[DataRequired(), Length(max=32)],
                       render_kw={'class': "form-control"})
    browser = SelectField(
        'Выберите ваш браузер',
        choices=["Google Chrome", "Mozilla Firefox", "Opera", "Safari", "Microsoft Edge", "Другой"],
        render_kw={'class': 'form-select',
                   'aria-label': "Default select example"}
    )
    message = TextAreaField("Напишите отзыв здесь: ", validators=[DataRequired()], render_kw={'class': "form-control"})
    email = StringField("Email: ", validators=[Email()], render_kw={'class': "form-control"})
    radio = RadioField('Ваш рейтинг', choices=[0, 1, 2, 3, 4, 5], default=0)
    submit = SubmitField("Оставить отзыв", render_kw={'class': "btn btn-primary"})


