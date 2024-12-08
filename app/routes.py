from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import Standing, db

import os

main = Blueprint('main', __name__)

@main.route('/')
def home():
    standings = Standing.query.order_by(Standing.w.desc()).all()
    return render_template('home.html', standings=standings)



@main.route('/termsofservice')
def terms_of_service():
    return render_template('termsofservice.html')

@main.route('/privacy')
def privacy_policy():
    return render_template('privacy.html')

@main.route('/about')
def about():
    return render_template('about.html')  # About Page
