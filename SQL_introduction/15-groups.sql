-- Lists the number of records with the same score in 'second_table' in SQL server.
-- Records are organized in descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;