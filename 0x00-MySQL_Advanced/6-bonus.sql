-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER //
DROP PROCEDURE IF EXISTS ADDBonus;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE new_id INT;
	SELECT id INTO new_id FROM projects WHERE name = project_name;
	IF new_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET new_id = LAST_INSERT_ID();
	END IF;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, new_id, score);
END//

DELIMITER ;
