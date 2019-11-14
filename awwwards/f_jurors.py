f_names = [elt.strip() for elt in open("femaleNames.txt", "r").readlines()]

jurors = ['Charles', 'Edwin', 'Felipe', 'Gabriel', 'Georgios', 'Goksel', 'Irene', 'Lea', 'Loïc', 'Mark', 'Nuno', 'CreativePeople', 'Trent', 'Lee', 'Brian', 'Rosa', 'Juan', 'Tomáš', 'Rodesk', 'Paulo', 'Edwin', 'Haraldur', 'Marcus', 'Brian', 'Creative', 'Alexey', 'Jacob', 'Damian', 'ivan', 'Klippoglim', 'Gonzalo', 'Vadim', 'David', 'brushgunz', 'Ines', 'Mathias', 'Aaron', 'Leandro', 'Helio', 'Addy', 'Antón', 'Rolf', 'Jack', 'Zack', 'Stevijn', 'Davy', 'Fernando', 'Julien', 'Richard', 'Jürgen', 'Charlie', 'Du', 'Sebastiano', 'Olga', 'Michael', 'Jessica', 'Paul', 'Aarron', 'John', 'Luke', 'Stéphane', 'Emilie', 'Anthony', 'Bastien', 'Kuba', 'Joe', 'Fred', 'Ralf', 'Neal', 'Guilherme', 'Xavier', 'Alexander', 'Bruno', 'Pablo', 'Kamil', 'Jeremie', 'Michael', 'Marie', 'Gilles', 'Matthieu', 'Arthur', 'Dario', 'Valentin', 'Chris', 'Agencia', 'Anthony', 'Antonio', 'Ido', 'Bulent', 'Fabio', 'Israel', 'Jay', 'JB', 'Jeff', 'Mark', 'Sean', 'Shyam', 'Simon', 'Vicki', 'Aravind', 'Robert', 'David', 'Juan', 'Tom', 'Rich', 'Ahmad', 'Manoela', 'Juan', 'Blackmoon', 'Jean-Maxime', 'Mert', 'James', 'Fabio', 'Kenta', 'Shawn', 'Claudio', 'Franc', 'Arek', 'Carlos', 'Bjarne', 'Abigail', 'Brave', 'Robby', 'Kiran', 'John', 'Thomas', 'Izaias', 'Luca', 'Andreas', 'Malte', 'Bartek', 'Aaron', 'Jonathan', 'Benoit', 'Filippo', 'Derek', 'Luke', 'Andy', 'James', 'Joris', 'Nathan', 'Mathias', 'Michi', 'Iris', 'Denise', 'Michal', 'Eran', 'Vanessa', 'Aude', 'Michele', 'Francesco', 'Alice', 'Miguel', 'Geovanny', 'Nemanja', 'Serkan', 'Jack', 'Jacob', 'Gregg', 'Michael', 'Marc', 'Sue', 'Matthew', 'Sylvain', 'Jon', 'Roman', 'Diego', 'Igor', 'Luisa', 'Samuel', 'Arne', 'Gláuber', 'Piotr', 'Baptiste', 'Joakim', 'Klaus-Martin', 'Julia', 'Dmitry', 'Mustafa', 'Peter', 'Alessandro', 'Oui', 'Julie', 'Priscilla', 'Thieb', 'Alessandro', 'Antwan', 'Maxime', 'Robert', 'Hannah', 'Eyal', 'Marco', 'Marissa', 'Laura', 'Fabricio', 'Ryan', 'Leopat', 'inTacto', 'David', 'Emil', 'Gopal', 'Josh', 'Joshua', 'Kevin', 'Mark', 'Paul', 'Raffael', 'Ray', 'Rob', 'Ivan', 'Patrick', 'Marcus', 'Matt', 'Ness', '60fps', 'Basile', 'Lee', 'Lukas', 'Cristian', 'Awwwards', 'Sarri', 'Lucas', 'Jonas', 'Wesley', 'Sun', 'Uli', 'Jakob', 'Colin', 'Murat', 'Gary', 'Gabriel', 'Rachel', 'Javier', 'Aidan', 'Bryan', 'Stephanie', 'Yaprak', 'Daan', 'Sam', 'Antoine', 'Clément', 'Lionel', 'Daniel', 'Harry', 'George', 'Barny', 'Marek', 'Kosmas', 'Jordi', 'Hrvoje', 'Lukasz', 'Franco', 'Trouble', 'Paul', 'Isaac', 'Vito', 'Douglas', 'Christin', 'Peter', 'Greg', 'Burak', 'Henrik', 'Thomas', 'Bruno', 'Rob', 'Pascal', 'Rosie', 'Charles', 'Martijn', 'Xuan', 'Roland', 'Rob', 'Nicolas', 'Sunny', 'Alexis', 'keeley', 'Louis', 'Miro', 'Corentin', 'Fabian', 'Iván', 'Julie', 'Roman', 'Alex', 'Carl', 'David', 'Dries', 'Irena', 'Kevin', 'Mike', 'Óscar', 'Sebastian', 'Stefano', 'Wing', 'Rally', 'Damian', 'Paul', 'Henry', 'Le', 'Sang', 'TRÜF', 'Alexander', 'Aravind', 'Paul', 'Mike', 'Alfredo', 'Simon', 'Nick', 'DOMANI', 'Daniel', 'Corey', 'Julio', 'Matthias', 'Simon', 'Ulises', 'Elegant', 'Brian', 'Peter', 'Tomomi', 'Dave', 'Matija', 'Monika', 'Sean', 'Steve', 'Peter', 'Paul', 'Ronny', 'Fadi', 'Héctor', 'Charlie', 'Luciano', 'Julian', 'Blake', 'Aral', 'Brad', 'Enea', 'Matteo', 'Pedro', 'Melanie', 'Aleksandr', 'Dorian', 'Timothy', 'Grzegorz', 'Sebastian', 'Matt', 'Mark', 'Matthias', 'Soren', 'Kenneth', 'Brendan', 'Garth', 'Louis', 'Tsukasa', 'Imran', 'Ronaldo', 'Julien', 'Lissy', 'Alex', 'Tore', 'Alessio', 'Frédéric', 'Samuel', 'Julio', 'Arnaud', 'Art', 'Ellie', 'Jonas', 'Shunsuke', 'Thales', 'Nicholas', 'Rinat', 'Ludmilla', 'Mustafa', 'Jenny', 'Brian', 'Drew', 'Florian', 'Jason', 'Kamil', 'Michael', 'Nikola', 'Pablo', 'Philip', 'Rehan', 'Romain', 'Shaz', 'Siddharth', 'Simon', 'Juanma', 'Tobias', 'Gustav', 'Alexander', 'Alexey', 'Umut', 'Emmanuel', 'Paul', 'Tom', 'Danilo', 'Umut', 'Mohit', 'Sarah', 'Rob', 'SNOOP', 'Trent', 'Alexandre', 'Kenji', 'Panagiotis', 'Karim', 'Keitaro', 'Tiago', 'Francesco', 'Brijan', 'David', 'Eric', 'Karl', 'Jorge', 'Kris', 'Michael', 'Jamie', 'Baptiste', 'Ariadne', 'Dan', 'Alejandro', 'Heiko', 'Bojan', 'Roel', 'Chryssa', 'Natalie', 'Michael', 'Rich', 'Magnus', 'Samuel', 'Pim', 'Ruben', 'Rick', 'Ambroise', 'Younus', 'Lu', 'Jeremy', 'Jean', 'Anton', 'Mira', 'Anastasia', 'Anatoliy', 'Filip', 'Hernan', 'Kai', 'Michał', 'Tommy', 'Luigi', 'Pablo', 'Petr', 'Warre', 'John', 'Andreas']

def percent_of(x,y):
    return(x * 100 / y)

counter = 0
f_jurors = []
all_jurors = len(jurors)

for name in f_names:
    if name in jurors:
        f_jurors.append(name)
        # print(name) # or not. Maybe make it an option after the fact?
        counter += 1

f_percentage = percent_of(len(f_jurors),len(jurors))
f_p = format(f_percentage, '.1f')

print(f"Aprroximately {counter} out of {all_jurors} jurors -- {f_p}% -- are female.")

