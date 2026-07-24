create table cidade
(
	id integer not null auto_increment,
	nome varchar(50) not null,
	estado_id integer not null,
	primary key(id),
	constraint fk_estado_cidade foreign key(estado_id) references estado(id)
);