CREATE TABLE IF NOT EXISTS positions(
    id INTEGER PRIMARY KEY UNIQUE,
    post VARCHAR(50) UNIQUE);

CREATE TABLE IF NOT EXISTS staff(
    id INTEGER PRIMARY KEY UNIQUE,
    position_id INTEGER NOT NULL,
    named VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    date_birth DATE NOT NULL,
    FOREIGN KEY(position_id)
        REFERENCES positions(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS tv_channels(
    id INTEGER PRIMARY KEY UNIQUE,
    title VARCHAR(50) NOT NULL UNIQUE,
    abbreviated_title VARCHAR(10) UNIQUE);

CREATE TABLE IF NOT EXISTS schedule_of_broadcasts(
    id INTEGER PRIMARY KEY UNIQUE,
    note VARCHAR(255));

CREATE TABLE IF NOT EXISTS time_broadcasts(
    id INTEGER PRIMARY KEY UNIQUE,
    schedule_id INTEGER NOT NULL,
    time_o_clock DATE NOT NULL UNIQUE,
    FOREIGN KEY(schedule_id)
        REFERENCES schedule_of_broadcasts(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS topics(
    id INTEGER PRIMARY KEY UNIQUE,
    title VARCHAR(50) NOT NULL UNIQUE,
    note VARCHAR(255));

CREATE TABLE IF NOT EXISTS tv_channel_broadcasts(
    id INTEGER PRIMARY KEY UNIQUE,
    tv_channel_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    time_id INTEGER NOT NULL,
    venue VARCHAR(100),
    title VARCHAR(50) UNIQUE,
    FOREIGN KEY(tv_channel_id)
        REFERENCES tv_channels(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(topic_id)
        REFERENCES topics(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(time_id)
        REFERENCES time_broadcasts(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS transfer_staff(
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

CREATE TABLE IF NOT EXISTS transfer_sets_of_equipment(
    id INTEGER PRIMARY KEY UNIQUE,
    equipment_set_id INTEGER NOT NULL,
    tv_show_id INTEGER NOT NULL,
    FOREIGN KEY(equipment_set_id)
        REFERENCES equipment_sets(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(tv_show_id)
        REFERENCES tv_channel_broadcasts(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS user_positions(
    id INTEGER PRIMARY KEY UNIQUE,
    title VARCHAR(100));

CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY UNIQUE,
    user_position_id INTEGER NOT NULL,
    nickname VARCHAR(50),
    password VARCHAR(100),
    FOREIGN KEY(user_position_id)
        REFERENCES user_positions(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);
