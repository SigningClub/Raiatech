package com.example.demo.professor;
import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "api/v1/professor")
public class ProfController {
    private final ProfService profService = new ProfService();

    @GetMapping
	public List<professsor> hello(){
		return profService.hello();
	}

}

