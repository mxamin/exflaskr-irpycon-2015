from flask import render_template, flash

from . import main
from .forms import EntryForm
from app import db
from app.models import Entry


@main.route('/', methods=['GET', 'POST'])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(title=form.title.data,
                      text=form.text.data)
        db.session.add(entry)
        db.session.commit()
        flash('Entry added successfully.')

        # clear form
        form.title.data = None
        form.text.data = None

    entries = Entry.query.all()
    return render_template('index.html', form=form, entries=entries)
