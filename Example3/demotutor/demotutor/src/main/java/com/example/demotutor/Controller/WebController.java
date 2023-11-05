package com.example.demotutor.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class WebController {

    @GetMapping("/hello")
    public String getHello(Model model) {
        model.addAttribute("message", "Hello, Thymeleaf!");
        return "hello";
    }
}
