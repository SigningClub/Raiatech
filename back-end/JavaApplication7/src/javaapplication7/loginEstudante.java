/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication7;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

/**
 *
 * @author Paulo Vitor
 */
public class loginEstudante {
    
    public Boolean consulta(String user, String password) {
        Boolean retorno = false;
        try {
            String myDriver = "org.apache.derby.jdbc.EmbeddedDriver";
            String myUrl = "jdbc:derby://localhost/1527dbRaia;create=true";
            Class.forName(myDriver);
            Connection conn = DriverManager.getConnection(myUrl, "APP", "1234");
            String query = "SELECT * FROM ESTUDANTES";
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery(query);
            
            while (rs.next()) {
                String usuario = rs.getString("USUARIO");
                String senha = rs.getString("SENHA");
                if (usuario.equals(user)) {
                    System.out.println("Usuário encontrado!");
                    if(senha.equals(password)){
                        System.out.println("Senha correta!");
                        retorno = true;
                        break;
                    } else {
                        System.err.println("Senha incorreta!");
                        break;
                    }
                } else { 
                    System.err.println("Usuário não encontrado!");
                    break;
                }
            }
            st.close();
        } catch (Exception e) {
            System.err.println("Got an exception!");
            System.err.println(e.getMessage());
        
        }
        return retorno;
    }
    
    public void testeBackEnd() {
        
        while (true) {
            Boolean teste;
            Scanner in = new Scanner(System.in);
            System.out.print("Estudante:");
            String estudante = in.next();
            System.out.print("Senha:");
            String senha = in.next();
            teste = consulta(estudante, senha);
            System.out.println(teste.toString());
        }
    }
}
