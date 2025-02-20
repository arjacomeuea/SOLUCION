using System;
using System.Collections.Generic;
using System.Linq;

public class CampañaVacunacion
{
    public static void Main(string[] args)
    {
        // Crear conjuntos ficticios de ciudadanos
        HashSet<string> ciudadanos = CrearConjuntoCiudadanos(500);
        HashSet<string> pfizer = CrearConjuntoCiudadanos(75);
        HashSet<string> astrazeneca = CrearConjuntoCiudadanos(75);

        // Calcular conjuntos resultantes aplicando operaciones de conjuntos
        HashSet<string> noVacunados = new HashSet<string>(ciudadanos);
        noVacunados.ExceptWith(pfizer);
        noVacunados.ExceptWith(astrazeneca);

        HashSet<string> dosVacunas = new HashSet<string>(pfizer);
        dosVacunas.IntersectWith(astrazeneca);

        HashSet<string> soloPfizer = new HashSet<string>(pfizer);
        soloPfizer.ExceptWith(astrazeneca);

        HashSet<string> soloAstrazeneca = new HashSet<string>(astrazeneca);
        soloAstrazeneca.ExceptWith(pfizer);

        // Mostrar resultados
        Console.WriteLine("Ciudadanos no vacunados:");
        MostrarCiudadanos(noVacunados);

        Console.WriteLine("\nCiudadanos con dos vacunas:");
        MostrarCiudadanos(dosVacunas);

        Console.WriteLine("\nCiudadanos con vacuna Pfizer solamente:");
        MostrarCiudadanos(soloPfizer);

        Console.WriteLine("\nCiudadanos con vacuna Astrazeneca solamente:");
        MostrarCiudadanos(soloAstrazeneca);
    }

    // Función para crear un conjunto ficticio de ciudadanos
    static HashSet<string> CrearConjuntoCiudadanos(int cantidad)
    {
        HashSet<string> ciudadanos = new HashSet<string>();
        for (int i = 1; i <= cantidad; i++)
        {
            ciudadanos.Add("Ciudadano" + i);
        }
        return ciudadanos;
    }

    // Función para mostrar un conjunto de ciudadanos
    static void MostrarCiudadanos(HashSet<string> ciudadanos)
    {
        if (ciudadanos.Count == 0)
        {
            Console.WriteLine("No hay ciudadanos en este conjunto.");
        }
        else
        {
            foreach (string ciudadano in ciudadanos)
            {
                Console.WriteLine(ciudadano);
            }
        }
    }
}