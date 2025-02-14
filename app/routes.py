from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import Standing, db
from .request import publishedArticles, publishedArticlesFive
import os
from . import cache

main = Blueprint('main', __name__)

@main.route('/')
@cache.cached(timeout=60*60)
def home():
    standings = Standing.query.order_by(Standing.w.desc()).all()
    articles=publishedArticlesFive()
    #articles = list(zip(articles))[:5] 
    return render_template('home.html', standings=standings, articles=articles)


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


@main.route('/about')
def about():
    standings = Standing.query.order_by(Standing.w.desc()).all()
    return render_template('about.html', standings=standings)  # About Page

@main.route('/news')
@cache.cached(timeout=60*60)
def news():
    print("Cache hit")
    articles = publishedArticles()
    return  render_template('news.html', articles = articles)
