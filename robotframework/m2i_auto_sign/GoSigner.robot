*** Settings ***
Documentation    Premiers tests
Library    SeleniumLibrary

Resource    ../ressources/browser.resource
Resource    ../m2i_auto_sign/connexion.resource
Resource    ../m2i_auto_sign/emargement.resource

Variables    ../m2i_auto_sign/url(m2i).py
Variables    ../m2i_auto_sign/identifiants.py
Variables    ../m2i_auto_sign/date_jour.py


*** Tasks ***
Signer Présence
    [Documentation]    Signer le calendrier de présence
    [Tags]    Emargement
    Browser Init    ${m2isign}  ${browser}
    Se Connecter    ${identifiant}  ${mdp}
    Ouvrir Calendrier
    Emarger    ${date_jour}
    Valider Et Quitter


*** Comments ***
Amélioration de mon programme de signature automatique
...    avec les techniques de robotframework.
Désormais non fonctionnel car données personnelles masquées
...    et date actuelle non utilisable sur la feuille.
