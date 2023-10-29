-- Выбрать самые дешёвые товары, стоимость которых меньше 1500
SELECT name, price
FROM shop.carpet
WHERE price < 1500
  AND amount > 1
ORDER BY name;


-- Выбрать производителей, у которых покупаются более 1 вида ковров
SELECT carpet.producer_id,
       p.name,
       p.country,
       count(carpet_id) AS carpet_number
FROM shop.carpet
         INNER JOIN shop.producer p
                    ON carpet.producer_id = p.producer_id
GROUP BY carpet.producer_id, p.name, p.country
HAVING count(carpet_id) > 1;


-- Установить соответствие между коврами и категориями,
-- пронумеровав категории
SELECT name,
       category,
       dense_rank() OVER (ORDER BY category) AS category_num
FROM shop.carpet
         INNER JOIN shop.carpet_description c
                    ON carpet.carpet_id = c.carpet_id;


-- Посчитать число ковров в зависимости от цвета
SELECT name,
       colour,
       count(c.carpet_id) OVER (PARTITION BY c.colour) AS colour_count
FROM shop.carpet
         INNER JOIN shop.carpet_description c
                    ON carpet.carpet_id = c.carpet_id;

-- Сравнение цен в каждой категории с минимальной
SELECT name,
       category,
       price,
       first_value(price)
       OVER (PARTITION BY category
           ORDER BY price)
           AS min_category_price
FROM shop.carpet
         INNER JOIN shop.carpet_description c
                    ON carpet.carpet_id = c.carpet_id;


-- Соответствие между наименованием ковра и местом и временем его доставки
SELECT name, address, date_from, date_to
FROM shop.carpet
         INNER JOIN shop.carpet_supply cs
                    ON carpet.carpet_id = cs.carpet_id
         INNER JOIN shop.supply s
                    ON cs.supply_id = s.supply_id
ORDER BY date_from;
