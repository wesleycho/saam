create database lucehack;

create table sidebyside
(
id serial,
image_id int,
title character varying,
image_url character varying,
primary key (id)
);

create table zoom_highscores
(
id serial,
name character varying,
score int,
primary key (id)
);

insert into zoom_highscores
(name, score)
values ('Popcorn Breath', 531),
('A cat walking across a keyboard', 40),
('Potato brains', 2),
('Zorbo the Magnificent', 12),
('Dracula', 70)