-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

CREATE TRIGGER email_validate
AFTER INSERT ON users
FOR EACH ROW
	SET @valid_email = IF(NEW.email <> OLD.email, 0, 1);
