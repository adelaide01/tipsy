create table Users (
    user_id INTEGER PRIMARY KEY,
    email VARCHAR(64),
    password VARCHAR(64),
    user_name VARCHAR(64)
);
create table Tasks (
    task_id INTEGER PRIMARY KEY,
    title VARCHAR(64),
    created_at DATETIME,
    completed_at DATETIME,
    task_user_id VARCHAR(15)
);