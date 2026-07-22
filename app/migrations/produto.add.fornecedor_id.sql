alter table PRODUTO 
add column fornecedor_id integer not null;

alter table produto
add constraint fk_produto_fornecedor
foreign key (fornecedor_id) 
references fornecedor(id);