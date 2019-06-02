import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='root', host='localhost', port=3306)

# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `jogoteca`;")
#conn.commit()

# descomente para criar o banco
# criar_tabelas = '''SET NAMES latin1;
#     CREATE DATABASE `jogoteca` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
#     USE `jogoteca`;
#     CREATE TABLE `jogo` (
#       `id` int(11) NOT NULL AUTO_INCREMENT,
#       `nome` varchar(50) COLLATE utf8_bin NOT NULL,
#       `categoria` varchar(40) COLLATE utf8_bin NOT NULL,
#       `console` varchar(20) NOT NULL,
#       `usuario_id` varchar(8) NOT NULL,
#       PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
#     CREATE TABLE `usuario` (
#       `id` varchar(8) COLLATE utf8_bin NOT NULL,
#       `nome` varchar(20) COLLATE utf8_bin NOT NULL,
#       `senha` varchar(8) COLLATE utf8_bin NOT NULL,
#       PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''
#
# conn.cursor().execute(criar_tabelas)

# conn.commit()
