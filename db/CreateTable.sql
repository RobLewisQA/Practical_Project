CREATE TABLE IF NOT EXISTS users
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          first_name VARCHAR(30) NOT NULL,
                          last_name  VARCHAR(30) NOT NULL,
                          email      VARCHAR(150),
                          rand_number VARCHAR(150) NOT NULL,
                          win_lose VARCHAR(150) NOT NULL,
                          PRIMARY KEY (id),
                          UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Ben','Hesketh','test@test7.com','5','No'),(2,'Luke','Benson','test@test.com','4','No'),(3,'Matt','Hunt','test4@test.com','7','No');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
