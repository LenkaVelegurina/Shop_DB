INSERT INTO shop.carpet
VALUES (1, 1, 'Кварц-виниловая LVT самоклеящаяся ПВХ плитка LAKO DECOR Делюкс', 883, 15),
       (2, 1, 'Плитка ПВХ LVT Tarkett New Age DryBack 230180012 AURA', 951, 33),
       (3, 2, 'Кварц-виниловый ламинат SPC Смарт Чойс Дуб Сильверсайд', 1849, 22),
       (4, 1, 'Грязезащитное противоскользящее покрытие Kolckmann GmbH AKO Safety Mat Антрацит', 3649, 98),
       (5, 3, 'Линолеум напольный на отрез TARKETT Sprint Pro Baden 3', 1210, 93),
       (6, 4, 'Ковролин на пол офисный Betap', 1341, 103),
       (7, 5, 'Коврики самоклеящиеся (ковролин/ковровая плитка)', 1427, 75),
       (8, 4, 'Ламинат кроношпан Loft 4376', 1287, 63),
       (9, 3, 'Искусственная трава, газон, Витебские ковры', 390, 58),
       (10, 3, 'Искусственная трава газон декоративная зелень для дома сада', 519, 616);

INSERT INTO shop.producer
VALUES (1, 'France carpets', 'France'),
       (2, 'Brigadir', 'Russia'),
       (3, 'Магазин искусственных цветов No.1', 'Russia'),
       (4, 'ИМ Групп', 'Russia'),
       (5, 'Remontnick.ru', 'Turkey');

INSERT INTO shop.supply
VALUES (1, '2022-04-03 08:30:00', '2022-04-03 18:30:00',
        'Rostovskaya oblast, Rostov-na-donu, Poselkovyy 1, bld. 1/Б'),
       (2, '2022-04-04 09:33:00', '2022-04-05 17:34:57',
        'Primorskiy kray, Vladivostok, Vatutina, bld. 26, appt. 95'),
       (3, '2022-04-04 19:33:28', '2022-04-05 13:32:58',
        'Saratovskaya oblast, Saratov, 2 Pionerskaya, bld. 30/36, appt. 118'),
       (4, '2022-04-06 21:25:25', '2022-04-07 15:07:02',
        'Vladimirskaya oblast, Vladimir, Suzdalskiy Prt., bld. 26, appt. 134'),
       (5, '2022-04-06 23:56:32', '2022-04-07 17:04:32',
        'Ivanovskaya oblast, Ivanovo, Remiznaya Ul., bld. 3, appt. 54'),
       (6, '2022-04-07 03:22:11', '2022-04-07 19:34:45',
        'Krasnodarskiy kray, Krasnodar, Gidrostroiteley, bld. 28, appt. 236'),
       (7, '2022-04-09 05:12:13', '2022-04-10 10:08:57',
        'Moskovskaya oblast, Moskva, Glagoleva Generala Ul., bld. 12/К. 1, appt. 80');

INSERT INTO shop.carpet_supply
VALUES (1, 1),
       (3, 2),
       (10, 3),
       (5, 4),
       (5, 5),
       (3, 6),
       (10, 7);


INSERT INTO shop.carpet_description
VALUES (1, 'Плитка ПВХ / LVT', 15, 10, 'brown'),
       (2, 'Плитка ПВХ / LVT', 50, 40, 'aura'),
       (3, 'Плитка ПВХ / LVT', 100, 10, 'white'),
       (4, 'Грязезащитные покрытия', 5, 10, 'black'),
       (5, 'Линолеум', 3, 6, 'grey'),
       (6, 'Ковролин на резиновой основе', 3, 10, 'grey'),
       (7, 'Ковролин для гостиниц', 3, 3, 'brown'),
       (8, 'Ламинат', 2, 4, 'pine'),
       (9, 'Искусственная трава', 1, 1, 'green'),
       (10, 'Искусственная трава', 1, 1, 'green');
