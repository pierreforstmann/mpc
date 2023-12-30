--
-- create.sql
--
-- create schema objects in bugs database
--
drop table if exists bugs;
create table bugs(
       bugref text,
       msgcount int,
       msgdate text,
       msgid text);
--
.schema
--
.quit 