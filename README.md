# ljc_oj

A small oj made by ljc (used Chinese)

used my_sql(5.7) & python(2.7)

```
$ brew install mysql
or $ sudo apt-get install mysql-server

$ mysql.server start
or $ service mysql start

$ mysql.server stop
or $ service mysql stop

$ mysql -u root

mysql> GRANT ALL PRIVILEGES ON *.* TO root@localhost IDENTIFIED BY "_root_password_";

$ mysql -u root -p

mysql> create database ljc_oj character set utf8;

$ mysql -u root -p -A ljc_oj

mysql> create table users(id int not null primary key auto_increment,username varchar(40),password text)default charset=utf8;

mysql> insert into users(username,password)values("_username_","_password_");

mysql> create table problems(id int not null primary key auto_increment,`index` int not null,name varchar(100),casenum int not null default 0,tl int not null default 1000,ml int not null default 256,sub int not null default 0,ac int not null default 0)default charset=utf8;

mysql> create table submissions(id int not null primary key auto_increment,usernmae varchar(40) not null,pid int not null,lang int not null,length int not null,submittime datetime not null default CURRENT_TIMESTAMP,testcase int not null default 0,result text,msg text,time int not null default -1,memory int not null default -1)default charset=utf8;

mysql> create table judge_queue(id bigint not null primary key auto_increment,rid int not null)default charset=utf8;

mysql> create table status(rid int not null,memory int not null)default charset=utf8;

mysql> CREATE USER 'oj'@'localhost' IDENTIFIED BY '_oj_password_';

mysql> grant select on ljc_oj.* to oj@localhost identified by '_oj_password_';

mysql> grant insert on ljc_oj.submissions to oj@localhost identified by '_oj_password_';

mysql> grant insert on ljc_oj.judge_queue to 'oj'@'localhost' identified by '_oj_password_';

mysql> flush privileges;

$ sudo pip install mysql-python

$ cd judge

$ python judge.py

$ python server.py
```
