package com.raiatech.demo.estudante;

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
@RequestMapping("api/v1/estudante")
@Api(value="ESTUDANTE")
public class EstudanteController {
	
	@Autowired
	private EstudanteRepository estudanteRepository;
	
	@RequestMapping(value="/", method=RequestMethod.GET)
	@ApiOperation(value="Retorna uma lista de professores")
	public ResponseEntity<?> listaEstudantes(){
		List<Estudante> obj = estudanteRepository.findAll();
		return ResponseEntity.ok().body(obj);
	}
	
	@RequestMapping(value="/{id}", method=RequestMethod.GET)
	@ApiOperation(value="Retorna um professor único")
	public ResponseEntity<?> listaEstudanteUnico(@PathVariable(value="codEst") Long codEst){
		Optional<Estudante> obj =  estudanteRepository.findById(codEst);
		return ResponseEntity.ok().body(obj);
	}
}
