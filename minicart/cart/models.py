from django.db import models


class Item(models.Model):
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price


_items_source_list = [
    Item(0, 'Grumpy Cat', 'Grumpy Cat\'s unique features are due to an ailment known as feline dwarfism and a skeletal abnormality causing a pronounced underbite.', 100),
    Item(1, 'Felicette', 'On October 18th, 1963, Felicette was launched into space by the French aeronautical institution. Felicette is the first and only cat to have returned to earth after travelling to outer space!', 120),
    Item(2, 'Crème Puff', 'Crème Puff was the oldest known cat in history, earning himself the Guinness World Record title for oldest known cat. Crème passed away at the AMAZING age of 38 years and 3 days old.', 80),
    Item(3, 'Tama', 'Tama was the beautiful Calico kitty that was named Station Master at the Kishi Station in Japan by railway officials in 2007. Her official duties were to greet passengers and look cute.', 100),
    Item(4, 'Orangey', 'Best known as \'Cat\' in Breakfast at Tiffany\'s, superstar Orangey has played roles alongside celebrities such as Audrey Hepburn and Dick Van Dyke. He has appeared in multiple roles in both film and television pieces and even won a Patsy Award.', 90),
    Item(5, 'Mayor Stubbs', 'People in Alaska decided to elect a stray ginger cat known around the town as Stubbs. Stubbs\' mayoral office was set up at the town\'s general store and stayed there until he retired from office some 20 years later!', 100),
    Item(6, 'Bob', 'When James had given up on life, a chirpy little kitten he named Bob, wandered across his path with an infected wound on his leg and demanded James’ attention. Bob gave his new owner a reason to keep living and a reason to turn his life around.', 85),
]

items = { item.id: item for item in _items_source_list }
