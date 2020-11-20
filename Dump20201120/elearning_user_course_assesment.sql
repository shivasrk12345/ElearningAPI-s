-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: elearning
-- ------------------------------------------------------
-- Server version	8.0.17

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'a844dc8d-e988-11e9-a1c5-54e1ad1fda26:1-150';

--
-- Table structure for table `user_course_assesment`
--

DROP TABLE IF EXISTS `user_course_assesment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_course_assesment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(50) NOT NULL,
  `courseid` varchar(50) NOT NULL,
  `assesmentid` varchar(50) NOT NULL,
  `assesment_score` int(11) NOT NULL,
  `assesment_state` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  KEY `courseid` (`courseid`),
  CONSTRAINT `user_course_assesment_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`),
  CONSTRAINT `user_course_assesment_ibfk_2` FOREIGN KEY (`courseid`) REFERENCES `course` (`courseid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_course_assesment`
--

LOCK TABLES `user_course_assesment` WRITE;
/*!40000 ALTER TABLE `user_course_assesment` DISABLE KEYS */;
INSERT INTO `user_course_assesment` VALUES (1,'14ee','coa101','asg1',50,'finished'),(2,'14ee','coa101','asg2',50,'finished'),(3,'14ee','coa101','asg3',50,'finished'),(4,'14ee','coa101','asg4',50,'finished'),(5,'14ee','dm101','asg1',30,'finished'),(6,'14ee','dm101','asg2',30,'finished'),(7,'14ee','dm101','asg3',30,'finished'),(8,'14ee','dm101','asg4',60,'finished'),(9,'shiva123','dm101','asg1',20,'finished'),(10,'shiva123','dm101','asg2',20,'finished'),(11,'shiva123','dm101','asg3',80,'finished'),(12,'shiva123','dm101','asg4',70,'finished'),(13,'14ee','dm101','asg4',70,'incomplete');
/*!40000 ALTER TABLE `user_course_assesment` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-20 22:45:42
