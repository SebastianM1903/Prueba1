from flask import Flask, render_template, url_for, request, redirect, session, flash
import cx_Oracle
app = Flask(__name__)


def inicio():
    return "Hola mundoOOOOOOO"
inicio()