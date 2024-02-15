
# Découverte Selenium sur temps personnel
""" programme pour signer automatiquement la feuille de présence, 
matin et après-midi durant la formation. Désormais non fonctionnel 
car données personnelles masquées et date actuelle non utilisable sur la feuille. """ 


from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime, time

# Définir une fonction qui retourne date du jour + matin ou après-midi :
# (+ formatage de la variable pour l'utiliser en css_selector)
def date_jour_css_format():

    info_jour = datetime.datetime.now()
    date = datetime.datetime.strftime(info_jour, "\\3%m\/%d\/%Y")
    heure = "am" if datetime.datetime.strftime(info_jour, "%H") < "13" else "pm"
    
    return date[:3] + " " + date[3:] + heure

def signature_auto(navigateur) :
    navigateur.maximize_window()
    navigateur.implicitly_wait(30)
    navigateur.get('https://sign.m2iformation.fr')

    # Cliquer sur "Espace stagiaire" :
    lien_1 = navigateur.find_element(By.CSS_SELECTOR, ".col-md-8 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h5:nth-child(1)")
    lien_1.click()
    time.sleep(1)

    # Remplir le champ "Email ou n° de télephone" avec l'identifiant :
    champ_1 = navigateur.find_element(By.CSS_SELECTOR, "#inputPhoneNumber")
    champ_1.send_keys("**********")

    # Remplir le champ "Code pin" :
    champ_2 = navigateur.find_element(By.CSS_SELECTOR, "#inputSmsCode")
    champ_2.send_keys("*****")

    # Cliquer sur le bouton "Se connecter" :
    bouton_1 = navigateur.find_element(By.CSS_SELECTOR, "#connexion")
    bouton_1.click()

    # Cliquer sur le lien "Feuille de présence" :
    lien_2 = navigateur.find_element(By.CSS_SELECTOR, ".main_nav > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
    #ActionChains(navigateur).move_to_element(lien_2).click(lien_2)
    lien_2.click()
    time.sleep(2)

    # Cliquer sur l'image "Emarger ici" correspondant à la date du jour :
    img_1 = navigateur.find_element(By.CSS_SELECTOR, f"#{date_jour_css_format()}")
    img_1.click()
    time.sleep(2)

    # Retour en haut de la page :
    lien_2 = navigateur.find_element(By.CSS_SELECTOR, ".main_nav > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
    lien_2.click()

    # Cliquer sur "Valider et se déconnecter" :
    lien_3 = navigateur.find_element(By.CSS_SELECTOR, ".login_button > a:nth-child(1)")
    lien_3.click()
    time.sleep(1)

    navigateur.quit()

if __name__ == "__main__" :
    signature_auto(webdriver.Chrome())

