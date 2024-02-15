*** Settings ***
Documentation    Premiers tests
Library    SeleniumLibrary

Resource    ../ressources/homepage.resource
Resource    ../ressources/browser.resource
Resource    ../ressources/header.resource
Resource    ../ressources/loginpage.resource
Resource    ../ressources/productlist.resource
Resource    ../ressources/productpage.resource

Variables    ../data/url.py
Variables    ../data/donnees.py

Test Setup    Run Keywords  Browser Init  url=${amazon}  browser=${browser}  AND  Accept Cookie
Test Teardown    Browser Close


*** Test Cases ***
# Test 1 - Cookies
#     [Documentation]    Accepte les cookies
#     [Tags]    Cookies  Accueil
#     Accept Cookie

Test 2 - Search
    [Documentation]    Rechercher "${product}"
    [Tags]    BarreDeRecherche  AfficheResultats
    Search Products  ${product}

Test 3 - Connexion
    [Documentation]    Connexion
    [Tags]    Identifiants  Connexion
    Connexion  ${email}  ${mdp}  ${username}

Test 4 - Select category
    [Documentation]    Sélectionne une catégorie
    [Tags]    Categorie  Produit
    Select Category  ${category}
    Search Products  ${product}
    Element Should Be Visible  //option[text()="${category}" and @selected="selected"]

Test 5 - Trier la liste
    [Documentation]    Trier la liste de produits par prix décroissants
    [Tags]    Liste  Tri  Produit
    Search Products  ${product}
    Sorted Products  ${tri}
    Wait Until Element Is Visible  //option[contains(., "décroissant") and @selected]

Test 6 - Ajouter un produit au panier
    [Documentation]    Ajouter un produit et vérifier qu'il soit bien présent dans le panier
    [Tags]    Panier  Produit
    ${index}  Set Variable  7
    ${qty}  Set Variable  5
    Search Products  ${product}
    Open Detailed Page  ${index}
    ${nomLivre}  Get Text  id=productTitle
    Add To Cart  ${qty}
    Element Text Should Be  id=nav-cart-count  ${qty}
    Go To Cart
    Element Text Should Be  //a[@rel="noopener"]//span[@class="a-truncate-cut"]  ${nomLivre}

Test 6 bis - Ajouter un produit au panier - Version intégration
    [Documentation]    Ajouter un produit et vérifier qu'il soit bien présent dans le panier
    [Tags]    Panier  Produit
    Go To  ${amazon}/dp/${idproduct}
    Add To Cart  ${qty}
    Element Text Should Be  id=nav-cart-count  ${qty}
    Go To Cart
    Element Text Should Be  //a[@rel="noopener"]//span[@class="a-truncate-cut"]  ${livre1}


*** Keywords ***
Calculate Cart
    [Documentation]  Calcul l'incrémentation du panier
    [Arguments]  ${qty}
    ${nb}  Get Text  id=nav-cart-count
    ${nb}  Convert To Integer  ${nb}
    ${result}  Evaluate  ${nb} + ${qty}
    ${result}  Convert To String  ${result}
    RETURN  ${result}
