alter table cliente add column cidade_id integer not null;
alter table cliente add constraint fk_cidade_cliente foreign key(cidade_id) references cidade(id);
