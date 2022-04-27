package com.raiatech.demo.estudante;

public class Estudante {
	
	Long codEst;
	String nomeEst;
    String emailEst;
    String login;
    String senha;
    String cpf;
    
	public Estudante(Long codEst, String nomeEst, String emailEst, String login, String senha, String cpf) {
		super();
		this.codEst = codEst;
		this.nomeEst = nomeEst;
		this.emailEst = emailEst;
		this.login = login;
		this.senha = senha;
		this.cpf = cpf;
	}
	
	public Long getCodEst() {
		return codEst;
	}
	
	public void setCodEst(Long codEst) {
		this.codEst = codEst;
	}
	
	public String getNomeEst() {
		return nomeEst;
	}
	
	public void setNomeEst(String nomeEst) {
		this.nomeEst = nomeEst;
	}
	
	public String getEmailEst() {
		return emailEst;
	}
	
	public void setEmailEst(String emailEst) {
		this.emailEst = emailEst;
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
