CREATE DATABASE `pet_adoption_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `pets` (
  `pet_id` int NOT NULL AUTO_INCREMENT,
  `pet_name` varchar(50) DEFAULT NULL,
  `species` varchar(30) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `adopted` varchar(10) DEFAULT NULL,
  `adoption_fee` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`pet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
