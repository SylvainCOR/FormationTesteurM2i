*** Settings ***
Documentation    Keywords concernant le header
Library   SeleniumLibrary


*** Keywords ***
Search Products
    [Documentation]    Rechercher de produits
    [Arguments]    ${produit}
    Click Element  locator=id=twotabsearchtextbox
    Input Text  locator=id=twotabsearchtextbox  text=${produit}  clear=True
    Click Element  locator=id=nav-search-submit-button
    Element Should Be Visible  locator=//*[contains(@class, "s-result-list")]

Goto Login/Account Page
    [Documentation]    Page login/votre compte
    Element Should Be Visible  locator=id=nav-link-accountList-nav-line-1
    Click Element  locator=id=nav-link-accountList-nav-line-1
    Wait Until Element Is Visible  id=ap_email

Select Category
    [Documentation]    Sélectionne une catégorie
    [Arguments]    ${category}
    Select From List By Label  id=searchDropdownBox  ${category}
