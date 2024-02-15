package Junit;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class DemoqaTest {
    WebDriver driver;

    @BeforeAll
    static void setupAll() {
        WebDriverManager.chromedriver().setup();
    }

    @BeforeEach
    void setup() {
        driver = new ChromeDriver();
        driver.get("https://demoqa.com/");
        driver.manage().window().maximize();
    }

    @AfterEach
    void teardown() {
        driver.quit();
    }

    @Test
    void acceptCookies() {
        driver.findElement(By.xpath("//p[text()='Autoriser']")).click();
        boolean acceptedCookies = driver.findElements(By.xpath("//p[text()='Autoriser']")).isEmpty();
        Assertions.assertTrue(acceptedCookies);
        boolean homeBanner = driver.findElements(By.xpath("//*[@class='home-banner']")).isEmpty();
        Assertions.assertFalse(homeBanner);
    }

    @Test
    void goToLinksElementsPage() {
        acceptCookies();
        JavascriptExecutor jse = (JavascriptExecutor) driver;
        WebElement elementsCard = driver.findElement(By.xpath("//h5[contains(.,'Elements')]"));
        jse.executeScript("arguments[0].scrollIntoView();", elementsCard);
        elementsCard.click();
        boolean elementsTitle = driver
                .findElements(By.xpath("//h5[contains(.,'Elements')]")).isEmpty();
        Assertions.assertTrue(elementsTitle);
        driver.findElement(By.xpath("//span[text()='Links']")).click();
        boolean mainElementsTitle = driver
                .findElements(By.xpath("//*[@class='main-header'][text()='Elements']")).isEmpty();
        Assertions.assertTrue(mainElementsTitle);
        boolean mainLinksTitle = driver
                .findElements(By.xpath("//*[@class='main-header'][text()='Links']")).isEmpty();
        Assertions.assertFalse(mainLinksTitle);
    }

    @Test
    void doBadRequest() {
        goToLinksElementsPage();
        driver.findElement(By.id("bad-request")).click();
        JavascriptExecutor jse = (JavascriptExecutor) driver;
        WebElement response = driver.findElement(By.xpath("//p[@id='linkResponse']"));
        jse.executeScript("arguments[0].scrollIntoView();", response);
        String responseExpected = "Link has responded with status 400 and status text Bad Request";
        boolean isCorrectText = response.getText()
                .equals(responseExpected);
        //System.out.println(response.getText());
        //System.out.println(responseExpected);
        Assertions.assertTrue(isCorrectText);
    }

    @Test
    void goToPracticeForm() {
        acceptCookies();
        JavascriptExecutor jse = (JavascriptExecutor) driver;
        WebElement elementsCard = driver.findElement(By.xpath("//h5[contains(.,'Forms')]"));
        jse.executeScript("arguments[0].scrollIntoView();", elementsCard);
        elementsCard.click();
        boolean elementsTitle = driver.findElements(By.xpath("//h5[contains(.,'Forms')]")).isEmpty();
        Assertions.assertTrue(elementsTitle);
        driver.findElement(By.xpath("//span[text()='Practice Form']")).click();
        boolean mainElementsTitle = driver
                .findElements(By.xpath("//*[@class='main-header'][text()='Forms']")).isEmpty();
        Assertions.assertTrue(mainElementsTitle);
        boolean mainLinksTitle = driver
                .findElements(By.xpath("//*[@class='main-header'][text()='Practice Form']")).isEmpty();
        Assertions.assertFalse(mainLinksTitle);
    }

    @Test
    void fillAndSubmitTheForm() {
        goToPracticeForm();
        JavascriptExecutor jse = (JavascriptExecutor) driver;

        // First Name
        WebElement inputFirstName = driver.findElement(By.id("firstName"));
        Assertions.assertTrue(inputFirstName.isEnabled());
        inputFirstName.sendKeys("John");
        // Last Name
        WebElement inputLastName = driver.findElement(By.id("lastName"));
        Assertions.assertTrue(inputLastName.isEnabled());
        inputLastName.sendKeys("Doe");
        // Email
        WebElement inputUserEmail = driver.findElement(By.id("userEmail"));
        Assertions.assertTrue(inputUserEmail.isEnabled());
        inputUserEmail.sendKeys("john_doe@gmail.com");
        // Gender
        WebElement optionGenderRadio = driver.findElement(By.xpath("//label[text()='Male']"));
        Assertions.assertTrue(optionGenderRadio.isEnabled());
        optionGenderRadio.click();
        WebElement optionRadioButton = driver.findElement(By.cssSelector("#gender-radio-1"));
        Assertions.assertTrue(optionRadioButton.isSelected());
        // Number
        WebElement inputUserNumber = driver.findElement(By.id("userNumber"));
        Assertions.assertTrue(inputUserNumber.isEnabled());
        inputUserNumber.sendKeys("0706100710");

        // Birth Date
        WebElement birthDate = driver.findElement(By.id("dateOfBirthInput"));
        birthDate.click();
        Select birthYear = new Select(driver
                .findElement(By.xpath("//select[contains(@class,'year')]")));
        birthYear.selectByVisibleText("1989");
        Select monthYear = new Select(driver
                .findElement(By.xpath("//select[contains(@class,'month')]")));
        monthYear.selectByVisibleText("October");
        driver.findElement(By.xpath("//*[contains(@class,'day')][text()='29']")).click();
        boolean isBirthDate = birthDate.getAttribute("value").equals("29 Oct 1989");
        //System.out.println(birthDate.getAttribute("value"));
        //System.out.println("29 Oct 1989");
        Assertions.assertTrue(isBirthDate);

        // Subjects
        WebElement subjects = driver.findElement(By.id("subjectsInput"));
        jse.executeScript("arguments[0].scrollIntoView();", subjects);
        subjects.sendKeys("s");
        driver.findElement(By.id("react-select-2-option-3")).click();
        WebElement selectedSubject = driver
                .findElement(By.xpath("//div[contains(@class,'multiValue ')]/div"));
        boolean isCorrectSubject = selectedSubject.getText()
                .equals("Chemistry");
        //System.out.println(selectedSubject.getText());
        //System.out.println("Chemistry");
        Assertions.assertTrue(isCorrectSubject);

        // Hobbies
        WebElement firstCheckbox = driver.findElement(By.xpath("//label[text()='Sports']"));
        Assertions.assertTrue(firstCheckbox.isEnabled());
        firstCheckbox.click();
        Assertions.assertTrue(driver.findElement(By.id("hobbies-checkbox-1")).isSelected());
        WebElement thirdCheckbox = driver.findElement(By.xpath("//label[text()='Music']"));
        Assertions.assertTrue(thirdCheckbox.isEnabled());
        thirdCheckbox.click();
        Assertions.assertTrue(driver.findElement(By.id("hobbies-checkbox-3")).isSelected());

        // Current Address
        driver.findElement(By.id("currentAddress")).sendKeys("1 rue de Paris\n59000 - LILLE");

        // State - City
        WebElement state = driver.findElement(By.xpath("//input[@id='react-select-3-input']"));
        state.sendKeys("Haryana");
        state.sendKeys(Keys.ENTER);
        WebElement city = driver.findElement(By.xpath("//input[@id='react-select-4-input']"));
        city.sendKeys("Panipat");
        city.sendKeys(Keys.ENTER);

        // Submit
        WebElement submitButton = driver.findElement(By.id("submit"));
        jse.executeScript("arguments[0].click();", submitButton);
        WebElement thanksMessage = driver.
                findElement(By.xpath("//*[contains(.,'Thanks for submitting')]"));
        Assertions.assertTrue(thanksMessage.isDisplayed());
    }
}