package Junitcucumber.StepsDefinitions;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.openqa.selenium.By;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

import static Junitcucumber.StepsDefinitions.Hooks.driver;

public class m2i_sign_stepdefs {
    @Given("J'ouvre le site {string}")
    public void jOuvreLeSite(String url) {
        driver.get(url);
    }
    @When("Je clique sur Espace stagiaire")
    public void jeCliqueSurEspaceStagiaire() {
        driver.findElement(By.cssSelector(".col-md-8 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h5:nth-child(1)")).click();
    }
    @Then("Le formulaire de connexion s'ouvre")
    public void LeFormulaireDeConnexionSOuvre() {
        Assert.assertFalse(driver.findElements(By.cssSelector(".col-md-8 > div:nth-child(1) > div:nth-child(1) > h5:nth-child(2)")).isEmpty());
    }
    @When("Je clique sur le champ Email ou n° de téléphone")
    public void jeCliqueSurLeChampEmailOuNDeTéléphone() {
        driver.findElement(By.cssSelector("#inputPhoneNumber")).click();
    }
    @And("J'indique mon numéro de télephonne comme identifiant {string}")
    public void jIndiqueMonNuméroDeTélephonneCommeIdentifiant(String login) {
        driver.findElement(By.cssSelector("#inputPhoneNumber")).sendKeys(login);
    }
    @Then("Mon numéro de téléphone apparait dans le champ et est aligné à gauche")
    public void monNuméroDeTéléphoneApparaitDansLeChampEtEstAlignéÀGauche() {
        Assert.assertFalse(driver.findElements(By.cssSelector("#inputPhoneNumber")).isEmpty());
    }
    @When("Je clique sur le champ Code pin")
    public void jeCliqueSurLeChampCodePin() {
        driver.findElement(By.cssSelector("#inputSmsCode")).click();
    }
    @And("J'indique mon code comme mot de passe {string}")
    public void jInidiqueMonCodeCommeMotDePasse(String mdp) {
        driver.findElement(By.cssSelector("#inputSmsCode")).sendKeys(mdp);
    }
    @Then("Mon code apparait dans le champ et est aligné à gauche")
    public void monCodeApparaitDansLeChampEtEstAlignéÀGauche() {
        Assert.assertFalse(driver.findElements(By.cssSelector("#inputSmsCode")).isEmpty());
    }
    @When("Je clique sur le bouton Se connecter")
    public void jeCliqueSurLeBouton() throws InterruptedException {
        driver.findElement(By.cssSelector("#connexion")).click();
        TimeUnit.SECONDS.sleep(2);
    }
    @Then("Je suis connecté à mon espace personnel")
    public void jeSuisConnectéÀMonEspacePersonnel() {
        Assert.assertFalse(driver.findElements(By.cssSelector("#modifier")).isEmpty());
    }


    @Given("Je suis connecté à mon espace personnel {string} {string} {string}")
    public void jeSuisConnectéÀMonEspacePersonnel(String url, String login, String mdp) throws InterruptedException {
        jOuvreLeSite(url);
        jeCliqueSurEspaceStagiaire();
        jIndiqueMonNuméroDeTélephonneCommeIdentifiant(login);
        jInidiqueMonCodeCommeMotDePasse(mdp);
        jeCliqueSurLeBouton();
        jeSuisConnectéÀMonEspacePersonnel();
    }
    @When("Je clique sur le lien Feuille de présence dans le header-container")
    public void jeCliqueSurLeLienDansLeHeaderContainer() {
        driver.findElement(By.cssSelector(".main_nav > li:nth-child(2) > a")).click();
    }
    @Then("J'ouvre le calendrier de signatures")
    public void jOuvreLeCalendrierDeSignatures() {
        Assert.assertFalse(driver.findElements(By.cssSelector(".container-fluid > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1)")).isEmpty());
    }
    @When("Je clique sur le lien Feuille de présence dans le body")
    public void jeCliqueSurLeLienDansLeBody() {
        driver.findElement(By.cssSelector("#dejasigner > a:nth-child(1)")).click();
    }


    @Given("Je suis sur la page du calendrier de signatures {string} {string} {string}")
    public void jeSuisSurLaPageDuCalendrierDeSignatures(String url, String login, String mdp) throws InterruptedException {
        jeSuisConnectéÀMonEspacePersonnel(url, login, mdp);
        jeCliqueSurLeLienDansLeHeaderContainer();
        jOuvreLeCalendrierDeSignatures();
    }
    @And("Ma signature est déjà créée")
    public void maSignatureEstDéjàCréée() {

    }
    public static String DateJour() {
        Date date_jour = new Date();
        DateFormat dateFormat = new SimpleDateFormat("\\3MM\\/dd\\/yyyy");
        DateFormat heureFormat = new SimpleDateFormat("a");
        String date = dateFormat.format(date_jour);
        String heure = heureFormat.format(date_jour).toLowerCase();
        return ("#" + date.substring(0, 3) + " " + date.substring(3) + heure);
    }
    @When("Je clique sur l'image Emarger ici correspondant à la date du jour et à la plage horaire")
    public void jeCliqueSurLImageEmargerIciCorrespondantÀLaDateDuJourEtÀLaPlageHoraire() {
        driver.findElement(By.cssSelector(DateJour())).click();
    }
    @Then("L'image Emarger ici est remplacée par ma signature")
    public void lImageEstRemplacéeParMaSignature() {
        String img = driver.findElement(By.cssSelector(DateJour())).getAttribute("src");
        Assert.assertFalse(img.contains("signatureicon"));
    }


    @Given("Ma signature est bien présente dans la case \\(date du jour, plage horaire) {string} {string} {string}")
    public void maSignatureEstBienPrésenteDansLaCaseDateDuJourPlageHoraire(String url, String login, String mdp) throws InterruptedException {
        jeSuisSurLaPageDuCalendrierDeSignatures(url, login, mdp);
        lImageEstRemplacéeParMaSignature();
    }
    @When("Je remonte tout en haut de la page")
    public void jeRemonteToutEnHautDeLaPage() {
        driver.findElement(By.cssSelector(".main_nav > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)")).click();
    }
    @Then("L'affichage de la top-bar réapparait")
    public void lAffichageDeLaTopBarRéapparait() {
        Assert.assertFalse(driver.findElements(By.cssSelector(".top_bar_content")).isEmpty());
    }
    @When("Je clique sur le lien en haut à droite Valider et se déconecter")
    public void jeCliqueSurLeLienEnHautÀDroite() {
        driver.findElement(By.cssSelector(".login_button > a")).click();
    }
    @When("Je clique sur le lien Retour à l'accueil en haut de page")
    public void jeCliqueSurLeLienRetourÀLAccueilEnHautDePage() {
        driver.findElement(By.cssSelector(".col-md-8 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a")).click();
    }
    @Then("Je reviens sur la page d'accueil")
    public void jeReviensSurLaPageDAccueil() {
        Assert.assertFalse(driver.findElements(By.cssSelector(".col-md-8 > div:nth-child(1) > div:nth-child(1) > h5:nth-child(1)")).isEmpty());
    }

    @And("test etape")
    public void testEtape() {

    }
}

