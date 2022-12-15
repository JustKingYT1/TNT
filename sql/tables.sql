CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY UNIQUE,
    staff_id INTEGER NOT NULL UNIQUE,
    login VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    FOREIGN KEY (staff_id)
        REFERENCES staff(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS positions(
    id INTEGER PRIMARY KEY UNIQUE,
    post VARCHAR(50) UNIQUE);

CREATE TABLE IF NOT EXISTS staff(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position_id INTEGER NOT NULL,
    user_id INTEGER UNIQUE,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    date_birth VARCHAR(50) NOT NULL,
    deleted BOOLEAN NOT NULL,
    FOREIGN KEY(position_id)
        REFERENCES positions(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS tv_channels(
    id INTEGER PRIMARY KEY UNIQUE,
    title VARCHAR(50) NOT NULL UNIQUE,
    abbreviated_title VARCHAR(10) UNIQUE);

CREATE TABLE IF NOT EXISTS topics(
    id INTEGER PRIMARY KEY UNIQUE,
    title VARCHAR(50) NOT NULL UNIQUE,
    note VARCHAR(255));

CREATE TABLE IF NOT EXISTS schedule_of_shows_id(
    id INTEGER PRIMARY KEY UNIQUE,
    tv_channel_id INTEGER NOT NULL,
    note VARCHAR(255),
    FOREIGN KEY(tv_channel_id)
        REFERENCES tv_channels(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS schedule_of_shows(
    id INTEGER PRIMARY KEY,
    schedule_id INTEGER NOT NULL,
    show_id INTEGER NOT NULL,
    time_id INTEGER NOT NULL,
    FOREIGN KEY (schedule_id)
        REFERENCES schedule_of_shows_id(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (show_id)
        REFERENCES tv_channel_shows(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (time_id)
        REFERENCES shows_time(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS shows_time(
    id INTEGER PRIMARY KEY UNIQUE,
    time_o_clock VARCHAR(20) NOT NULL UNIQUE);

CREATE TABLE IF NOT EXISTS tv_channel_shows(
    id INTEGER PRIMARY KEY UNIQUE,
    tv_channel_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    schedule_id INTEGER NOT NULL,
    equipment_set_id INTEGER NOT NULL,
    venue VARCHAR(100),
    title VARCHAR(50) UNIQUE,
    FOREIGN KEY(schedule_id)
        REFERENCES schedule_of_shows_id(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(tv_channel_id)
        REFERENCES tv_channels(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(topic_id)
        REFERENCES topics(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(equipment_set_id)
        REFERENCES names_sets_of_equipment(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS show_staff(
    id INTEGER PRIMARY KEY,
    tv_show_id INTEGER NOT NULL,
    personnel_id INTEGER NOT NULL,
    FOREIGN KEY(tv_show_id)
        REFERENCES tv_channel_broadcasts(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(personnel_id)
        REFERENCES staff(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS names_sets_of_equipment(
    id INTEGER PRIMARY KEY UNIQUE,
    name_of_equipment_set VARCHAR(100) NOT NULL UNIQUE);

CREATE TABLE IF NOT EXISTS equipment(
    id INTEGER PRIMARY KEY UNIQUE,
    equipment VARCHAR(100) NOT NULL UNIQUE);

CREATE TABLE IF NOT EXISTS equipment_sets(
    id INTEGER PRIMARY KEY UNIQUE,
    name_equipment_set_id INTEGER NOT NULL,
    equipment_id INTEGER NOT NULL,
    FOREIGN KEY(name_equipment_set_id)
        REFERENCES names_sets_of_equipment(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(equipment_id)
        REFERENCES equipment(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);
