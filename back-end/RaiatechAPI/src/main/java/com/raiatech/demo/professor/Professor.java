package com.raiatech.demo.professor;

import javax.persistence.Entity;

@Entity
public class Professor {
	
	Long codProf;
    String nomeProf;
    String emailProf;
    String login;
    String senha;
    String cpf;
	
    public Professor(Long codProf, String nomeProf, String emailProf, String login, String senha, String cpf) {
		super();
		this.codProf = codProf;
		this.nomeProf = nomeProf;
		this.emailProf = emailProf;
		this.login = login;
		this.senha = senha;
		this.cpf = cpf;
	}
    
    public Long getCodProf() {
        return codProf;
    }

    public void setCodProf(Long codProf) {
        this.codProf = codProf;
    }

    public String getNomeProf() {
        return nomeProf;
    }

    public void setNomeProf(String nomeProf) {
        this.nomeProf = nomeProf;
    }

    public String getEmailProf() {
        return emailProf;
    }

    public void setEmailProf(String emailProf) {
        this.emailProf = emailProf;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    @Override
    public String toString() {
        return super.toString();
    }
}