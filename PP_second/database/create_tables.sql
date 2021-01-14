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
    aid SERIAL NOT NULL,
    title VARCHAR NOT NULL,
    text VARCHAR NOT NULL,
    date VARCHAR NOT NULL,
    status VARCHAR NOT NULL,
    PRIMARY KEY(aid)
);

CREATE TABLE Uarticles(
    art_id SERIAL NOT NULL,
    us_id SERIAL NOT NULL,
    mod_id SERIAL NOT NULL,
    ed_text VARCHAR NOT NULL,
    ed_date VARCHAR NOT NULL,
    PRIMARY KEY(art_id)
);
