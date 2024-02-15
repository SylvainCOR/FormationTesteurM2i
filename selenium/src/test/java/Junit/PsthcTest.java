package Junit;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

import java.util.concurrent.TimeUnit;

public class PsthcTest {

    WebDriver driver;

    @BeforeAll
    static void setupAll() {
        WebDriverManager.chromedriver().setup();
    }

    @BeforeEach
    void setup() {
        driver = new ChromeDriver();
    }

    @AfterEach
    void teardown() {
        driver.quit();
    }


    @Test
    void go_psthc_accept_cookies() throws InterruptedException {
        driver.get("https://www.psthc.fr/");
        driver.manage().window().maximize();
        TimeUnit.SECONDS.sleep(1);
        driver.findElement(By.cssSelector("#didomi-notice-agree-button")).click();
    }

    @Test
    void connexion_ok() throws InterruptedException {
        go_psthc_accept_cookies();
        driver.findElement(By.cssSelector("#btnConnect > span:nth-child(1)")).click();
        TimeUnit.SECONDS.sleep(1);
        driver.findElement(By.cssSelector("#username")).sendKeys("********");
        driver.findElement(By.cssSelector("#password")).sendKeys("*********");
        driver.findElement(By.cssSelector("#autologin")).click();
        driver.findElement(By.cssSelector(".button1")).click();
    }

    @Test
    void connexion_id_ko() throws InterruptedException {
        go_psthc_accept_cookies();
        driver.findElement(By.cssSelector("#btnConnect > span:nth-child(1)")).click();
        TimeUnit.SECONDS.sleep(1);
        driver.findElement(By.cssSelector("#username")).sendKeys("id_faux");
        driver.findElement(By.cssSelector("#password")).sendKeys("*********");
        driver.findElement(By.cssSelector(".button1")).click();
        TimeUnit.SECONDS.sleep(1);
        WebElement test_error = driver.findElement(By.cssSelector(".error"));
        System.out.println("Message d'erreur : \n" + test_error.getText());
    }

    @Test
    void connexion_mdp_ko() throws InterruptedException {
        go_psthc_accept_cookies();
        driver.findElement(By.cssSelector("#btnConnect > span:nth-child(1)")).click();
        TimeUnit.SECONDS.sleep(1);
        driver.findElement(By.cssSelector("#username")).sendKeys("********");
        driver.findElement(By.cssSelector("#password")).sendKeys("mdp_faux");
        driver.findElement(By.cssSelector(".button1")).click();
        TimeUnit.SECONDS.sleep(1);
        WebElement test_error = driver.findElement(By.cssSelector(".error"));
        System.out.println("Message d'erreur : \n" + test_error.getText());
    }

    @Test
    void deconnexion() throws InterruptedException {
        connexion_ok();
        driver.findElement(By.cssSelector("#btnMember")).click();
        TimeUnit.SECONDS.sleep(1);
        driver.findElement(By.cssSelector("#menu-member > a:nth-child(8) > div:nth-child(1)")).click();
        driver.findElement(By.cssSelector("#menu-main > a:nth-child(3) > div:nth-child(1)")).click();
    }
    @Test
    void trophee_rare() throws InterruptedException {
        connexion_ok();
        TimeUnit.SECONDS.sleep(1);
        driver.findElement(By.cssSelector("#btnMember")).click();
        TimeUnit.SECONDS.sleep(2);
        driver.findElement(By.cssSelector("#menu-member > a:nth-child(3) > div:nth-child(1)")).click();
        TimeUnit.SECONDS.sleep(3);
        Actions action = new Actions(driver);
        action.moveToElement(driver.findElement(By.xpath("//div/div[contains(.,'rares')]//a[1]"))).click().perform();
        String texte1 = driver.findElement(By.xpath("//div/div[contains(.,'rares')]/div[3]/div[1]/div[3]/p")).getText();
        String texte2 = driver.findElement(By.xpath("//div/div[contains(.,'rares')]/div[3]/div[1]/div[3]/em")).getText();
        String texte3 = driver.findElement(By.xpath("//div/div[contains(.,'rares')]/div[3]/div[1]/div[4]")).getText();
        System.out.println("Trophée le plus rare :\n" + texte1 + "\n" + texte2 + "\nObtenu le " + texte3.substring(0,9) + " à " + texte3.substring(11,16));
    }
}
