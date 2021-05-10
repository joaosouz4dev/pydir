CREATE DATABASE `bd_estudos` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
use bd_estudos;
DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` char(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `idade` int(11) DEFAULT NULL,
  `endereco` char(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `salario` decimal(18,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'Flavio',24,'Rua das palmeras 375 Centro Betim - MG',4254.20),(2,'Gustavo',28,'Rua das Esmerinda 85 Centro Betim - MG',4180.33),(3,'Peralta',32,'AV das america 1245 Centro BH - MG',7596.22),(4,'Pablo',19,'Rua Olinda 236 Chacara Contagem - MG',1685.00),(5,'Luiz',22,'Rua palmares Bom retiro Betim - MG',2120.33),(6,'Tatiana',26,'Rua das Oliveiras Centro Betim - MG',3965.96),(7,'Fernanda',30,'AV dos andradas 2485 Centro BH - MG',6293.14),(8,'Olivia',28,'Rua dos catatau Betim - MG',4624.74),(9,'Valeria',33,'Rua das Dores - Brasil',2458.22);
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;
SELECT 
    CONCAT(fun1.nome,
            ' ',
            (SELECT 
                    fun2.nome
                FROM
                    funcionarios fun2
                WHERE
                    fun2.salario < fun1.salario
                ORDER BY fun2.salario DESC
                LIMIT 1)) AS 'LISTA'
FROM
    funcionarios fun1
ORDER BY fun1.salario DESC;