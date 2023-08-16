CREATE TABLE IF NOT EXISTS events (
id integer primary key autoincrement, 
title varchar(20), 
start_date date, 
start_time time, 
end_date date, 
end_time time, 
notes varchar, 
category varchar(20));
