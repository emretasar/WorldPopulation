from datetime import datetime
from flask import render_template
from utils import connect, query
from settings import user, password, database

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


def population_page():
    cursor = connect(username=user, password=password, database=database)
    query_result = query(cursor)
    
    table_heading = ("Rank", "CCA3", "Country", "Capital", "Continent", "2022 Population", "2020 Population", "2015 Population", "2010 Population", "2000 Population", "1990 Population", "1980 Population", "1970 Population", "Area", "Density", "Growth Rate", "World Population Percentage")
    # table_heading = ("Country", "Capital", "Continent")
    
    return render_template("population.html", table_heading=table_heading, table_data=query_result)
