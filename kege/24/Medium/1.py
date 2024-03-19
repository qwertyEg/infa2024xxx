package BOOT-INF.classes.com.server;

import java.io.File;
import java.util.Objects;
import java.util.Scanner;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HelloController {
  @GetMapping({"/"})
  public String index(Model model) {
    model.addAttribute(", ":)");
    return "welcome";
  }
  
  @GetMapping({"/doc/{document}"})
  public void getDocument(@PathVariable String document) {
    System.out.println("This function is not ready yet");
  }
  
  @GetMapping({"/login"})
  public String login(@RequestParam String password) {
    String adminPassword = "password";
    String flag = "flag";
    try {
      Scanner scanner = new Scanner(new File("password.txt"));
      try {
        adminPassword = scanner.nextLine();
        scanner.close();
      } catch (Throwable throwable) {
        try {
          scanner.close();
        } catch (Throwable throwable1) {
          throwable.addSuppressed(throwable1);
        } 
        throw throwable;
      } 
    } catch (Exception e) {
      System.out.println(e.toString());
    } 
    if (Objects.equals(adminPassword, password))
      try {
        Scanner scanner = new Scanner(new File("flag"));
        try {
          flag = scanner.nextLine();
          scanner.close();
        } catch (Throwable throwable) {
          try {
            scanner.close();
          } catch (Throwable throwable1) {
            throwable.addSuppressed(throwable1);
          } 
          throw throwable;
        } 
      } catch (Exception e) {
        throw new RuntimeException(e);
      }  
    return flag;
  }
}
