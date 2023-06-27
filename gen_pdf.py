#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:46:39 2023

@author: nass
"""

import jinja2
import pdfkit
from datetime import datetime


def gen_pdf():
    my_name = "Franck AndradeEDFDZHEVC"
    item1 = "TV"
    item2="Couch"
    item3 = "Washing Machine"
    today_date = datetime.today().strftime("%d %b, %Y")
    
    context = {'my_name' : my_name, 'item1': item1, 'item2': item2, 'item3': item3, 'today_date' : today_date}
    
    template_loader = jinja2.FileSystemLoader('/Users/nass/Documents/Streamlit-app/')
    template_env = jinja2.Environment(loader = template_loader)
    
    
    template = template_env.get_template("basic_template.html")
    output_text = template.render(context)
    
    config = pdfkit.configuration(wkhtmltopdf = "/usr/local/bin/wkhtmltopdf")
    pdf = pdfkit.from_string(output_text, 'pdf_generated.pdf', configuration = config)
    