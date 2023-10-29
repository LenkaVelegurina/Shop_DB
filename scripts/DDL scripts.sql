CREATE SCHEMA shop;

CREATE TABLE shop.carpet
(
    carpet_id   SERIAL PRIMARY KEY,
    producer_id SERIAL       NOT NULL,
    name        VARCHAR(256) NOT NULL,
    price       INTEGER CHECK (price > 0),
    amount      INTEGER CHECK (amount >= 0)
);

CREATE TABLE shop.producer
(
    producer_id SERIAL PRIMARY KEY,
    name        VARCHAR(256) NOT NULL,
    country     VARCHAR(256) NOT NULL
);

CREATE TABLE shop.supply
(
    supply_id SERIAL PRIMARY KEY,
    date_from DATE         NOT NULL,
    date_to   DATE         NOT NULL,
    address   VARCHAR(256) NOT NULL
);

CREATE TABLE shop.carpet_description
(
    carpet_id SERIAL PRIMARY KEY,
    category  VARCHAR(256) NOT NULL,
    length    INTEGER CHECK (length > 0),
    width     INTEGER CHECK (width > 0),
    colour    VARCHAR(256) NOT NULL
);

CREATE TABLE shop.carpet_supply
(
    carpet_id SERIAL NOT NULL,
    supply_id SERIAL NOT NULL,
    FOREIGN KEY (carpet_id) REFERENCES shop.carpet (carpet_id),
    FOREIGN KEY (supply_id) REFERENCES shop.supply (supply_id)
);
