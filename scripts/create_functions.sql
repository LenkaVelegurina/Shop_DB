CREATE OR REPLACE FUNCTION shop.get_carpet_info(p_carpet_id INTEGER)
    RETURNS TABLE
            (
                carpet_id     INTEGER,
                name          VARCHAR(256),
                price         INTEGER,
                amount        INTEGER,
                producer_name VARCHAR(256),
                category      VARCHAR(256),
                length        INTEGER,
                width         INTEGER,
                colour        VARCHAR(256)
            )
AS
$$
BEGIN
    RETURN QUERY
        SELECT c.carpet_id,
               c.name,
               c.price,
               c.amount,
               p.name AS producer_name,
               cd.category,
               cd.length,
               cd.width,
               cd.colour
        FROM shop.carpet AS c
                 JOIN shop.producer AS p
                      ON c.producer_id = p.producer_id
                 JOIN shop.carpet_description AS cd
                      ON c.carpet_id = cd.carpet_id
        WHERE c.carpet_id = p_carpet_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION shop.get_total_carpet_amount()
    RETURNS INTEGER AS
$$
BEGIN
    RETURN (SELECT sum(amount)
            FROM shop.carpet);
END;
$$ LANGUAGE plpgsql;
