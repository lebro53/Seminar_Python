honey_song = input('Введите текст песни Михаила Горшенева. Слова во фразе разделяются дефисами. Фразы пробелами: ')
song_list = [i.replace('-', '') for i in honey_song.split(' ')]
abc = 'ауоыиэяюёе'
cnt = 0
rhythm_list = []
for j in song_list:
    for i in range(len(abc)):
        cnt += j.count(abc[i])
    rhythm_list.append(cnt)
    cnt = 0
rhythm_list.sort()
print('Парам-пам-пам') if rhythm_list[0] == rhythm_list[len(rhythm_list)-1] else print('Пам парам')
print(rhythm_list)