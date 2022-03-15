package com.example.demo.professor;
import java.util.List;

public class ProfService {
    public List<professsor> hello(){
		return List.of(new professsor(15151, "nomeProf", "emailProf", "login", "senha", "cpf"));
	}
}
