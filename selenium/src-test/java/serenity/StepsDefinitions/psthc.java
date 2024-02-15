package serenity.StepsDefinitions;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import net.serenitybdd.core.pages.PageObject;
import net.serenitybdd.core.pages.WebElementFacade;
import org.openqa.selenium.support.FindBy;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class psthc extends PageObject {
    //---SELECTORS-------------------------------------------------------------
    @FindBy(css="#didomi-notice-agree-button")
    WebElementFacade accept_cookies;
    @FindBy(css = "#btnConnect > span:nth-child(1)")
    WebElementFacade sign_in;
    @FindBy(id = "username")
    WebElementFacade input_username;
    @FindBy(id = "password")
    WebElementFacade input_password;
    @FindBy(css = ".button1")
    WebElementFacade connexion;
    @FindBy(id = "btnMember")
    WebElementFacade member_name;
    @FindBy(xpath = "//*[@id='menu-main']//span[contains(@class, 'fa-shopping-cart')]")
    WebElementFacade shopping_link;
    @FindBy(xpath = "//*[@id='test-list']//img[@title='Amazon']")
    WebElementFacade amazon_img;
    @FindBy(id = "nav-logo-sprites")
    WebElementFacade amazon_page;
    @FindBy(xpath = "//*[@class='nav-logo-base nav-sprite']")
    WebElementFacade logo_amazon;
    //------------------------------------------------------------------------


    //---BACKGROUND-----------------------------------------------------------
    @Given("he opens {string} website")
    public void heOpensWebsite(String url) {
        openAt(url);
        waitFor(accept_cookies);
    }
    @And("he accepts cookies")
    public void heAcceptsCookies() {
        clickOn(accept_cookies);
        shouldNotBeVisible(accept_cookies);
    }
    //------------------------------------------------------------------------


    //---SCENARIO_CONNEXION---------------------------------------------------
    @When("he clicks on the signin button")
    public void heClicksOnTheSigninButton() {
        waitFor(sign_in);
        clickOn(sign_in);
    }
    @Then("he goes on login page")
    public void heGoesOnLoginPage() {
        waitFor(input_username);
    }
    @When("he clicks on the username empty field and type {string}")
    public void heClicksOnTheUsernameEmptyFieldAndType(String username) {
        input_username.getAttribute("");
        typeInto(input_username, username);
    }
    @And("he clicks on the password empty field and type {string}")
    public void heClicksOnThePasswordEmptyFieldAndType(String password) {
        input_password.getAttribute("");
        typeInto(input_password, password);
    }
    @And("he clicks on the connection button")
    public void heClicksOnTheConnectionButton() {
        clickOn(connexion);
    }
    @Then("he is connected as {string}")
    public void heIsConnectedAs(String member) {
        waitFor(member_name);
        containsElements(member, member_name);
    }
    //------------------------------------------------------------------------


    //---SCENARIO_AMAZON_STORE------------------------------------------------
    @When("he clicks on shopping link")
    public void heClicksOnShoppingLink() {
        clickOn(shopping_link);
    }
    @Then("shopping stores page is opened")
    public void shoppingStoresPageIsOpened() {
        waitFor(amazon_img);
    }
    @When("he clicks on amazon image")
    public void heClicksOnAmazonImage() {
        clickOn(amazon_img);
    }
    @Then("amazon store page is opened in a new tab")
    public void amazonStorePageIsOpenedInANewTab() {
        Set<String> handles = getDriver().getWindowHandles();
        List<String> handlesList = new ArrayList<>(handles);
        String secondTab = handlesList.get(1);
        getDriver().switchTo().window(secondTab);
        waitFor(amazon_page);
        waitFor(logo_amazon);
    }
    //------------------------------------------------------------------------


}









