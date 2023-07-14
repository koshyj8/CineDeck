-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: cinedeck
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `movie_name` varchar(45) NOT NULL,
  `movie_price` varchar(45) DEFAULT NULL,
  `movie_rating` varchar(45) DEFAULT NULL,
  `movie_desc` varchar(500) DEFAULT NULL,
  `movie_poster` varchar(500) DEFAULT NULL,
  `cast` varchar(500) DEFAULT NULL,
  `runtime` varchar(30) DEFAULT NULL,
  `director` varchar(30) DEFAULT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `Languages` varchar(30) DEFAULT NULL,
  `rated` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`movie_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES ('An Action Hero',NULL,'None','It is based on an actor\'s journey in front and behind the lens who promises action and an offbeat sense of humor.','CineDeck\\assets\\An Action Hero.jpg','Ayushmann Khurrana, Rachit Jadoun, Mirabel Stuart','8 min','Anirudh Iyer','Action','N/A','N/A'),('Avatar: The Way of Water',NULL,'None','Jake Sully lives with his newfound family formed on the planet of Pandora. Once a familiar threat returns to finish what was previously started, Jake must work with Neytiri and the army of the Na\'vi race to protect their planet.','CineDeck\\assets\\Avatar: The Way of Water.jpg','Zoe Saldana, Kate Winslet, Sam Worthington','192 min','James Cameron','Action, Adventure, Fantasy','English','PG-13'),('Black Adam',NULL,'6.9/10','Nearly 5,000 years after he was bestowed with the almighty powers of the Egyptian gods-and imprisoned just as quickly-Black Adam (Johnson) is freed from his earthly tomb, ready to unleash his unique form of justice on the modern world.','CineDeck\\assets\\Black Adam.jpg','Dwayne Johnson, Aldis Hodge, Pierce Brosnan','125 min','Jaume Collet-Serra','Action, Adventure, Fantasy','English','PG-13'),('Black Panther: Wakanda Forever',NULL,'7.3/10','The people of Wakanda fight to protect their home from intervening world powers as they mourn the death of King T\'Challa.','CineDeck\\assets\\Black Panther: Wakanda Forever.jpg','Letitia Wright, Lupita Nyong\'o, Danai Gurira','161 min','Ryan Coogler','Action, Adventure, Drama','English, Spanish','PG-13'),('Blonde',NULL,'5.5/10','A fictionalized chronicle of the inner life of Marilyn Monroe.','CineDeck\\assets\\Blonde.jpg','Ana de Armas, Lily Fisher, Julianne Nicholson','167 min','Andrew Dominik','Biography, Drama, Romance','English, Italian','NC-17'),('Bones and All',NULL,'7.3/10','Maren, a young woman, learns how to survive on the margins of society.','CineDeck\\assets\\Bones and All.jpg','Timothée Chalamet, Taylor Russell, Mark Rylance','131 min','Luca Guadagnino','Drama, Horror, Romance','English','R'),('Gold',NULL,'5.4/10','Set against the backdrop of a vast, unique and unforgiving landscape, Gold is a taut thriller about greed and the lengths people will go to secure themselves a fortune. When two drifters travelling through the desert stumble across the biggest gold nugge...','CineDeck\\assets\\Gold.jpg','Zac Efron, Akuol Ngot, Thiik Biar','97 min','Anthony Hayes','Action, Adventure, Thriller','English','R'),('Kooman',NULL,'8.6/10','The story is about a strict police officer who relocates to a hilly village on the Kerala-Tamil Nadu border. Few normal incidents that take place suddenly appear to be abnormal.','CineDeck\\assets\\Kooman.jpg','Asif Ali, Pauly Valsan, Renji Panicker','153 min','Jeethu Joseph','Drama, Mystery, Thriller','Malayalam','N/A'),('Poker Face',NULL,'5.2/10','Crowe plays Jake, a tech billionaire who gathers his childhood friends to his Miami estate for what turns into a high stakes game of poker. Those friends have a love hate relationship with the host, a master game-player/planner, and he has concocted an e...','CineDeck\\assets\\Poker Face.jpg','Russell Crowe, Liam Hemsworth, RZA','94 min','Russell Crowe','Action, Crime, Thriller','English','N/A'),('The Menu',NULL,'7.6/10','A young couple travels to a remote island to eat at an exclusive restaurant where the chef has prepared a lavish menu, with some shocking surprises.','CineDeck\\assets\\The Menu.jpg','Ralph Fiennes, Anya Taylor-Joy, Nicholas Hoult','107 min','Mark Mylod','Comedy, Horror, Thriller','Spanish, English','R'),('Uunchai',NULL,'7.9/10','Three friends take a trek to the Everest Base Camp. A simple trek turns out to be a personal, emotional and spiritual journey as they battle their physical limitations and discover the true meaning of freedom.','CineDeck\\assets\\Uunchai.jpg','Amitabh Bachchan, Anupam Kher, Boman Irani','173 min','Sooraj R. Barjatya','Adventure, Drama','Hindi','N/A'),('Violent Night',NULL,'None','A team of elite mercenaries breaks into a wealthy family compound on Christmas Eve, taking everyone inside hostage. But the team isn\'t prepared for a surprise combatant: Santa Claus is on the grounds, and he\'s about to show why this Nick is no saint.','CineDeck\\assets\\Violent Night.jpg','David Harbour, Beverly D\'Angelo, John Leguizamo','101 min','Tommy Wirkola','Action, Comedy, Crime','English','R');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-01 14:06:46
