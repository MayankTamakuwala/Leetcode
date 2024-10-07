SELECT MAX(score)- MIN(score) as difference_in_score FROM (
    SELECT assignment1, assignment2, assignment3, (assignment1+assignment2+assignment3) as score FROM Scores
) as total_scores