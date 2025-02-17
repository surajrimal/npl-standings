from flask import Blueprint, render_template, redirect, url_for, request, flash, send_from_directory
from .models import Standing, db, ContactMessage
from .request import publishedArticles, publishedArticlesFive
import os
from . import cache
from hashlib import sha256
from flask import session

main = Blueprint('main', __name__)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = sha256(os.urandom(64)).hexdigest()
    return session['_csrf_token']

@main.route('/')
@cache.cached(timeout=60*60)
def home():
    standings = Standing.query.order_by(Standing.w.desc()).all()
    articles=publishedArticlesFive()
    #articles = list(zip(articles))[:5] 
    return render_template('home.html', standings=standings, articles=articles)

@main.route('/ads.txt')
def ads_txt():
    return send_from_directory('static', 'ads.txt')

@main.route('/termsofservice')
def terms_of_service():
    return render_template('termsofservice.html')

@main.route('/privacy')
def privacy_policy():
    return render_template('privacy.html')

@main.route('/recap2024')
def recap2024():
    standings = Standing.query.order_by(Standing.w.desc()).all()
    return render_template('recap2024.html', standings=standings)  # recap Page



@main.route('/news')
@cache.cached(timeout=60*60)
def news():
    print("Cache hit")
    articles = publishedArticles()
    return  render_template('news.html', articles = articles)


# Route for About Page
@main.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        csrf_token = request.form.get('_csrf_token')
        if csrf_token != session.get('_csrf_token'):
            flash('CSRF token missing or incorrect!', 'danger')
            return redirect(url_for('main.about'))
        
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        security_answer = request.form['security_question']

        # Simple spam prevention check
        if security_answer.strip() != '8':
            flash('Incorrect security answer. Please try again.', 'danger')
            return redirect(url_for('main.about'))

        # Save message to database
        new_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        flash('Your message has been submitted successfully!', 'success')
        return redirect(url_for('main.about'))
    
    csrf_token = generate_csrf_token()
    return render_template('about.html', csrf_token=csrf_token)