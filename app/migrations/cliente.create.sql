create table cliente
(
	id integer not null auto_increment,
	nome varchar(50) not null ,
	data_nascimento date not null,
	limite_credito decimal(10,2),
	primary key(id)
);