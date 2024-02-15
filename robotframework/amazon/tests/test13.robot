*** Settings ***
Documentation    Premiers tests
Library    Collections
Library    String
Library    SeleniumLibrary
Library    ../library/calcul.py

Resource    ../ressources/homepage.resource
Resource    ../ressources/browser.resource
Resource    ../ressources/loginpage.resource
Resource    ../ressources/productpage.resource

Variables    ../data/url.py
Variables    ../data/donnees.py

Test Teardown    Browser Close


*** Test Cases ***
Test 13 - Accept Cookies
    [Documentation]  Gérer les cookies
    Browser Init  url=${amazon}  browser=${browser}
    Manage Cookie  accept

Test 13bis - Refuse Cookies
    [Documentation]  Gérer les cookies
    Browser Init  url=${amazon}  browser=${browser}
    Manage Cookie  refuse

Test 13ter - Customize Cookies
    [Documentation]  Gérer les cookies
    Browser Init  url=${amazon}  browser=${browser}
    Manage Cookie  customize

Test 14 - Connexion Si Non Connecté
    [Documentation]  Gérer la connexion
    Browser Init  url=${amazon}  browser=${browser}
    Connexion Optimisée  &{compte}
    ${bool}  Run Keyword And Return Status  Element Should Contain   id=nav-link-accountList-nav-line-1  Identifiez-vous
    IF  ${bool}  Connexion Optimisée  &{compte}

Test Final
    [Documentation]  Ajouter le 1er bonbon de la liste et recommencer avec les suivant jusqu'à 50€ dans le panier
    Browser Init  url=${amazon}  browser=${browser}
    Manage Cookie  accept
    FOR  ${i}  IN RANGE  11
        Search Products  bonbon
        Open Detailed Page   ${i+1}
        Add To Cart
        Go To Cart
        ${prix}  Get Text  //*[@id="sc-subtotal-amount-buybox"]/span
        ${prix}  Convert To Number  ${prix.replace(' €', '').replace(',', '.')}
        IF  ${prix}>=50  BREAK
    END
    Click Element  id=sc-buy-box-ptc-button-announce

Bonus - Library Custom
    [Documentation]    Library custom exemple
    ${result}  Addition Nombre  15  10
    Log To Console  ${result}
