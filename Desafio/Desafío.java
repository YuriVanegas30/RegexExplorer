import java.util.regex.*;
import java.util.*;

public class Desafío {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduzca el texto: ");
        String texto = sc.nextLine();

        String regexFlotante = "\\b-?\\d+\\.\\d+\\b";
        String regexEntero = "(?<!\\.)\\b-?\\d+\\b(?!\\.)";
        String regexString = "\"(.*?)\"";
        String regexLista = "\\[\\s*-?\\d+(?:\\s*,\\s*-?\\d+)*\\s*\\]";
        String regexBooleano = "\\b(True|False)\\b";

        List<String> flotantes = buscar(texto, regexFlotante);
        List<String> enteros = buscar(texto, regexEntero);
        List<String> strings = buscar(texto, regexString);
        List<String> listas = buscar(texto, regexLista);
        List<String> booleanos = buscar(texto, regexBooleano);

        System.out.println("\nResultados encontrados:");
        System.out.println("Enteros: " + enteros);
        System.out.println("Flotantes: " + flotantes);
        System.out.println("Strings: " + strings);
        System.out.println("Listas: " + listas);
        System.out.println("Booleanos: " + booleanos);
    }

    public static List<String> buscar(String texto, String regex) {
        List<String> coincidencias = new ArrayList<>();
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(texto);
        while (matcher.find()) {
            coincidencias.add(matcher.group());
        }
        return coincidencias;
    }
}
