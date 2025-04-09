CREATE DATABASE  IF NOT EXISTS `get_into_tech_c2_2025_v2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `get_into_tech_c2_2025_v2`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: get_into_tech_c2_2025_v2
-- ------------------------------------------------------
-- Server version	8.4.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `colour`
--

DROP TABLE IF EXISTS `colour`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colour` (
  `ColourID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  PRIMARY KEY (`ColourID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colour`
--

LOCK TABLES `colour` WRITE;
/*!40000 ALTER TABLE `colour` DISABLE KEYS */;
INSERT INTO `colour` VALUES (1,'Purple'),(2,'Green'),(3,'Grey'),(4,'Red'),(5,'Blue'),(6,'Orange'),(7,'Black'),(15,'Burgundy'),(16,'Silver');
/*!40000 ALTER TABLE `colour` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `PersonID` int NOT NULL AUTO_INCREMENT,
  `Firstname` varchar(50) NOT NULL,
  `Lastname` varchar(100) DEFAULT NULL,
  `ColourID` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `role` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`PersonID`),
  KEY `ColourID` (`ColourID`),
  CONSTRAINT `person_ibfk_1` FOREIGN KEY (`ColourID`) REFERENCES `colour` (`ColourID`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'Renee','Gujral',1,NULL,NULL),(2,'Fowsiya','Olow',2,NULL,NULL),(3,'Milena','Davudova',5,NULL,NULL),(4,'Chaitra','Boregowda',7,NULL,'user'),(5,'Aiman','Ahmed',3,NULL,NULL),(6,'Lisa','Simpson',1,NULL,NULL),(7,'Bart','Simpson',4,NULL,NULL),(8,'Maggie','Simpson',3,NULL,NULL),(9,'Fred','Flintstone',1,NULL,NULL),(10,'Wilma','Flintstone',2,NULL,NULL),(11,'Ned','Flanders',1,NULL,NULL),(12,'Lisa','Simpson',NULL,NULL,NULL),(13,'Fred','Flintstone',NULL,'FredFlin@gmail.com',NULL),(14,'Shine','Shetty',NULL,'Shineshetty@email.com',NULL),(15,'Lora','James',NULL,'LoraJames@gmail.com',NULL),(16,'Charan','Gowda',NULL,'CharanGowda@gmail.com',NULL),(17,'Miko','Raj',NULL,'Mikoraj@email.com',NULL),(18,'Pooja','M',NULL,'Pooja@gmail.com',NULL),(19,'admin_user','Tom',NULL,'admin@gmail.com','admin'),(20,'M','P',NULL,'Mp@email.com','user'),(21,'Mary','Priya',NULL,'Mary@gmail.com','user'),(22,'M','P',NULL,'Mp@email.com','user'),(23,'Jeo','Lancy',NULL,'Jeo@email.com','user'),(24,'Shine','Gowda',NULL,'Gowda@gmail.com','user'),(25,'Monica','A',NULL,'monica@gmail.com','user'),(26,'Shine','Shetty',NULL,'Shineshetty@email.com','user'),(27,'Shine','Shetty',NULL,'Shineshetty@email.com','user'),(28,'Shine','Shetty',NULL,'Shineshetty@email.com','user'),(29,'Chaitra','Boregowda',NULL,'chai@email.com','user'),(30,'V','Lancy',NULL,'lancy@gmail.com','admin'),(31,'Sheshank','G',NULL,'Gowda@gmail.com','User'),(32,'V','Aim',NULL,'aim@email.com','User'),(33,'Shine','Shetty',NULL,'Shineshetty@email.com','User');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE IF NOT EXISTS project (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    image_src VARCHAR(255)  -- This column stores the image filename or path
);

select * 
from project;

INSERT INTO project (name, description, image_src) 
VALUES 
('Team Website', 'A simple website built for our team with HTML, CSS, and Flask.', 'image_1.jpg'),
('Task Manager App', 'A web app to track tasks and assign responsibilities among team members.', 'project_1.jpg'),
('Team Chatbot', 'An AI-powered chatbot to answer FAQs related to the project workflow.', 'project_2.png');

--
-- Temporary view structure for view `vpeoplefavouritecolurs`
--

DROP TABLE IF EXISTS `vpeoplefavouritecolurs`;
/*!50001 DROP VIEW IF EXISTS `vpeoplefavouritecolurs`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vpeoplefavouritecolurs` AS SELECT 
 1 AS `PersonId`,
 1 AS `Firstname`,
 1 AS `Lastname`,
 1 AS `Colou`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'get_into_tech_c2_2025_v2'
--
/*!50003 DROP PROCEDURE IF EXISTS `pGetAllPeople` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `pGetAllPeople`()
BEGIN
    SELECT *  FROM person;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `vpeoplefavouritecolurs`
--

/*!50001 DROP VIEW IF EXISTS `vpeoplefavouritecolurs`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vpeoplefavouritecolurs` AS select `p`.`PersonID` AS `PersonId`,`p`.`Firstname` AS `Firstname`,`p`.`Lastname` AS `Lastname`,`c`.`Name` AS `Colou` from (`person` `p` join `colour` `c` on((`p`.`ColourID` = `c`.`ColourID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-08 18:45:59
