-- SQL script that creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a student.

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE av_score FLOAT;
	SELECT AVG(score) INTO av_score
	FROM corrections WHERE user_id = user_id GROUP BY user_id;

	UPDATE users SET average_score = av_score WHERE id = user_id;
	
END//

DELIMITER ;
