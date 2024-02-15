package serenity.StepsDefinitions;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import net.serenitybdd.core.pages.PageObject;
import net.serenitybdd.core.pages.WebElementFacade;
import net.serenitybdd.screenplay.actions.ScrollToWebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.support.FindBy;

import java.util.List;
import java.util.Random;

public class personalities extends PageObject {

    //----------SCENARIO_1---------------------------------------
    //----------SELECTEURS---------------------------------------

    @FindBy(css = "#main-app > main > div.hero > div > a")
    WebElementFacade button_passer_test;
    @FindBy(css = "#test-app header h1")
    WebElementFacade titre_page_test;
    @FindBy(css = "fieldset")
    List<WebElementFacade> list_question;
    By var = By.cssSelector("span.sp-radio");
    @FindBy(css = "button.sp-button")
    WebElementFacade btn_suivant;
    @FindBy(xpath = "//span[text()='Résutats']")
    WebElementFacade btn_result;
    @FindBy(css = "div.card__text div.results__intro")
    WebElementFacade type_perso;

    //----------FONCTIONS---------------------------------------

    @Given("le client se connecte sur le site {string}")
    public void leClientSeConnecteSurLeSite(String url) {
        openAt(url);
    }
    @When("il clique sur le bouton Passer le test")
    public void ilCliqueSurLeBoutonPasserLeTest() {
        clickOn(waitFor(button_passer_test));
    }
    @Then("il est dirige sur la page du test")
    public void ilEstDirigeSurLaPageDuTest() {
        waitFor(titre_page_test);
    }
    @When("il repond aux questions de facon aleatoire en commencant par la question {int}")
    public void ilRepondAuxQuestionsDeFaconAleatoireEnCommencantParLaQuestion(int numQ) {
        while (!btn_result.isCurrentlyVisible() && numQ <= 6) {
            Random rand = new Random();
            int i = rand.nextInt(6 + 1);
            list_question.get(numQ - 1).thenFindAll(var).get(i).click();
            numQ++;
        }
    }
    @Then("le bouton suivant s'affiche")
    public void leBoutonSuivantSAffiche() {
        waitFor(btn_suivant);
    }
    @When("il clique sur le bouton suivant")
    public void ilCliqueSurLeBoutonSuivant() {
        clickOn(btn_suivant);
        while(!type_perso.isVisible()){
            ilRepondAuxQuestionsDeFaconAleatoireEnCommencantParLaQuestion(1);
            clickOn(btn_suivant);
        }
    }
    @Then("la page resultat s'affiche")
    public void laPageResultatSAffiche() {
        shouldBeVisible(type_perso);
    }


    //----------SCENARIO_2---------------------------------------
    //----------SELECTEURS---------------------------------------

    @FindBy(linkText="Types de personnalité")
    WebElementFacade ongletTypes;
    @FindBy(css=".hero h1")
    WebElementFacade titreType;
    @FindBy(css = ".type-info h1 span")
    WebElementFacade titreLogicien;

    //----------FONCTIONS---------------------------------------

    @When("il clique sur l'onglet types de personnalite qui se situe au milieu de la topbar")
    public void ilCliqueSurLOngletTypesDePersonnaliteQuiSeSitueAuMilieuDeLaTopbar() {
        waitABit(500);
        clickOn(ongletTypes);
    }
    @Then("la page types de personnalite s'affiche")
    public void laPageTypesDePersonnaliteSAffiche() {
        waitABit(500);
        waitFor(titreType);
    }
    @When("scroller pour afficher le {string} de personalite")
    public void scrollerPourAfficherLeTypeDePersonalite(String type) {
        waitABit(500);
        String personalite = "//h4[text()='"+type+"']" ;
        WebElementFacade typePerso = $(personalite) ;
        new ScrollToWebElement(typePerso);
    }
    @And("cliquer sur le {string} de personalite")
    public void cliquerSurLeDePersonalite(String type) {
        waitABit(500);
        String personalite = "//h4[text()='"+type+"']" ;
        WebElementFacade typePerso = $(personalite) ;
        clickOn(typePerso);
    }
    @Then("la page du type s'affiche")
    public void laPageDuTypeSAffiche() {
        waitABit(500);
        waitFor(titreLogicien);
    }


    //----------SCENARIO_3---------------------------------------
    //----------SELECTEURS---------------------------------------

    @FindBy(linkText="Contact")
    WebElementFacade ongletcontact;

    @FindBy(css=".caption > h1:nth-child(1)")
    WebElementFacade titre_contact;

    @FindBy(xpath="//a[@class='icon twitter']")
    WebElementFacade logo_TT;

    @FindBy(css="svg.r-16y2uox > g:nth-child(1) > path:nth-child(1)")
    WebElementFacade logo_X;

    //----------FONCTIONS---------------------------------------

    @When("il clique sur l'onglet contact qui se situe sur la topbar")
    public void ilCliqueSurLOngletContactQuiSeSitueSurLaTopbar() {
        waitABit(500);
        clickOn(ongletcontact);
    }
    @Then("la page contactez-nous s'affiche")
    public void laPageContactezNousSAffiche() {
        waitABit(500);
        titre_contact.isCurrentlyVisible();
    }
    @When("il clique sur le logo twitter en bas a gauche")
    public void ilCliqueSurLeLogoTwitterEnBasAGauche() {
        waitABit(500);
        clickOn(logo_TT);
    }
    @Then("la page 16 personalities de X s'affiche")
    public void laPagePersonalitiesDeXSAffiche() {
        waitABit(500);
        logo_X.isCurrentlyVisible();
    }
}
