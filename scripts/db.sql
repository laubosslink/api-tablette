SQLite format 3   @                                                                     -�� �  �e�                                                                                                                                                                                                                                                                            �b�tablecommentcommentCREATE TABLE comment (
	id INTEGER NOT NULL, 
	content VARCHAR NOT NULL, 
	vote INTEGER, 
	date_creation DATETIME, 
	post_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(post_id) REFERENCES post (id)
)�8�StablepostpostCREATE TABLE post (
	id INTEGER NOT NULL, 
	title VARCHAR(255) NOT NULL, 
	content VARCHAR NOT NULL, 
	vote INTEGER, 
	date_creation DATETIME, 
	PRIMARY KEY (id)
)�0�CtableinfoinfoCREATE TABLE info (
	id INTEGER NOT NULL, 
	title VARCHAR(255) NOT NULL, 
	content VARCHAR NOT NULL, 
	vote INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (title)
)'; indexsqlite_autoindex_info_1info      � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          #helloWorld2test !helloWorldtest
   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      #helloWorld2!	helloWorld                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            