In this project, i develop a Python application, which employs backtracking to color the countries 
in South America.

!(map_output)[ColorMapping.png]

Firstly i define color and countries then i create a dictionary (dictCountries) which takes countries and 
their neighbours. I need to color the country with the most neighbors so i define sort function to sort 
all countries according to numbers of neighbours. Then i define colorThecountry function to color the 
sorted countries by back-tracking. Then i define isColoredTheTrue function to check if one of the 
neighbors of a country has the same color as the country. If there is a problem like same color then 
this functions will help to our colorThecountry functions to know that.

Variables: X = 
- {"Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay","Peru", "Suriname", "Uruguay", "Venezuela"}

Domains: D = 
- {"blue", "green", "red", "yellow"} 

Constraints: adjacent regions must have different colors.

C = { 
- ( "Argentina" != "Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"),
- ("Bolivia" != "Argentina", "Brazil", "Chile", "Paraguay", "Peru"),
- ("Brazil" != "Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"),
- ("Chile" != " Argentina", "Bolivia", "Peru"),
- ("Colombia" !="Brazil", "Ecuador", "Peru", "Venezuela"),
- ("Ecuador" != "Colombia", "Bolivia", "Peru"),
- ("Guyana" != "Brazil", "Suriname", "Venezuela"), 
- ("Paraguay" !="Argentina", "Bolivia", "Brazil"),
- ("Peru" != "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"),
- ("Suriname" != "Brazil", "Guyana"),
- ("Uruguay" !="Argentina", "Brazil"),
- ("Venezuela" != "Brazil", "Colombia", "Guyana") 
}

