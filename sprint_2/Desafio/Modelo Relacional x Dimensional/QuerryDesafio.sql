-- ##MODELO RELACIONAL##

CREATE TABLE Clientes (
    ClienteID INTEGER PRIMARY KEY,
    NomeCliente TEXT NOT NULL,
    Cidade TEXT NOT NULL,
    Estado TEXT NOT NULL,
    País TEXT NOT NULL
);
CREATE TABLE Veículos (
    CarroID INTEGER PRIMARY KEY,
    CombustivelID INTEGER NOT NULL,
    KmCarro INTEGER NOT NULL,
    Chassi TEXT NOT NULL,
    Marca TEXT NOT NULL,
    Modelo TEXT NOT NULL,
    Ano INTEGER NOT NULL,
    FOREIGN KEY (CombustivelID) REFERENCES Combustivel (CombustivelID)
);

CREATE TABLE Combustivel (
    CombustivelID INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL
);

CREATE TABLE Vendedores (
    VendedorID INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Sexo SMALLINT NOT NULL,
    Estado TEXT NOT NULL
);

CREATE TABLE Locacoes (
    LocacaoID INTEGER PRIMARY KEY,
    ClienteID INTEGER NOT NULL,
    CarroID INTEGER NOT NULL,
    CombustivelID INTEGER NOT NULL,
    VendedorID INTEGER NOT NULL,
    DataInicio DATE NOT NULL,
    HoraInicio TIME NOT NULL,
    Diarias INTEGER NOT NULL,
    Valor REAL NOT NULL,
    DataFim DATE NOT NULL,
    HoraFim TIME NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes (ClienteID),
    FOREIGN KEY (CarroID) REFERENCES Veículos (CarroID),
    FOREIGN KEY (VendedorID) REFERENCES Vendedores (VendedorID),
    FOREIGN KEY (CombustivelID) REFERENCES Combustivel (CombustivelID)
);

