m_names = [elt.strip() for elt in open('maleNames.txt', 'r').readlines()]

artists = ['Brendan', 'Charles', 'David', 'Ellie', 'Eric', 'Erica', 'Eva', 'Franco', 'Fight', 'Demand', 'Florence', 'Forensic', 'Future', 'Heather', 'Horst', 'IF', 'Ingo', 'Ingrid', 'Dan', 'Interaction', 'Goldsmiths', 'ITO', 'Jaime', 'James', 'John', 'Jonathan', 'Jonathan', 'Julian', 'Julie', 'Kamel', 'Kiln', 'Laura', 'Lev', 'Moritz', 'Lisa', 'Lise', 'Josh', 'mySociety', 'Nesta', 'Nicholas', 'Open', 'OpenCorporates', 'Owen', 'Paolo', 'Alessandro', 'Philipp', 'Rafael', 'Ryoji', 'Safecast', 'Salvatore', 'Oriana', 'Stefanie', 'Giorgia', 'Tekja', 'TeleGeography', 'The', 'The', 'Thomson', 'Craighead', 'Timo', 'Umbrellium', 'William', 'Zach']

def pc(x,y):
    return(x * 100 / y)

counter = 0
m_artists = []
all_artists = len(artists)


for artist in artists:
    if artist in m_names:
        m_artists.append(artist)
        print(artist)
        counter += 1

m_percentage = pc(len(m_artists),len(artists))
m_p = format(m_percentage, '.1f')



print(f"{counter} out of {all_artists} exhibitors -- {m_p}% -- are male.")


