from spamsub import app, db
from flask import request, flash, render_template, send_file
from models import *
from forms import SpammerForm
import utils


@app.route('/', methods=['GET', 'POST'])
def index():
    """ Index page """
    count = Address.query.count()
    latest = utils.sync_check()
    form = SpammerForm()
    # try to validate, and check for AJAX submission
    if form.validate_on_submit():
            if not utils.check_if_exists(form.address.data):
                flash(
                    u"We've added %s to the database." % form.address.data,
                    "text-success")
            else:
                flash(
                    u"We already know about %s, though." % form.address.data,
                    "text-success")
    if request.is_xhr:
        # OK to send back a fragment
        return render_template('form.jinja', form=form)
    # GET or no JS, so render a full page
    return render_template('index.jinja', form=form, count=count, latest=latest)

@app.route('/download', methods=['GET'])
def download():
    """ Download the latest version of spammers.txt """
    utils.update_db()
    return send_file(
        "git_dir/spammers.txt",
        as_attachment=True,
        attachment_filename="spammers.txt")