insert into Clientes (ClienteID, NomeCliente, Cidade, Estado, País) VALUES
(2, 'Cliente dois', 'São Paulo', 'São Paulo', 'Brasil'),
(3, 'Cliente tres', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
(4, 'Cliente quatro', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
(5, 'Cliente cinco', 'Manaus', 'Amazonas', 'Brasil'),
(6, 'Cliente seis', 'Belo Horizonte', 'Minas Gerais', 'Brasil'),
(10, 'Cliente dez', 'Rio Branco', 'Acre', 'Brasil'),
(20, 'Cliente vinte', 'Macapá', 'Amapá', 'Brasil'),
(22, 'Cliente vinte e dois', 'Porto Alegre', 'Rio Grande do Sul', 'Brasil'),
(23, 'Cliente vinte e tres', 'Eusébio', 'Ceará', 'Brasil'),
(26, 'Cliente vinte e seis', 'Campo Grande', 'Mato Grosso do Sul', 'Brasil');

insert into Veículos (CarroID, CombustivelID, KmCarro, Chassi, Marca, Modelo, Ano) VALUES
(1, 3,  8500, 'AAAKNS8JS76S39', 'Toyota', 'Corolla XEI', 2023),
(2, 2, 40000, 'AKIUNS1JS76S39', 'Nissan', 'Versa', 2019),
(3, 1, 152800, 'DKSHKNS8JS76S39', 'VW', 'Fusca 78', 1978),
(4, 2, 58000, 'LLLUNS1JS76S39', 'Nissan', 'Versa', 2020),
(5, 4, 78000, 'MSLUNS1JS76S39', 'Nissan', 'Frontier', 2022),
(6, 1, 21800, 'SKIUNS8JS76S39', 'Nissan', 'Versa', 2019),
(7, 1, 212800, 'SSIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996),
(10, 1, 211800, 'LKIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996),
(98, 2, 29450, 'AKJHKN98JY76539', 'Fiat', 'Fiat Uno', 2000),
(99, 5, 21700, 'IKJHKN98JY76539', 'Fiat', 'Fiat Palio', 2010);

insert into Combustivel (CombustivelID, Nome) VALUES
(1,'Gasolina'),
(2,'Etanol'),
(3,'Flex'),
(4,'Diesel');

insert into Vendedores (VendedorID, Nome, Sexo, Estado) VALUES
(5, 'Vendedor cinco', 0, 'São Paulo'),
(6, 'Vendedora seis', 1, 'São Paulo'),
(7, 'Vendedora sete', 1, 'Rio de Janeiro'),
(8, 'Vendedora oito', 1, 'Minas Gerais'),
(16, 'Vendedor dezesseis', 0, 'Amazonas'),
(30, 'Vendedor trinta', 0, 'Rio Grande do Sul'),
(31, 'Vendedor trinta e um', 0, 'Ceará'),
(32, 'Vendedora trinta e dois', 1, 'Mato Grosso do Sul');

insert into Locacoes (LocacaoID, ClienteID, CarroID, CombustivelID, VendedorID, DataInicio, HoraInicio, Diarias, Valor, DataFim, HoraFim) VALUES
(1, 2, 98, 1, 5, '2015-01-10', '10:00', 2, 100.00, '2015-01-12', '10:00'),
(2, 2, 98, 1, 5, '2015-02-10', '12:00', 2, 100.00, '2015-02-12', '12:00'),
(3, 3, 99, 1, 6, '2015-02-13', '12:00', 2, 150.00, '2015-02-15', '12:00'),
(4, 4, 99, 1, 6, '2015-02-15', '13:00', 5, 150.00, '2015-02-20', '13:00'),
(5, 4, 99, 1, 7, '2015-03-02', '14:00', 5, 150.00, '2015-03-07', '14:00'),
(6, 6, 3, 1, 8, '2016-03-02', '14:00', 10, 250.00, '2016-03-12', '14:00'),
(7, 6, 3, 1, 8, '2016-08-02', '14:00', 10, 250.00, '2016-08-12', '14:00'),
(8, 4, 3, 1, 6, '2017-01-02', '18:00', 10, 250.00, '2017-01-12', '18:00'),
(9, 4, 3, 1, 6, '2018-01-02', '18:00', 10, 280.00, '2018-01-12', '18:00'),
(10, 10, 10, 1, 16, '2018-03-02', '18:00', 10, 50.00, '2018-03-12', '18:00'),
(11, 20, 7, 1, 16, '2018-04-01', '11:00', 10, 50.00, '2018-04-11', '11:00'),
(12, 20, 6, 1, 16, '2020-04-01', '11:00', 10, 150.00, '2020-04-11', '11:00'),
(13, 22, 2, 2, 30, '2022-05-01', '08:00', 20, 150.00, '2022-05-21', '18:00'),
(14, 22, 2, 2, 30, '2022-06-01', '08:00', 20, 150.00, '2022-06-21', '18:00'),
(15, 22, 2, 2, 30, '2022-07-01', '08:00', 20, 150.00, '2022-07-21', '18:00'),
(16, 22, 2, 2, 30, '2022-08-01', '08:00', 20, 150.00, '2022-07-21', '18:00'),
(17, 23, 4, 2, 31, '2022-09-01', '08:00', 20, 150.00, '2022-09-21', '18:00'),
(18, 23, 4, 2, 31, '2022-10-01', '08:00', 20, 150.00, '2022-10-21', '18:00'),
(19, 23, 4, 2, 31, '2022-11-01', '08:00', 20, 150.00, '2022-11-21', '18:00'),
(20, 5, 1, 3, 16, '2023-01-02', '18:00', 10, 880.00, '2023-01-12', '18:00'),
(21, 5, 1, 3, 16, '2023-01-15', '18:00', 10, 880.00, '2023-01-25', '18:00'),
(22, 26, 5, 4, 32, '2023-01-25', '08:00', 5, 600.00, '2023-01-30', '18:00'),
(23, 26, 5, 4, 32, '2023-01-31', '08:00', 5, 600.00, '2023-02-05', '18:00'),
(24, 26, 5, 4, 32, '2023-02-06', '08:00', 5, 600.00, '2023-02-11', '18:00'),
(25, 26, 5, 4, 32, '2023-02-12', '08:00', 5, 600.00, '2023-02-17', '18:00'),
(26, 26, 5, 4, 32, '2023-02-18', '08:00', 1, 600.00, '2023-02-19', '18:00');

-- MODELO DIMENSIONAL

create view fato_locacoes as
select Locacoes.ClienteID, Locacoes.CarroID, Locacoes.CombustivelID, Locacoes.VendedorID, Locacoes.DataInicio, Locacoes.HoraInicio,Locacoes.Diarias,Locacoes.Valor,Locacoes.DataFim,Locacoes.HoraFim
from Locacoes;

create view dim_cliente as
select  *
from Clientes

create view dim_veiculo as
select Veículos.CarroID, Veículos.KmCarro,Veículos.Chassi,Veículos.Marca,Veículos.Modelo,Veículos.Ano
from Veículos;

create view dim_vendedor as
select *
from Vendedores;

create view dim_combustivel as
select *
from Combustivel;










