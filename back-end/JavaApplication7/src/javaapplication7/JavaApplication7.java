/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication7;
import java.util.Scanner;
/**
 *
 * @author gabri
 */
public class JavaApplication7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        login start = new login();
        Scanner in = new Scanner(System.in);
        loginEstudante start2 = new loginEstudante();
        System.out.print("Escolha teste(1: professor, 2 aluno): ");
        int escolha = Integer.parseInt(in.nextLine());
        switch(escolha){
            case 1:
                start.testeBackEnd();
                break;
            case 2:
                start2.testeBackEnd();
                break;
            default:
                System.err.println("Opção inválida");
                
        }
    }
    
}
