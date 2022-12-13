CREATE DATABASE IF NOT EXISTS `hhctf`;

USE `hhctf`;

CREATE TABLE IF NOT EXISTS `users7693` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `movies` (
    `id` int(11) NOT NULL,
    `name` varchar(255) NOT NULL,
    `year` int(11) NOT NULL,
    `director` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
);

INSERT INTO `users7693` (`username`,`password`) VALUES ('admin','sup3r_S3Cur3_p4SSword');

INSERT INTO `movies` (`id`,`name`,`year`,`director`) VALUES (1,'Harry Potter and the Philosopher Stone',2001,'Chris Colombus');
INSERT INTO `movies` (`id`,`name`,`year`,`director`) VALUES (2,'Harry Potter and the Chamber of Secrets',2002,'Chris Colombus');
INSERT INTO `movies` (`id`,`name`,`year`,`director`) VALUES (3,'Harry Potter and the Prisoner of Azkaban',2004,'Alfonso Cuarón');
INSERT INTO `movies` (`id`,`name`,`year`,`director`) VALUES (4,'Harry Potter and the Goblet of Fire',2005,'Mike Newell');
INSERT INTO `movies` (`id`,`name`,`year`,`director`) VALUES (5,'Harry Potter and the Order of the Phoenix',2007,'Michael Goldenberg');
INSERT INTO `movies` (`id`,`name`,`year`,`director`) VALUES (6,'Harry Potter and the Half-Blood Prince',2009,'David Yates');
INSERT INTO `movies` (`id`,`name`,`year`,`director`) VALUES (7,'Harry Potter and the Deathly Hallows – Part 1',2010,'David Yates');
INSERT INTO `movies` (`id`,`name`,`year`,`director`) VALUES (8,'Harry Potter and the Deathly Hallows – Part 2',2011,'David Yates');


CREATE USER IF NOT EXISTS 'flask'@'%' IDENTIFIED BY 'b762596d25ea8c5f';

GRANT SELECT ON `hhctf`.* TO 'flask'@'%';

FLUSH PRIVILEGES;