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
 * @author gabri
 */
public class login {

    public Boolean consulta(String usuario, String senha) {
        Boolean retorno = false;
        try {

            String myDriver = "org.apache.derby.jdbc.EmbeddedDriver";
            String myUrl = "jdbc:derby://localhost/1527dbRaia;create=true";
            Class.forName(myDriver);
            Connection conn = DriverManager.getConnection(myUrl, "APP", "1234");

            String query = "SELECT * FROM PROFESSOR";

            Statement st = conn.createStatement();

            ResultSet rs = st.executeQuery(query);

            while (rs.next()) {
                String comparação = rs.getString("USUARIO");
                String comparação2 = rs.getString("SENHA");
                if (comparação.equals(usuario)) {
                    System.out.println("Usuário encontrado");
                    if(comparação2.equals(senha)){
                        System.out.println("Senha correta");
                        retorno = true;
                        break;
                    
                    }
                    else{
                        System.err.println("Senha incorreta");
                        break;
                    }
                

                }

            }

            st.close();

        } catch (Exception e) {
            System.err.println("Got an exception! ");
            System.err.println(e.getMessage());
        }
        return retorno;

    }

    public void testeBackEnd() {
        while (true) {
            Boolean teste;
            Scanner in = new Scanner(System.in);
            System.out.print("Usuário:");
            String usuario = in.next();
            System.out.print("Senha:");
            String senha = in.next();
            teste = consulta(usuario, senha);
            System.out.println(teste.toString());
        }

    }

}
