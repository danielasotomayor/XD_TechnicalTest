import pandas as p
import requests as r

url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
response = r.get(url)

if response.status_code == 200:
    data = response.json()
    print("Datos obtenidos")
else:
    print("Error:", response.status_code)

df = p.DataFrame(data['items'])

# 2. Cantidad de preguntas respondidas y no respondidas
total_records = len(df)
print("\nTotal de respuestas:", total_records)
answered_count = df[df['is_answered'] == True].shape[0]
unanswered_count = df[df['is_answered'] == False].shape[0]
print("Cantidad de preguntas respondidas:", answered_count)
print("Cantidad de preguntas no respondidas:", unanswered_count)


# 3. Respuesta con menor número de vistas
min_view_row = df.loc[df['view_count'].idxmin()]
print("\nRespuesta con la menor cantidad de vistas:")
print(min_view_row)
print("Número de vistas:",min_view_row['view_count'])

# 4. Respuesta más antigua y más nueva por creation_date
oldest_answer = df.loc[df['creation_date'].idxmin()]
newest_answer = df.loc[df['creation_date'].idxmax()]

print("\nRespuesta más antigua:")
print("Título:", oldest_answer['title'])
print("Fecha de creación:", oldest_answer['creation_date'])

print("Respuesta más nueva:")
print("Título:", newest_answer['title'])
print("Fecha de creación:", newest_answer['creation_date'])

# 5. Respuesta con mayor reputación
df['reputation'] = df['owner'].apply(lambda x: x['reputation'])
max_reputation_owner = df.loc[df['reputation'].idxmax()]
print("\nRespuesta con mayor reputación:")
print("Título:", max_reputation_owner['title'])
print("Reputación del propietario:", max_reputation_owner['reputation'])
