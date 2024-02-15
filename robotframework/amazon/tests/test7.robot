*** Settings ***
Documentation    Premiers tests
Library    Collections
Library    SeleniumLibrary

Resource    ../ressources/homepage.resource
Resource    ../ressources/browser.resource
Resource    ../ressources/productpage.resource
Resource    ../ressources/header.resource
Resource    ../ressources/loginpage.resource

Variables    ../data/url.py
Variables    ../data/donnees.py

Test Setup    Run Keywords  Browser Init  url=${amazon}  browser=${browser}  AND  Accept Cookie
Test Teardown    Browser Close


*** Variables ***
${PRODUCT_SELECTOR}  id=productTitle
&{DICT}  id=${idproduct}  name=${livre1}
# ${LISTE_DICT}  [{"id": 2253934100,"name": "Tout le bleu du ciel"},
# ...    {"id": 2811229507,"name": "On se reverra"},
# ...    {"id": 2253174076,"name": "Le Joueur d'échecs"}]


*** Test Cases ***
Test 7 - Ajouter différents produits
    [Documentation]    Ajouter 2 produits au panier
    [Tags]    Panier  Produit

    Go To  ${amazon}/dp/${idproduct}
    Wait Until Element Is Visible    ${PRODUCT_SELECTOR}
    Add To Cart
    Go To  ${amazon}/dp/${idproduct2}
    Wait Until Element Is Visible    ${PRODUCT_SELECTOR}
    Add To Cart

Test 7bis - Ajouter différents produits - List
    [Documentation]    Ajouter 2 produits au panier
    [Tags]    Panier  Produit
    VAR  @{list}  ${idproduct}  ${idproduct2}

    Go To  ${amazon}/dp/${list[0]}
    Wait Until Element Is Visible    ${PRODUCT_SELECTOR}
    Add To Cart
    Go To  ${amazon}/dp/${list[1]}
    Wait Until Element Is Visible    ${PRODUCT_SELECTOR}
    Add To Cart

Test 7ter - Ajouter différents produits - Boucle FOR
    [Documentation]    Ajouter 2 produits au panier
    [Tags]    Panier  Produit
    VAR  @{list}  ${idproduct}  ${idproduct2}

    FOR  ${produit}  IN  @{list}
        Go To  ${amazon}/dp/${produit}
        Wait Until Element Is Visible    ${PRODUCT_SELECTOR}
        Add To Cart
    END

Test 8 - Vérifier la liste de produits
    [Documentation]    Ajouter 3 produits et vérifier la liste des produits
    [Tags]    Produit  Liste
    VAR  @{list_livre}  ${livre1}  ${livre2}  ${livre3}
    Search Products  Livres

    FOR  ${livres}  IN  @{list_livre}
        Wait Until Element Is Visible    //span[contains(., "${livres}")]
    END

Test 9 - Manipulation de liste
    [Documentation]    Vérifier liste
    [Tags]    Produit  Liste
    VAR  @{liste_10}  @{EMPTY}
    Search Products  Livres
    FOR  ${i}  IN RANGE  1  11
        ${titre}  Get Text   (//*[contains(@class, "s-card-container")]//span[contains(@class, "a-text-normal")])[${i}]
        Append To List  ${liste_10}  ${titre}
    END
    Length Should Be  ${liste_10}  10

Test 9bis - Manipulation de liste - Dictionnaire
    [Documentation]    Ajouter et vérifier produit avec dictionnaire
    [Tags]    Produit  Dictionnaire
    VAR  &{dict}  id=${idproduct}  name=${livre1}
    Go To  ${amazon}/dp/${dict["id"]}
    Add To Cart
    Go To Cart
    Element Text Should Be  //a[@rel="noopener"]//span[@class="a-truncate-cut"]  ${dict["name"]}

Test 10 - Optimisation du test 3
    [Documentation]    Connexion
    [Tags]    Identifiants  Connexion
    Connexion Optimisée  &{compte}

# Test HS - Liste de dictionnaire
#     [Documentation]    Liste de dictionnaire
#     &{D1}  Create Dictionary  id=${idproduct}  name=${livre1}
#     &{D2}  Create Dictionary  id=${idproduct2}  name=${livre2}
#     @{Liste}  Create List  ${D1}  ${D2}
#     ${list_product}  Evaluate  ${LISTE_DICT}

Test 11 - Les tableaux
    [Documentation]    Utilisation de tableau
    [Tags]    Panier  Dictionnaire
    VAR  @{liste_produit}  ${product1}  ${product2}  ${product3}

    FOR  ${dict}  IN  @{liste_produit}
        Go To  ${amazon}/dp/${dict['id']}
        Wait Until Element Is Visible    ${PRODUCT_SELECTOR}
        Add To Cart
    END
    Go To Cart
    FOR  ${dict}  IN  @{liste_produit}
        Wait Until Element Is Visible    //a[@rel="noopener"]//span[contains(., "${dict['name']}")]
    END

Test 12 - Les tableaux (suite)
    [Documentation]    Utilisation de tableau
    [Tags]    Panier  Dictionnaire
    VAR  @{liste_produit}  ${product1}  ${product4}
    FOR  ${produit}  IN  @{liste_produit}
        Search Products  ${produit['cat']}
        Element Should Be Visible  //*[contains(@class, "s-card-container")]//span[contains(., "${produit['name']}")]
    END
