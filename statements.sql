CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE country (
    id SERIAL PRIMARY KEY,
    country VARCHAR NOT NULL,
    postal-code INT(4) NOT NULL
);