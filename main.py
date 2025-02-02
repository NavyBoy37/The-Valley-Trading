from initial_generation import (
    Feldor_Initialization,
    Crankston_Initialization,
    Tetra_Tower_Initialization,
    Cabella_Initialization,
    Foyella_Initialization,
)
from running_functions import Map_Total_Supplies, Price_Calculator


cities = [
    Feldor_Initialization(),
    Crankston_Initialization(),
    Tetra_Tower_Initialization(),
    Cabella_Initialization(),
    Foyella_Initialization(),
]
Feldor = cities[0]
Crankston = cities[1]
Tetra_Tower = cities[2]
Cabella = cities[3]
Foyella = cities[4]

"""Goods Guide
corn
iron_ore

"""
Price_Calculator(Feldor, "corn")
Price_Calculator(Crankston, "iron_ore")
print(Map_Total_Supplies("corn"))
Price_Calculator(Tetra_Tower, "corn")
