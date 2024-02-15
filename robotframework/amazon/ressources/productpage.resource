*** Settings ***
Documentation    Keywords concernant les détails du produit
Library   String
Library   SeleniumLibrary


*** Keywords ***
Open Detailed Page
    [Documentation]    Ouvrir la page détaillée du produit
    [Arguments]    ${index}=1
    Click Element    (//div[contains(@class, "s-card-container")])[${index}]
    Wait Until Element Is Visible    id=productTitle  timeout=10

Add To Cart
    [Documentation]    Ajouter le produit au panier
    [Arguments]    ${qty}=1
    Select From List By Value  id=quantity  ${qty}
    Click Element  id=add-to-cart-button
    Wait Until Element Is Visible  id=sw-atc-details-single-container

Go To Cart
    [Documentation]    Aller dans le panier
    Wait Until Element Is Visible  id=sw-atc-details-single-container
    Click Element  id=nav-cart-text-container
    Wait Until Element Is Visible  //h1[contains(., "Votre panier")]

