f_names = [elt.strip() for elt in open("femaleNames.txt", "r").readlines()]

artists = ['Brendan', 'Charles', 'David', 'Ellie', 'Eric', 'Erica', 'Eva', 'Franco', 'Fight', 'Demand', 'Florence', 'Forensic', 'Future', 'Heather', 'Horst', 'IF', 'Ingo', 'Ingrid', 'Dan', 'Interaction', 'Goldsmiths', 'ITO', 'Jaime', 'James', 'John', 'Jonathan', 'Jonathan', 'Julian', 'Julie', 'Kamel', 'Kiln', 'Laura', 'Lev', 'Moritz', 'Lisa', 'Lise', 'Josh', 'mySociety', 'Nesta', 'Nicholas', 'Open', 'OpenCorporates', 'Owen', 'Paolo', 'Alessandro', 'Philipp', 'Rafael', 'Ryoji', 'Safecast', 'Salvatore', 'Oriana', 'Stefanie', 'Giorgia', 'Tekja', 'TeleGeography', 'The', 'The', 'Thomson', 'Craighead', 'Timo', 'Umbrellium', 'William', 'Zach']

def pc(x,y):
    return(x * 100 / y)

counter = 0
f_artists = []
all_artists = len(artists)

for name in f_names:
    if name in artists:
        f_artists.append(name)
        # print(name)
        counter += 1

f_percentage = pc(len(f_artists),len(artists))
f_p = format(f_percentage, '.1f')

print(f"{counter} out of {all_artists} artists -- {f_p}% -- are female.")

