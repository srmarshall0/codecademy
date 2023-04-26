-- initialize a new table for friends
CREATE TABLE friends(
  id INTEGER, 
  name TEXT, 
  birthday DATE
);

-- add new friends 
INSERT INTO friends(id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

-- add more friends 
INSERT INTO friends(id, name, birthday)
VALUES(2, 'Jenna Hoffstatter', '1997-12-03');

INSERT INTO friends(id, name, birthday)
VALUES(3, 'Maggie Meyer', '1999-07-02');

-- update a record
UPDATE friends
SET name = 'Storm'
WHERE id = 1;

-- add a column
ALTER TABLE friends
ADD COLUMN email TEXT;

-- update emails 
UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'jhoffstatter@wisc.edu'
WHERE id = 2;

UPDATE friends
SET email = 'memeyer3@wisc.edu'
WHERE id = 3;

-- remove storm, shes fictional
DELETE FROM friends
WHERE id IS 1;

-- print table 
SELECT * FROM friends