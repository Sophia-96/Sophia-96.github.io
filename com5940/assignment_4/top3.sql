-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 08, 2020 at 10:40 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assignment_4`
--

-- --------------------------------------------------------

--
-- Table structure for table `top3`
--

CREATE TABLE `top3` (
  `Ranking` int(1) DEFAULT NULL,
  `Name` varchar(39) DEFAULT NULL,
  `Nat` varchar(2) DEFAULT NULL,
  `SP` decimal(4,2) DEFAULT NULL,
  `FS` decimal(5,2) DEFAULT NULL,
  `Total` decimal(5,2) DEFAULT NULL,
  `Pic_url` varchar(85) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `top3`
--

INSERT INTO `top3` (`Ranking`, `Name`, `Nat`, `SP`, `FS`, `Total`, `Pic_url`) VALUES
(1, 'Nathan CHEN', 'US', '99.99', '216.02', '323.42', 'https://dl.airtable.com/.attachments/0768b9f0d792e6f51e31d67e0eb4c1f9/d3f97a53/1.jpg'),
(2, 'Yuzuru HANYU', 'JP', '94.87', '206.10', '300.97', 'https://dl.airtable.com/.attachments/76e052671611f03a5229901d807fe7b1/ecd08783/2.jpeg'),
(3, 'Vincent ZHOU', 'US', '94.17', '186.99', '281.16', 'https://dl.airtable.com/.attachments/1be9328f6bab0d1ca0ae342d2182665f/daa15e6e/3.png'),
(1, 'Alina ZAGITOVA', 'RU', '82.08', '155.42', '237.50', 'https://dl.airtable.com/.attachments/67970464c43d531d26d2357b241e6b36/47aa7b6a/4.jpg'),
(2, 'Elizabet TURSYNBAEVA', 'KZ', '75.96', '148.80', '224.76', 'https://dl.airtable.com/.attachments/b58b049df1fe886ebc0a2b78994ffc8d/f1ffcfd1/5.jpg'),
(3, 'Evgenia MEDVEDEVA', 'RU', '74.23', '149.57', '223.80', 'https://dl.airtable.com/.attachments/e26772e186628302296768ccb781dae7/1e000b88/6.jpg'),
(1, 'Wenjing SUI / Cong HAN', 'CN', '79.24', '155.60', '234.84', 'https://dl.airtable.com/.attachments/e6cf34ba8dc8d5348d3b48dacda68e21/90aa3c7a/7.png'),
(2, 'Evgenia TARASOVA / Vladimir MOROZOV', 'RU', '81.21', '147.26', '228.47', 'https://dl.airtable.com/.attachments/6a889ffef4568021b0bf69792a291a3c/8cb51c0f/8.png'),
(3, 'Natalia ZABIIAKO / Alexander ENBERT', 'RU', '73.96', '144.02', '217.98', 'https://dl.airtable.com/.attachments/4149a216855867fa048c68ff1e582d2e/c22d288f/9.jpg'),
(1, 'Gabriella PAPADAKIS / Guillaume CIZERON', 'FR', '88.42', '134.23', '222.65', 'https://dl.airtable.com/.attachments/182471465e6b218fced65409e9892161/68684f30/10.png'),
(2, 'Victoria SINITSINA / Nikita KATSALAPOV', 'RU', '83.94', '127.82', '211.76', 'https://dl.airtable.com/.attachments/8d6fb9bb875f74cfa0555f3ca6e61319/3effe678/11.png'),
(3, 'Madison HUBBELL / Zachary DONOHUE', 'US', '83.09', '127.31', '210.40', 'https://dl.airtable.com/.attachments/ff736b43d516483f8717ce5dd744550c/290523cf/12.png');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
