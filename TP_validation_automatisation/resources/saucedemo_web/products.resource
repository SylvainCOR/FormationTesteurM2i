*** Settings ***
Documentation    Keywords concernant les produits
Library    Collections
Library    SeleniumLibrary


*** Keywords ***
He Clicks On Product Sort Container To Select Price High To Low
    [Documentation]    Trier les produits par prix décroissants
    Select From List By Value  //*[@id='header_container']//*[@class='product_sort_container']  hilo

The Most Expensive Item Is In First Position
    [Documentation]    Vérifier le premier produit est le plus cher
    @{liste_prix}    Create List
    ${total_element}  Get Element Count  //*[@class='inventory_item']
    FOR  ${i}  IN RANGE  ${total_element}
        ${prix}  Get Text  //div[@class='inventory_item'][${i+1}]//div[@class='inventory_item_price']
        Append To List  ${liste_prix}  ${prix.replace('$','')}
    END
    ${lenght}  Get Length  ${liste_prix}
    FOR  ${index}  IN RANGE  ${lenght-1}
        Should Be True  ${liste_prix}[${index}] >= ${liste_prix}[${index+1}]
    END

He Adds Product Number "${product_position}" To The Cart
    [Documentation]    Ajouter un produit au panier
    Click Button  //div[@class='inventory_item'][${product_position}]//button

Button Of Product "${product_position}" Add To Cart Become Remove Button
    [Documentation]    Vérifier le produit sélectionné
    Element Text Should Be  //div[@class='inventory_item'][${product_position}]//button  expected=Remove
