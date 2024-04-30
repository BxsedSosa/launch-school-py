"""
5. The python doc for the datetime module provides two attributes to retriee the year from a date or datetime object: year and isocalendar

What is the difference between the year attribute and the isocalendar method?
"""

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

print(today_year)
print(iso_year)

"""
isocalendar
------------
Returns a named tuple object   

Year method
------------
returns between MINYEAR and MAXYEAR inclusive
"""
