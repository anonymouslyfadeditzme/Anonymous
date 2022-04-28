CREATE DATABASE `lpg_booking` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
SELECT * FROM lpg_booking.booking;CREATE TABLE `booking` (
  `ConsumerID` int NOT NULL,
  `BookingDate` varchar(45) DEFAULT NULL,
  `DeliveryDate` varchar(45) DEFAULT NULL,
  `BookingType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ConsumerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `customer` (
  `ConsumerID` int NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `IDNumber` varchar(45) DEFAULT NULL,
  `IDProof` varchar(45) DEFAULT NULL,
  `MothersName` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Mobile` varchar(45) DEFAULT NULL,
  `AltMobile` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Nationality` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ConsumerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
