using System;
using System.Security.Cryptography;

internal class Program
{
    private static void Main(string[] args)
    {
        Console.Write("Wat is je geboorte datum in dag/maand/jaar: ");
        var dataVerjaardag = Console.ReadLine();
        DateTime dt;

        var verjaardag = DateTime.Parse(dataVerjaardag);


        var dateNu = DateTime.Now;
       

        TimeSpan verschil = dateNu - verjaardag;
        var dagen = verschil.Days;
        
       
        decimal dagen2 = verschil.Days;
        var VerKdag = Math.Ceiling(dagen2 / 1000);

        var Count = 0;
        var x = dagen % 1000;

        while(x < 1000)
        {
            x += 1;
            Count += 1;


        }

        dagen = Count;
        DateTime b = dateNu.AddDays(dagen);




  
        
      


        Console.Write($"Over {dagen} dagen op ");
        Console.Write(b);
        Console.Write($" is het je {VerKdag} de/ste verKdag!  ");
    }
}