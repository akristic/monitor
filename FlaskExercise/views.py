from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log=="info": app.logger.info('%s logged value', log)
    if log=="warning": app.logger.warning('%s logged value', log)
    if log=="error": app.logger.error('%s logged value', log)
    if log=="critical": app.logger.critical('%s logged value', log)

    return render_template(
        'index.html',
        log=log
    )
