package com.raiatech.demo.estudante;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

public interface EstudanteRepository extends JpaRepository<Estudante, Long> {
	
	Optional<Estudante> findById(Long codProf);

	Optional<Estudante> findByUsername(String nomeProf);
}
