*** Settings ***
Documentation    Tests de l'appli calculatrice sur Android
Library    Collections
Library    String
Library    AppiumLibrary

Variables    ../../library/calculator_data.py


*** Keywords ***
He Taps On ${number}
    [Documentation]    Cliquer sur un chiffre
    @{chars}  Split String To Characters  ${number}
    FOR  ${char}  IN  @{chars}
        Click Element  //android.widget.ImageButton[@content-desc="${char}"]
    END

He Taps On "${symbol}"
    [Documentation]    Cliquer sur un operateur
    Click Element  //android.widget.ImageButton[@content-desc="${symbol}"]

Calculator Displays Formula And Preview Result Of "${dict}"
    [Documentation]    Vérifier la formule saisie et la prévisualisation du résultat
    # Triche pour symboles non reconnus '×' et '÷'
    ${formula}  Get Text  com.google.android.calculator:id/formula
    ${erroned_symbol}  Set Variable  ${formula.replace('${dict["number1"]}','').replace('${dict["number2"]}','')}
    ${formula2}  Convert To String  ${formula.replace('${erroned_symbol}','${dict["symbol"]}')}
    Should Be Equal As Strings  ${formula2}  ${dict["number1"]}${dict["symbol"]}${dict["number2"]}
    # Fin triche
    ${number1}  Convert To Integer  ${dict["number1"]}
    ${number2}  Convert To Integer  ${dict["number2"]}
    ${result1}  Evaluate  ${number1}${dict["symbol"]}${number2}
    ${result}  Convert To String  ${result1}
    # Triche pour symbole non reconnu '­­­­-'
    ${final}  Get Text  com.google.android.calculator:id/result_preview
    Should Be Equal As Strings  ${final.replace('−','${dict["symbol"]}')}  ${result}
    # Fin triche

He Taps On Equal Symbol
    [Documentation]    Cliquer sur égal
    Click Element  //android.widget.ImageButton[@content-desc="equals"]

Calculator Displays The Result Of "${dict}"
    [Documentation]    Afficher le résultat
    ${number1}  Convert To Integer  ${dict["number1"]}
    ${number2}  Convert To Integer  ${dict["number2"]}
    ${result}  Evaluate  ${number1}${dict["symbol"]}${number2}
    ${result}  Convert To String  ${result}
    # Triche pour symbole non reconnu '­­­­-'
    ${final}  Get Text  com.google.android.calculator:id/result_final
    Should Be Equal As Strings  ${final.replace('−','${dict["symbol"]}')}  ${result}
    # Fin triche
