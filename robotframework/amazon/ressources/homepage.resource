*** Settings ***
Documentation    Keywords concernant la page d'accueil
Library   SeleniumLibrary


*** Keywords ***
Accept Cookie
    [Documentation]  Accepter les cookies
    Wait Until Element Is Visible  id=sp-cc-accept
    Click Element  id=sp-cc-accept
    Sleep  1
    Wait Until Element Is Not Visible  id=sp-cc-accept

Manage Cookie
    [Documentation]  Gérer les cookies
    ...  button : doit contenir 'accept' | 'refuse' | 'customize'
    [Arguments]  ${button}=accept
    Wait Until Element Is Visible  id=sp-cc-accept
    IF  '${button}' == 'accept'
        Click Element  id=sp-cc-accept
    ELSE IF  '${button}' == 'refuse'
        Click Element  id=sp-cc-rejectall-link
    ELSE
        Click Element  id=sp-cc-customize
    END
    Wait Until Element Is Not Visible  id=sp-cc-accept
