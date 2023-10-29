-- CREATE
INSERT INTO shop.supply
VALUES (8, '2022-04-10 15:25:33', '2022-04-11 12:58:37',
        'Novosibirskaya oblast, Novosibirsk, Vybornaya Ul., bld. 106, appt. 186');

INSERT INTO shop.carpet_supply
VALUES (4, 8);

-- READ
SELECT *, count(*)
FROM shop.carpet
WHERE price > 1000
GROUP BY carpet_id;

SELECT carpet_id, name, amount
FROM shop.carpet
WHERE amount > 100
GROUP BY carpet_id;

SELECT *
FROM shop.supply
ORDER BY date_from;


-- UPDATE
UPDATE shop.supply
SET address = 'Kostromskaya oblast, Kostroma, Severnoy Pravdy Ul., bld. 31, appt. 9'
WHERE supply_id = 3;

UPDATE shop.supply
SET date_to = '2022-04-03 09:31:10'
WHERE supply_id = 1;

UPDATE shop.carpet
SET amount = 517
WHERE carpet_id = 10;

-- DELETE
DELETE
FROM shop.carpet_supply
WHERE supply_id = 5;

DELETE
FROM shop.supply
WHERE supply_id = 5;