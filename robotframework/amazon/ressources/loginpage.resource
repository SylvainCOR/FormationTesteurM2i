*** Settings ***
Documentation    Keywords concernant la connexion
Library   SeleniumLibrary

Resource    ../ressources/header.resource
Variables    ../data/account.py


*** Keywords ***
Connexion
    [Documentation]    Se connecter
    [Arguments]    ${email}  ${mdp}  ${username}
    ${IDemail}  Set Variable  id=ap_email
    ${IDpassword}  Set Variable  id=ap_password
    Goto Login/Account Page
    Wait Until Element Is Visible  locator=${IDemail}
    Input Text  locator=${IDemail}  text=${email}
    Click Element  locator=id=continue
    Wait Until Element Is Visible  locator=${IDpassword}
    Input Text  locator=${IDpassword}  text=${mdp}
    Click Element  locator=id=signInSubmit
    Wait Until Element Contains  locator=id=glow-ingress-line1  text=Livrer à ${username}

Connexion Optimisée
    [Documentation]    Se connecter optimisé
    [Arguments]    &{compte}
    Goto Login/Account Page
    Input Text  id=ap_email  ${compte['email']}
    Click Element  id=continue
    Input Text  id=ap_password  ${compte['mdp']}
    Click Element  id=signInSubmit
    Wait Until Element Contains  id=glow-ingress-line1  Livrer à ${compte['username']}
