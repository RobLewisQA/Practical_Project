CREATE TABLE IF NOT EXISTS entrants
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          num1 VARCHAR(30) NOT NULL,
                          num2  VARCHAR(30) NOT NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `entrants` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `entrants` VALUES (1,'12','34'),(2,'13','23'),(3,'34','65');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
