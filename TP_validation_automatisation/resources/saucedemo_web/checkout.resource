*** Settings ***
Documentation    Keywords concernant la commande
Library    SeleniumLibrary

Resource    ../../resources/saucedemo_web/connexion.resource


*** Keywords ***
He Enters "${firstname}", "${lastname}", "${zipcode}" And Clicks On Continue Button
    [Documentation]    Remplissage du formulaire
    Input Text  id=first-name  ${firstname}
    Input Text  id=last-name  ${lastname}
    Input Text  id=postal-code  ${zipcode}
    Click Element  id=continue

Checkout Overview Appears
    [Documentation]    Vue d'ensemble de la commande et vérifications
    Wait Until Element Is Visible  id=finish

Item Total Price Is Correct
    [Documentation]    Vérification prix sous-total
    ${prix1_str}  Get Text  (//*[@class='inventory_item_price'][1])[1]
    ${prix2_str}  Get Text  (//*[@class='inventory_item_price'][1])[2]
    ${soustotal_str}  Get Text  //*[@class='summary_subtotal_label']
    ${prix1}  Convert To Number  ${prix1_str.replace('$','')}
    ${prix2}  Convert To Number  ${prix2_str.replace('$','')}
    ${soustotal}  Convert To Number  ${soustotal_str.replace('Item total: $','')}
    ${calculsoustotal}  Evaluate  ${prix1} + ${prix2}
    Should Be Equal As Numbers  ${calculsoustotal}  ${soustotal}

Total Price Is Correct
    [Documentation]    Vérification prix total
    ${taxe_str}  Get Text  //*[@class='summary_tax_label']
    ${total_str}  Get Text  //*[@class='summary_info_label summary_total_label']
    ${soustotal_str}  Get Text  //*[@class='summary_subtotal_label']
    ${taxe}  Convert To Number  ${taxe_str.replace('Tax: $','')}
    ${total}  Convert To Number  ${total_str.replace('Total: $','')}
    ${soustotal}  Convert To Number  ${soustotal_str.replace('Item total: $','')}
    ${calcultotal}  Evaluate  ${soustotal} + ${taxe}
    Should Be Equal As Numbers  ${calcultotal}  ${total}

He Clicks On Finish Button
    [Documentation]    Validation de la commande
    Click Element  id=finish

His Checkout Is Complete And He Can Go Back To HomePage
    [Documentation]    Vérification de la commande
    Wait Until Element Is Visible  id=back-to-products
    Element Text Should Be  //h2  Thank you for your order!
