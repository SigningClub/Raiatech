package com.raiatech.demo.professor;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;

@RestController
@RequestMapping("api/v1/professor")
@Api(value="PROFESSOR")
public class ProfessorController {
	
	@Autowired
	private ProfessorRepository professorRepository;
	
	@RequestMapping(value="/", method=RequestMethod.GET)
	@ApiOperation(value="Retorna uma lista de professores")
	public ResponseEntity<?> listaProfessores(){
		List<Professor> obj = professorRepository.findAll();
		return ResponseEntity.ok().body(obj);
	}
	
	@RequestMapping(value="/{id}", method=RequestMethod.GET)
	@ApiOperation(value="Retorna um professor único")
	public ResponseEntity<?> listaProfessorUnico(@PathVariable(value="codProf") Long codProf){
		Optional<Professor> obj =  professorRepository.findById(codProf);
		return ResponseEntity.ok().body(obj);
	}
}
