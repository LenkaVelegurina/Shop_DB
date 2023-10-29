CREATE INDEX idx_carpet_producer_id
    ON shop.carpet (producer_id);

CREATE INDEX idx_producer_country
    ON shop.producer (country);

CREATE INDEX idx_supply_date_from
    ON shop.supply (date_from);

CREATE INDEX idx_carpet_description_category
    ON shop.carpet_description (category);

CREATE INDEX idx_carpet_supply_carpet_id_supply_id
    ON shop.carpet_supply (carpet_id, supply_id);