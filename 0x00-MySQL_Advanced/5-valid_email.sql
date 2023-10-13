-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

DROP TRIGGER IF EXISTS email_validate;
CREATE TRIGGER email_validate
BEFORE UPDATE ON users
FOR EACH ROW
	SET NEW.valid_email = IF(NEW.email <> OLD.email, 0, NEW.valid_email);
