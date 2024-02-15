/*
1er exercice : automatiser la signature de la feuille de feuille de présence
(Transposition du programme m2i_auto_sign depuis la version python)
Désormais non fonctionnel car données personnelles masquées
et date actuelle non utilisable sur la feuille.
*/

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
// import org.openqa.selenium.firefox.FirefoxDriver;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class m2i_auto_sign {
    static WebDriver driver;
    public static String DateJour() {
        Date date_jour = new Date();
        DateFormat dateFormat = new SimpleDateFormat("\\3MM\\/dd\\/yyyy");
        DateFormat heureFormat = new SimpleDateFormat("a");
        String date = dateFormat.format(date_jour);
        String heure = heureFormat.format(date_jour).toLowerCase();
        return ("#" + date.substring(0, 3) + " " + date.substring(3) + heure);
    }

    public static void main(String[] args) throws InterruptedException {

        // System.setProperty("webdriver.gecko.driver", "C:\\maven\\drivers\\geckodriver.exe");
        System.setProperty("webdriver.chrome.driver", "C:\\maven\\drivers\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.get("https://sign.m2iformation.fr");
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        // Cliquer sur "Espace stagiaire"
        driver.findElement(By.cssSelector(".col-md-8 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h5:nth-child(1)")).click();

        // Remplir le champ "Email ou n° de télephone" avec l'identifiant :
        driver.findElement(By.cssSelector("#inputPhoneNumber")).sendKeys("**********");

        // Remplir le champ "Code pin" :
        driver.findElement(By.cssSelector("#inputSmsCode")).sendKeys("*****");

        // Cliquer sur le bouton "Se connecter" :
        driver.findElement(By.cssSelector("#connexion")).click();
        //TimeUnit.SECONDS.sleep(5);

        // Cliquer sur le lien "Feuille de présence" :
        driver.findElement(By.cssSelector(".main_nav > li:nth-child(2) > a")).click();
        TimeUnit.SECONDS.sleep(1);

        // Cliquer sur l'image "Emarger ici" correspondant à la date du jour :
        driver.findElement(By.cssSelector(DateJour())).click();
        TimeUnit.SECONDS.sleep(1);

        // Retour en haut de la page :
        driver.findElement(By.cssSelector(".main_nav > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)")).click();

        // Cliquer sur "Valider et se déconnecter" :
        driver.findElement(By.cssSelector(".login_button > a")).click();

        TimeUnit.SECONDS.sleep(1);
        driver.close();
    }
}