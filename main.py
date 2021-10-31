import sqlalchemy
login = input('Внесение данных по музыкальному магазину в базу данных. \n Введите логин: ')
password = input('Введите пароль: ')
database = input('Введите название базы: ')
address = 'postgresql://' + login + ':' + password + '@localhost:5432/' + database
engine = sqlalchemy.create_engine(address)
connection = engine.connect()
s = {}
performers = connection.execute("""SELECT * FROM performers;
""").fetchmany(10)

with open(r'artist.txt', encoding='utf-8') as inf:
    for i in inf:
        d = i.split('*')
        added_data = f"""INSERT INTO public.performers (name_performers, description) values
        ({d[0]}, {d[1]})
"""
        connection.execute(added_data)

with open(r'genre.txt', encoding='utf-8') as inf:
    for i in inf:
        d = i.split('*')
        added_data = f"""INSERT INTO public.genre (title_genre, description) values
        ({d[0]}, {d[1]})
"""
        connection.execute(added_data)

with open(r'performers_ganre.txt', encoding='utf-8') as inf:
    for i in inf:
        d = i.split('*')
        added_data = f"""INSERT INTO public.performers_ganre (performers_id, genre_id) values
        ({d[0]}, {d[1]})
"""
        connection.execute(added_data)

with open(r'albums.txt', encoding='utf-8') as inf:
    for i in inf:
        d = i.split('*')
        added_data = f"""INSERT INTO public.albums (title_albums, year_of_release) values
        ({d[0]}, {d[1]})
"""
        connection.execute(added_data)

with open(r'collection.txt', encoding='utf-8') as inf:
    for i in inf:
        d = i.split('*')
        added_data = f"""INSERT INTO public.collection (title_collection, year_of_release) values
        ({d[0]}, {d[1]})
"""
        connection.execute(added_data)

with open(r'tracks.txt', encoding='utf-8') as inf:
    for i in inf:
        d = i.split('*')
        added_data = f"""INSERT INTO public.tracks (track_name, duration, albums_id) values
        ({d[0]}, {d[1]}, {d[2]})
"""
        connection.execute(added_data)

with open(r'performers_albums.txt', encoding='utf-8') as inf:
    for i in inf:
        d = i.split('*')
        added_data = f"""INSERT INTO public.performers_albums (performers_id, albums_id) values
        ({d[0]}, {d[1]})
"""
        connection.execute(added_data)

with open(r'collection_track.txt', encoding='utf-8') as inf:
    for i in inf:
        d = i.split('*')
        added_data = f"""INSERT INTO public.collection_track (collection_id, tracks_id) values
        ({d[0]}, {d[1]})
"""
        connection.execute(added_data)

print('Выполнено!')