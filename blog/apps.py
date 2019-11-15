from django.apps import AppConfig
import os
import sys
from flask import Flask, render_template, request, jsonify
import plaid
class BlogConfig(AppConfig):
    name = 'blog'

