f_names = [elt.strip() for elt in open("femaleNames.txt", "r").readlines()]

scholars = ['Paul', 'Neera', 'David', 'Charles', 'Peter', 'Donald', 'James', 'Bryan', 'Tyler', 'Christopher', 'Rachel', 'Veronique', 'Jerry', 'Michael', 'Jason', 'Jack', 'Robert', 'Daniel', 'Tim', 'Stefanie', 'Omar', 'Dustin', 'Emily', 'Seth', 'Antony', 'John', 'Abigail', 'Steven', 'Arnold', 'Brian', 'Robert', 'Chandran', 'Paul', 'Deirdre', 'Christina', 'Thomas', 'Adam', 'Johanna', 'Liya', 'David', 'Bobbi', 'Arielle', 'Noel', 'Garett', 'Daniel', 'Brian', 'Christopher', 'Mark', 'Peter', 'Jayme', 'Kevin', 'Christine', 'Patrick', 'Maurice', 'Stephen', 'Matthew', 'Eileen', 'John', 'Hester', 'Hilton', 'David', 'George', 'Vernon', 'Jason', 'Nona', 'Daniel', 'Chad', 'Richard', 'Walter', 'Claudia', 'Bruce', 'Brent', 'Solomon', 'Virgil', 'Thomas', 'Scott', 'Alexander', 'Adam', 'J.', 'Richard', 'Lawrence', 'Todd']

def pc(x,y):
    return(x * 100 / y)

counter = 0
f_scholars = []
all_scholars = len(scholars)

for name in f_names:
    if name in scholars:
        f_scholars.append(name)
        # print(name) # or not. Maybe make it an option after the fact?
        counter += 1

f_percentage = pc(len(f_scholars),len(scholars))
f_p = format(f_percentage, '.1f')

print(f"Aprroximately {counter} out of {all_scholars} scholars -- {f_p}% -- are female.")