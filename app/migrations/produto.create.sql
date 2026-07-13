use mini_erp;

create table produto
(
	id integer not null auto_increment,
	nome varchar(50) not null,
	estoque integer not null,
	preco decimal(10,2) not null,
	primary key(id)
);