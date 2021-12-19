create table if not exists author (
    id integer primary key autoincrement not null,
    name text,
    born integer
);

create table if not exists author_died (
    id integer primary key autoincrement not null,
    died integer not null,
    author_id integer not null unique,
    foreign key(author_id) references author(id)
);

create table if not exists country (
    id integer primary key autoincrement not null,
    name text not null unique
);

create table if not exists category (
    id integer primary key autoincrement not null,
    name text
);

create table if not exists item (
    id integer primary key autoincrement not null,
    name text,
    creation_date integer,
    category_id integer references category(id)
);

create table if not exists author_country (
    id integer primary key autoincrement not null,
    country_id integer references country(id) not null,
    author_id integer references author(id) not null
);

create table if not exists author_item (
    id integer primary key autoincrement not null,
    author_id integer references author(id) not null,
    item_id integer references item(id) not null
);
