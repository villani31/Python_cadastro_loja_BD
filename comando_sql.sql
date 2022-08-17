CREATE DATABASE loja_informatica
    DEFAULT CHARACTER SET = 'utf8mb4';

CREATE TABLE acesso (
    id_acesso INT PRIMARY KEY AUTO_INCREMENT,
    usuario_acesso VARCHAR(50) NOT NULL,
    senha_acesso VARCHAR(30) NOT NULL,
    id_pessoa INT NOT NULL
);

CREATE TABLE pessoas (
    id_pessoa INT PRIMARY KEY AUTO_INCREMENT,
    nome_pessoa VARCHAR(50) NOT NULL,
    id_perfil INT NOT NULL
);

CREATE TABLE perfis (
    id_perfil INT PRIMARY KEY AUTO_INCREMENT,
    nome_perfil VARCHAR(50)
);

CREATE TABLE produtos (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(50)
);

-- criando relacionamento entre as tabels
ALTER TABLE acesso ADD CONSTRAINT fk_id_pessoa 
    FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa)
    ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE pessoas ADD CONSTRAINT fk_id_perfil
    FOREIGN KEY (id_perfil) REFERENCES perfis (id_perfil)
    ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO perfis (nome_perfil) VALUES ('Administrador'), ('Vendedor');

-- reset index, iniciando a partir do 1 apos delete
--ALTER TABLE perfis AUTO_INCREMENT = 1;

INSERT INTO pessoas (nome_pessoa, id_perfil) VALUES ('Thiago', 1), ('Ana', 2);

INSERT INTO produtos (nome_produto) VALUES ('Mouse'), ('Teclado'), ('Processador');

SELECT * FROM produtos;

--valores unicos
ALTER TABLE produtos ADD CONSTRAINT valor_unico UNIQUE (nome_produto);

-- Adicionar usuario no banco
INSERT INTO acesso (usuario_acesso,senha_acesso,id_pessoa) VALUES ("Thiago","thiago",1);

SELECT usuario_acesso, senha_acesso FROM acesso WHERE usuario_acesso = 'Thiago' AND
    senha_acesso = 'thiago';

