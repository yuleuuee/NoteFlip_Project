-- ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'rabhav9861'; 



-- First Note That : only after creating a databse we create tables and add values 

-- 1) 'Notefilp_users;' database was created from the python code(create_db.py):

-- ( CREATE DATABASE Notefilp_users; )

CREATE DATABASE Notefilp_users;

USE Notefilp_users;

SELECT * FROM user;

SELECT * FROM note;

SELECT id as SN , data as "ALL NOTES OF USER_1"
FROM note
WHERE user_id =1;

