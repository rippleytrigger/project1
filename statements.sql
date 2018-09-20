CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    address_id VARCHAR UNIQUE NOT NULL,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    CONSTRAINT addresses FOREIGN KEY (address_id)
);

/*CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    role VARCHAR(16) NOT NULL UNIQUE
)*/

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    ISBN_number VARCHAR UNIQUE NOT NULL,
    title VARCHAR UNIQUE NOT NULL,
    author VARCHAR NOT NULL,
    publication_year DATE NOT NULL
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    review_count INTEGER NOT NULL, 
    average_score INTEGER NOT NULL,
    CHECK (average_score<=5),
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (book_id) REFERENCES books (id)
);


CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    address1  VARCHAR(120) NOT NULL,
    address2  VARCHAR(120),
    country VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    postal_code VARCHAR(16) NOT NULL
);