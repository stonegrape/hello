PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE flights (
id integer primary key autoincrement,
origin text not null,
destination text not null,
duration text not null
);
INSERT INTO flights VALUES(1,'New York','london','415');
INSERT INTO flights VALUES(2,'Shanghai','Paris','760');
INSERT INTO flights VALUES(3,'Istanbul','Tokyo','700');
INSERT INTO flights VALUES(4,'New York','Paris','435');
INSERT INTO flights VALUES(5,'Moscow','Paris','245');
INSERT INTO flights VALUES(6,'Lima','New York','455');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('flights',6);
COMMIT;
