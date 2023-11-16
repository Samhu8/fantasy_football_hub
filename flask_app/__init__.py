from flask import Flask
from flask import render_template, redirect, request, session,flash
app = Flask(__name__)
app.secret_key = "coder123"