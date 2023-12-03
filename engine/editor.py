from flask import Blueprint, render_template, request, redirect, jsonify
# import dataengine
from helpers import checkpoint
import os, runpy
from settings import cms_version

THEMES = "templates/SYSTEM/"
THEMES_STAT = "static/SYSTEM/"
THEME_DATA = "theme.py"
VERIFIED_THEMES,TO_VERIFY = [],{}

editor = Blueprint("editor", __name__)

def verify_theme(theme,theme_pack):
    try:
        if float(cms_version) < float(theme_pack[theme][1]):
            print("wrong vers")
    except:
        pass

def get_templates():
    for theme_ in os.listdir(THEMES):
        theme_fold = THEMES+theme_
        if os.path.isdir(theme_fold):
            theme_fold_in = runpy.run_path(theme_fold+"/"+THEME_DATA)
            try:
                t_data = {theme_:[theme_fold_in['linecms_name'],theme_fold_in['linecms_compat'],theme_fold_in['linecms_info'],theme_fold]}
                verify_theme(theme_,t_data)
            except:
                pass # not a template file

def get_robotssitemap():
    pass

@editor.route("/edit",methods=['GET','POST'])
@checkpoint.onlylogged
def codeedit():
    items = {}
    get_templates()

    return render_template("/dashboard/editor.html")
