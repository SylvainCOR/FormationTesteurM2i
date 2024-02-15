import datetime

def date_jour_css_format():
    
    info_jour = datetime.datetime.now()
    date = datetime.datetime.strftime(info_jour, "\\3%m\/%d\/%Y")
    heure = "am" if datetime.datetime.strftime(info_jour, "%H") < "13" else "pm"
    
    return date[:3] + " " + date[3:] + heure

print(date_jour_css_format())

