-- 1 Function: search by pattern (part of name or phone)
CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    WHERE phonebook.name ILIKE '%' || pattern || '%' 
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- 2 Procedure: insert newcuser or update phone if user already exists
CREATE OR REPLACE PROCEDURE insert_or_update_user(username TEXT, userphone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = username) THEN
        UPDATE phonebook SET phone = userphone WHERE name = username;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (username, userphone);
    END IF;
END;
$$;


-- 3. Procedure: insert many users, return incorrect data
CREATE OR REPLACE PROCEDURE insert_many_users(
    IN names TEXT[],
    IN phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= array_length(names, 1) LOOP
        IF phones[i] ~ '^\d{11}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = names[i]) THEN
                UPDATE phonebook SET phone = phones[i] WHERE name = names[i];
            ELSE
                INSERT INTO phonebook(name, phone) VALUES (names[i], phones[i]);
            END IF;
        ELSE
            RAISE NOTICE 'Invalid: % - %', names[i], phones[i];
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;

-- 4 Function: get paginated results (limit, offset)
CREATE OR REPLACE FUNCTION paginate(limit_num INT, offset_num INT)
RETURNS TABLE(id INT, name VARCHAR(100), phone VARCHAR(100)) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    ORDER BY id
    LIMIT limit_num OFFSET offset_num;
END;
$$ LANGUAGE plpgsql;

-- 5 Procedure: delete user by name or phone
CREATE OR REPLACE PROCEDURE delete_user(target TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook WHERE name = target OR phone = target;
END;
$$;