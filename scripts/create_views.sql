CREATE VIEW shop.supply_view AS
SELECT supply_id,
       date_from,
       date_to,
       substring(address, 1, position(',' IN address) - 1) || ', *******' AS address
FROM shop.supply
ORDER BY date_from;


CREATE VIEW shop.carpet_info_view AS
SELECT carpet_id,
       name,
       price
FROM shop.carpet
ORDER BY price;


CREATE VIEW shop.carpet_sales_by_producer AS
SELECT p.producer_id,
       p.name        AS producer_name,
       sum(c.amount) AS total_sales
FROM shop.carpet c
         JOIN shop.producer p
              ON c.producer_id = p.producer_id
GROUP BY p.producer_id,
         p.name
ORDER BY total_sales DESC;


CREATE VIEW shop.average_price_by_producer AS
SELECT producer.name,
       avg(carpet.price) AS average_price
FROM shop.carpet
         JOIN shop.producer
              ON carpet.producer_id = producer.producer_id
GROUP BY producer.name
ORDER BY average_price;


CREATE VIEW shop.carpet_amount_by_address AS
SELECT supply.address,
       count(carpet_supply.carpet_id) AS total_carpet
FROM shop.carpet_supply
         JOIN shop.supply
              ON carpet_supply.supply_id = supply.supply_id
GROUP BY supply.address
ORDER BY total_carpet DESC;


CREATE VIEW shop.carpet_sales_by_category AS
SELECT carpet_description.category,
       sum(carpet.amount) AS total_sold
FROM shop.carpet
         JOIN shop.carpet_description
              ON carpet.carpet_id = carpet_description.carpet_id
GROUP BY carpet_description.category
ORDER BY total_sold DESC;