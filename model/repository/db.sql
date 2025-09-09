INSERT INTO TASKS
(id_, title, start_time, description, priority)
VALUES
(1003, 'english', '1404-6-21', 'self study', 'mid');

SELECT *
FROM TASKS
WHERE id_ = 1003;

UPDATE TASKS
SET id_ = 1003,
    title = 'english',
    start_time = '1404-6-22',
    description = 'self study',
    priority = 'mid'
WHERE id_ = 1003;

DELETE FROM TASKS
WHERE id_ = 1002;

SELECT * FROM TASKS;

