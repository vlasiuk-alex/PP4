CREATE TABLE Users(
    id SERIAL NOT NULL,
    username VARCHAR NOT NULL,
    firstname VARCHAR NOT NULL,
    lastname VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    ustatus VARCHAR NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Articles(
    id SERIAL NOT NULL,
    title VARCHAR NOT NULL,
    text VARCHAR NOT NULL,
    korystuvach VARCHAR NOT NULL,
    status VARCHAR NOT NULL,
    complete BOOLEAN NOT NULL,
    PRIMARY KEY(id)
);