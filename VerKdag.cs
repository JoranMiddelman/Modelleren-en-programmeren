using System;

internal class Program
{
    private static void Main(string[] args)
    {   //vraag om de geboorte datum - user input
        Console.Write("Wat is je geboorte datum in maand/dag/jaar: ");
        
        //verkregen verjaardag
        var dataVerjaardag = Console.ReadLine();
        var verjaardag = DateTime.Parse(dataVerjaardag);
        
        //verkrijgen van de datum heden
        var dateNu = DateTime.Now;

        //hoeveel dagen leeft iemand
        TimeSpan verschil = (dateNu - verjaardag);
        var dagen = verschil.Days;
        
        //resten berekenen
        var x = (dagen % 1000);
        
        //tellen hoeveel dagen tot de volgende verKdag
        var Count = 0;

        while(x < 1000) {
            x += 1;
            Count += 1;
        }
        
        //andere naam geven
        dagen = Count;
        
        //Het optellen van de datum plus aantal dagen tot verKdag
        DateTime b = dateNu.AddDays(dagen);

        Console.Write($"Over {dagen} dagen op {b} is je verKdag!");

    }
}