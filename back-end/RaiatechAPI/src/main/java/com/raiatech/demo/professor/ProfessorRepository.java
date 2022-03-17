package com.raiatech.demo.professor;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

public interface ProfessorRepository extends JpaRepository<Professor, Long> {
	
	Optional<Professor> findById(Long codProf);

	Optional<Professor> findByUsername(String nomeProf);
	
}
