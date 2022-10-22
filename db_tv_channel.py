import sqlite3 as sql

connection = sql.connect('tv_channels.db')

table_staff = """
                CREATE TABLE IF NOT EXISTS staff
                    (
                    id INTEGER PRIMARY KEY UNIQUE,
                    position_id INTEGER NOT NULL,
                    named VARCHAR(20),
                    surname VARCHAR(30),
                    date_birth DATE,
                    FOREIGN KEY(position_id) 
                        REFERENCES positions(id)
                        ON DELETE SET NULL ON UPDATE NO ACTION
                    )
              """

table_positions = """
                    CREATE TABLE IF NOT EXISTS positions
                        (   
                            id INTEGER PRIMARY KEY UNIQUE,
                            post VARCHAR(50)
                        )
                  """

table_transfer_staff = """
                        CREATE TABLE IF NOT EXISTS transfer_staff
                            (
                                id INTEGER PRIMARY KEY,
                                TV_show_id INTEGER NOT NULL,
                                personnel_id INTEGER NOT NULL,
                                FOREIGN KEY(TV_show_id)
                                    REFERENCES tv_channel_broadcasts(id)
                                    ON DELETE SET NULL ON UPDATE NO ACTION
                            )
                        """

table_tv_channels = """
                    CREATE TABLE IF NOT EXISTS tv_channels
                        (
                            id INTEGER PRIMARY KEY UNIQUE,
                            title VARCHAR(50) NOT NULL UNIQUE,
                            abbreviated_title VARCHAR(10) UNIQUE
                        )
                   """

table_topics = """
               CREATE TABLE IF NOT EXISTS topics
                    (
                        id INTEGER PRIMARY KEY UNIQUE,
                        title VARCHAR(50) NOT NULL UNIQUE,
                        note VARCHAR(255)
                    )        
               """

table_tv_channel_broadcasts = """
                                CREATE TABLE IF NOT EXISTS tv_channel_broadcasts
                                    (
                                        id INTEGER PRIMARY KEY UNIQUE,
                                        tv_channel_id INTEGER NOT NULL,
                                        topic_id INTEGER NOT NULL,
                                        venue VARCHAR(100),
                                        title VARCHAR(50),
                                        FOREIGN KEY(tv_channel_id)
                                            REFERENCES tv_channels(id)
                                            ON DELETE SET NULL ON UPDATE NO ACTION
                                        FOREIGN KEY(topic_id)
                                            REFERENCES topics(id)
                                            ON DELETE SET NULL ON UPDATE NO ACTION
                                    )
                              """

table_schedule_of_broadcasts = """
                                CREATE TABLE IF NOT EXISTS schedule_of_broadcasts
                                    (
                                        id INTEGER PRIMARY KEY UNIQUE,
                                        tv_show_id INTEGER NOT NULL,
                                        date_and_time_of_the_event VARCHAR(255),
                                        note VARCHAR(255),
                                        FOREIGN KEY(tv_show_id)
                                            REFERENCES tv_channel_broadcasts(id)
                                            ON DELETE SET NULL ON UPDATE NO ACTION
                                    )
                               """

table_names_sets_of_equipment = """
                                 CREATE TABLE IF NOT EXISTS names_sets_of_equipment
                                     (
                                         id INTEGER PRIMARY KEY UNIQUE,
                                         name_of_equipment_set VARCHAR(100)
                                     )
                                """

table_equipment = """
                    CREATE TABLE IF NOT EXISTS equipment
                        (
                            id INTEGER PRIMARY KEY UNIQUE,
                            equipment VARCHAR(100)
                        )
                  """

table_equipment_sets = """
                      CREATE TABLE IF NOT EXISTS equipment_sets
                          (
                            id INTEGER PRIMARY KEY UNIQUE,
                            name_equipment_set_id INTEGER NOT NULL,
                            equipment_id INTEGER NOT NULL,
                            FOREIGN KEY(name_equipment_set_id)
                                REFERENCES names_sets_of_equipment(id)
                            FOREIGN KEY(equipment_id)
                                REFERENCES equipment(id)
                          )
                       """

table_transfer_sets_of_equipment = """
                                    CREATE TABLE IF NOT EXISTS transfer_sets_of_equipment
                                        (
                                            id INTEGER PRIMARY KEY UNIQUE,
                                            equipment_set_id INTEGER NOT NULL,
                                            tv_show_id INTEGER NOT NULL,
                                            FOREIGN KEY(equipment_set_id)
                                                REFERENCES equipment_sets(id)
                                            FOREIGN KEY(tv_show_id)
                                                REFERENCES tv_channel_broadcasts(id)
                                        )
                                   """

table_user_positions = """
                        CREATE TABLE IF NOT EXISTS user_positions
                            (
                                id INTEGER PRIMARY KEY UNIQUE,
                                title VARCHAR(100)
                            )
                       """

table_users = """
                CREATE TABLE IF NOT EXISTS users
                    (
                        id INTEGER PRIMARY KEY UNIQUE,
                        user_position_id INTEGER NOT NULL,
                        nickname VARCHAR(50),
                        password VARCHAR(100),
                        FOREIGN KEY(user_position_id)
                            REFERENCES user_positions(id)
                    )
              """

with connection:
    try:
        cursor = connection.cursor()
        cursor.execute(table_transfer_sets_of_equipment)
        cursor.execute('INSERT INTO staff(position_id, named, surname, date_birth) VALUES (3, "Vadim", "Pismenskiy", "2004-07-01")')
        cursor.execute(table_users)
        connection.commit()
    except sql.Error as ex:
        print(ex)
        connection.rollback()
    # finally:
    #     connection.close()
