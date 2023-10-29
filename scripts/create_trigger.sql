CREATE OR REPLACE FUNCTION check_supply_dates() RETURNS TRIGGER AS
$$
BEGIN
    IF NEW.date_from >= NEW.date_to THEN
        RAISE EXCEPTION 'Supply start date must be earlier than end date';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_supply_dates
    BEFORE INSERT OR UPDATE
    ON shop.supply
    FOR EACH ROW
EXECUTE FUNCTION check_supply_dates();


CREATE OR REPLACE FUNCTION update_carpet_amount() RETURNS TRIGGER AS
$$
BEGIN
    UPDATE shop.carpet
    SET amount = amount - 1
    WHERE carpet_id = NEW.carpet_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_carpet_amount
    AFTER INSERT
    ON shop.carpet_supply
    FOR EACH ROW
EXECUTE FUNCTION update_carpet_amount();


CREATE OR REPLACE FUNCTION check_producer_exists() RETURNS TRIGGER AS
$$
BEGIN
    IF NOT EXISTS(SELECT 1
                  FROM shop.producer
                  WHERE producer_id = NEW.producer_id)
    THEN
        RAISE EXCEPTION 'Producer with ID % does not exist', NEW.producer_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_producer_exists
    BEFORE INSERT OR UPDATE
    ON shop.carpet
    FOR EACH ROW
EXECUTE FUNCTION check_producer_exists();