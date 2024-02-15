*** Settings ***
Documentation    Keywords concernant la page de connexion
Library    SeleniumLibrary

Variables    ../../library/saucedemo_data.py


*** Keywords ***
User Is On Swag Labs Connexion Page
    [Documentation]    Verification page de connexion
    Wait Until Element Is Visible  id=user-name

He Enters "${username}" In Username Field
    [Documentation]    Entrer le nom d'utilisateur
    Input Text  id=user-name  ${username}

He Enters "${password}" In Password Field
    [Documentation]    Entrer le mot de passe
    Input Text  id=password  ${password}

Fields Are Not Empty
    [Documentation]    Verification des champs (non vides)
    Element Text Should Not Be  id=user-name  ${None}
    Element Text Should Not Be  id=password  ${None}

He Clicks On Login Button
    [Documentation]    Cliquer sur le bouton de connexion
    Click Element  id=login-button

User Is Connected And WebPage Has Changed
    [Documentation]    Verification de connexion
    Wait Until Element Is Visible  id=react-burger-menu-btn

Locked Out Error Message Appears
    [Documentation]    Verification message d'erreur
    Wait Until Element Is Visible  //h3
    Element Text Should Be  //h3  expected=Epic sadface: Sorry, this user has been locked out.
