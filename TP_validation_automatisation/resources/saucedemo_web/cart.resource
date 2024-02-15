*** Settings ***
Documentation    Keywords concernant les produits
Library    SeleniumLibrary


*** Keywords ***
He Clicks On The Cart Icon In The Header
    [Documentation]    Aller au panier
    Click Element  id=shopping_cart_container

Page Change To Cart Containing "${nb_produits}"
    [Documentation]    Vérifier panier et nombre produits
    Element Text Should Be  //*[@class='title']  Your Cart
    Element Text Should Be  //*[@id='shopping_cart_container']//span  ${nb_produits}

He Clicks On Checkout Button
    [Documentation]    Cliquer sur le bouton de commande
    Click Element  id=checkout

Page Change To A Form
    [Documentation]    Vérifier l'apparition du formulaire
    Wait Until Element Is Visible  id=first-name
