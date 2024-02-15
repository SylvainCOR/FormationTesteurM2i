import datetime

info_jour = datetime.datetime.now()
date = datetime.datetime.strftime(info_jour, "%m/%d/%Y")
heure = "am" if datetime.datetime.strftime(info_jour, "%H") < "13" else "pm"

date_jour = date[:3] + date[3:] + heure

