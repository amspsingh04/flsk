DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS POST;

CREATE TABLE USER(
    id integer primary key autoincrement,
    username text unique not null,
    password text not null
);

CREATE TABLE POST(
    id integer primary key autoincrement,
    author_id integer not null,
    created timestamp not null default current_timestamp,
    title text not null,
    body text not null,
    foreign key (author_id) references user(id)
)