DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
  UserId INTEGER PRIMARY KEY AUTOINCREMENT,
  Username TEXT UNIQUE NOT NULL,
  Password TEXT NOT NULL
);
