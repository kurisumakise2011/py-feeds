-- DROP TABLE article_feed.users_articles;
-- DROP TABLE article_feed.users;
-- DROP TABLE article_feed.articles;

CREATE TABLE IF NOT EXISTS article_feed.users (
	user_id int auto_increment primary key,
    login varchar(255) not null unique,
    name varchar(255) not null,
	token varchar(1000) not null,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;

CREATE TABLE IF NOT EXISTS article_feed.articles (
	article_id int auto_increment primary key,
	title varchar(255) not null,
  created_at timestamp,
	description text,
	content text,
	fetched_at timestamp default current_timestamp,
	author varchar(512) default 'unknown',
	url varchar(256),
	index_keyword varchar(128) not null
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;

CREATE TABLE IF NOT EXISTS article_feed.users_articles (
	user_article_id int auto_increment primary key,
	user_id int not null,
	article_id int not null,
    foreign key (user_id) references users(user_id)
	on update restrict on delete cascade,
	foreign key (article_id) references articles(article_id)
   	on update restrict on delete cascade
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;



