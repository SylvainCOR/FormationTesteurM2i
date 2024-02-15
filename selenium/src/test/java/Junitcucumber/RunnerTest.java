package Junitcucumber;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
        features = "src/test/resources/features/junitcucumber",
        glue =  {"Junitcucumber"},
        tags = "@SignUp or @SignIn"
)

public class RunnerTest {

}
