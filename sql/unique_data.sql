INSERT INTO schedule_of_broadcasts(note)
    VALUES ("dsgsdg");

INSERT INTO topics(title, note)
    VALUES ("dsfdsf", "fsfds");

INSERT INTO tv_channels(title, abbreviated_title)
    VALUES ("asf", "fasf");

INSERT INTO tv_channel_broadcasts(tv_channel_id, topic_id, time_id, venue, title)
    VALUES (1, 1, 1, "At home", "Dom_2");

INSERT INTO time_broadcasts(schedule_id, time_o_clock)
    VALUES (1, "2022-07-01 19:00:00");

INSERT INTO positions(post)
    VALUES ("Director");

INSERT INTO staff(position_id, named, surname, date_birth)
    VALUES (1, "Vadim", "Pismenskiy", "2022-07-01 18:00:00");

INSERT INTO equipment(equipment)
    VALUES ("Kak");

INSERT INTO names_sets_of_equipment(name_of_equipment_set)
    VALUES ("For uzhasi");
