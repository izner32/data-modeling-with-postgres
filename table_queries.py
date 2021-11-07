# drop table if they exist - so we're sure we are creating fresh table
songplays_fact_drop = "DROP TABLE IF EXISTS songplays"
users_dimension_drop = "DROP TABLE IF EXISTS users"
songs_dimension_drop = "DROP TABLE IF EXISTS songs"
time_dimension_drop = "DROP TABLE IF EXISTS time"
artist_dimension_drop = "DROP TABLE IF EXISTS artists"

# create table queries
songplays_fact_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time TIMESTAMP,
        user_id INTEGER,
        level VARCHAR(10),
        song_id VARCHAR(20),
        artist_id VARCHAR(20),
        session_id INTEGER,
        location VARCHAR(50),
        user_agent VARCHAR(150)
    ); 
""")

users_dimension_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        gender CHAR(1),
        level VARCHAR(10)
    ); 
""")

songs_dimension_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR(20) PRIMARY KEY,
        title VARCHAR(100),
        artist_id VARCHAR(20) NOT NULL,
        year INTEGER,
        duration FLOAT(5)
    ); 
""")

time_dimension_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY,
        hour INTEGER,
        day INTEGER,
        week INTEGER,
        month INTEGER,
        year INTEGER,
        weekday INTEGER
    ); 
""")

artists_dimension_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_ID VARCHAR(20) PRIMARY KEY,
        name VARCHAR(100),
        location VARCHAR(100),
        latitude FLOAT(5),
        longitude FLOAT(5)
    );
""")

# insert values inside table queries
songplays_fact_insert = ("""
    INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT(songplay_id) DO NOTHING;
""")

users_dimension_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

songs_dimension_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT DO NOTHING;
""")

time_dimension_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s) 
    ON CONFLICT DO NOTHING;
""")

artists_dimension_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT DO NOTHING;
""")

drop_table_queries = [songplays_fact_drop,users_dimension_drop,songs_dimension_drop,time_dimension_drop,artist_dimension_drop]
create_table_queries = [songplays_fact_create,users_dimension_create,songs_dimension_create,time_dimension_create,artists_dimension_create]




