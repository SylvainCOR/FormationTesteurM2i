package Junitcucumber.StepsDefinitions;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;

import java.util.concurrent.TimeUnit;

import static Junitcucumber.StepsDefinitions.Hooks.driver;
import static org.junit.jupiter.api.Assertions.assertFalse;

public class UltimateqaStepDefs {

    @Given("user is on page {string}")
    public void userIsOnPage(String url) {
        driver.get(url);
    }
    @When("he clicks on sign in link in the header")
    public void heClicksOnSignInLinkInTheHeader() {
        driver.findElement(By.xpath("//a[contains(.,'Sign In')]")).click();
    }
    @Then("page switch to sign in page")
    public void pageSwitchToSignInPage() {
        assertFalse(driver.
                findElements(By.xpath("//h2[contains(.,'Welcome')]")).isEmpty());
    }
    @When("he clicks on create an account link at bottom of page")
    public void heClicksOnCreateAnAccountLinkAtBottomOfPage() {
        JavascriptExecutor jse = (JavascriptExecutor) driver;
        WebElement footer = driver.findElement(By.xpath("//footer"));
        jse.executeScript("arguments[0].scrollIntoView();", footer);
        WebElement link = driver.findElement(By.xpath("//a[contains(.,'Create')]"));
        jse.executeScript("arguments[0].click();", link);
    }
    @Then("page switch to sign up page")
    public void pageSwitchToSignUpPage() {
        assertFalse(driver.
                findElements(By.xpath("//h2[contains(.,'Create')]")).isEmpty());
    }
    @When("he clicks on sign up button")
    public void heClicksOnSignUpButton() {
        driver.findElement(By.xpath("//button[contains(.,'Sign up')]")).click();
    }
    @Then("error message {string} appear between page heading and form")
    public void errorMessageAppearBetweenPageHeadingAndForm(String errorMessage) throws InterruptedException {
        TimeUnit.SECONDS.sleep(1);
        String xpath = String.format("//li[contains(.,\"%s\")]", errorMessage);
        assertFalse(driver.findElements(By.xpath(xpath)).isEmpty());
    }
    @When("he fills the first name field with {string}")
    public void heFillsTheFirstNameFieldWithFirstName(String firstName) {
        driver.findElement(By.id("user[first_name]")).sendKeys(firstName);
    }
    @And("he fills the last name field with {string}")
    public void heFillsTheLastNameFieldWithLastName(String lastName) {
        driver.findElement(By.id("user[last_name]")).sendKeys(lastName);
    }
    @And("he fills the email field with {string}")
    public void heFillsTheEmailFieldWith(String email) {
        driver.findElement(By.id("user[email]")).sendKeys(email);
    }
    @And("he fills the password field with {string}")
    public void heFillsThePasswordFieldWith(String password) {
        driver.findElement(By.id("user[password]")).sendKeys(password);
    }
    @And("he clicks on checkbox to accept terms of use")
    public void heClicksOnCheckboxToAcceptTermsOfUse() {
        driver.findElement(By.id("user[terms]")).click();
    }
    @Then("he's connected on the product page")
    public void heSConnectedOnTheProductPage() throws InterruptedException {
        TimeUnit.MILLISECONDS.sleep(500);
        assertFalse(driver.findElements(By.id("main-content")).isEmpty());
    }
    @When("he clicks on the sign in button")
    public void heClicksOnTheSignInButton() {
        driver.findElement(By.xpath("//button[contains(.,'Sign in')]")).click();
    }
    @When("he clicks on {string} fields")
    public void heClicksOnFields(String fieldLocation) {
        String id = String.format("user[%s]", fieldLocation);
        driver.findElement(By.id(id)).click();
    }
    @And("he clicks somewhere else to get out of the flied \\(e.g. on the page heading)")
    public void heClicksSomewhereElseToGetOutOfTheFliedEGOnThePageHeading() {
        driver.findElement(By.xpath("//h2[@class='page__heading']")).click();
    }
    @Then("error message {string} appear under {string} field")
    public void errorMessageAppearUnderTheField(String errorMessage, String fieldLocation) {
        String xpath = String.format("//p[contains(@id,'%s') and contains(.,'%s')]", fieldLocation, errorMessage);
        assertFalse(driver.findElements(By.xpath(xpath)).isEmpty());
    }
}

