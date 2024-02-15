*** Settings ***
Documentation    Keywords concernant la liste de résultats
Library   SeleniumLibrary


*** Keywords ***
Sorted Products
    [Documentation]    Trier la liste par orde décroissant
    [Arguments]    ${tri}
    Select From List By Label  s-result-sort-select  ${tri}
    