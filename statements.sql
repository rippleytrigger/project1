CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles (role_id)
);

CREATE TABLE roles (
    role_id SERIAL PRIMARY KEY,
    role VARCHAR(16) NOT NULL UNIQUE
)

CREATE TABLE books (
    ISBN_number VARCHAR PRIMARY KEY NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    publication_year INTEGER NOT NULL
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    ISBN_number INTEGER NOT NULL,
    review_count INTEGER NOT NULL, 
    average_score INTEGER NOT NULL,
    CHECK (average_score<=5),
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (ISBN_number) REFERENCES books (ISBN_number)
);


CREATE TABLE addresses (
    user_id SERIAL PRIMARY KEY,
    address1  VARCHAR(120) NOT NULL,
    address2  VARCHAR(120),
    country VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    postal_code VARCHAR(16) NOT NULL
);