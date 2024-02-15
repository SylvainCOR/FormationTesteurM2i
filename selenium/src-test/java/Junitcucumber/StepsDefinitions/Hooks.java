package Junitcucumber.StepsDefinitions;

import io.github.bonigarcia.wdm.WebDriverManager;
import io.cucumber.java.After;
import io.cucumber.java.Before;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class Hooks {

    public static WebDriver driver;
    @Before
    public void beforeScenario(){
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }
    @After
    public void afterScenario(){
        if (driver !=null){
            driver.quit();
        }
    }
}
