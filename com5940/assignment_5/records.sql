-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 21, 2020 at 08:41 AM
-- Server version: 5.7.24
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rankings`
--

-- --------------------------------------------------------

--
-- Table structure for table `records`
--

CREATE TABLE `records` (
  `recordID` int(11) NOT NULL,
  `Name` varchar(44) NOT NULL,
  `Ranking` int(11) NOT NULL,
  `Nation` varchar(2) NOT NULL,
  `SP` decimal(5,2) NOT NULL,
  `FS` decimal(6,2) NOT NULL,
  `Total` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `records`
--

INSERT INTO `records` (`recordID`, `Name`, `Ranking`, `Nation`, `SP`, `FS`, `Total`) VALUES
(1, 'Nathan CHEN', 1, 'US', '107.40', '216.02', '323.42'),
(2, 'Yuzuru HANYU', 2, 'JP', '94.87', '206.10', '300.97'),
(3, 'Vincent ZHOU', 3, 'US', '94.17', '186.99', '281.16'),
(4, 'Shoma UNO', 4, 'JP', '91.40', '178.92', '270.32'),
(5, 'Boyang JIN', 5, 'CN', '84.26', '178.45', '262.71'),
(6, 'Mikhail KOLYADA', 6, 'RU', '84.23', '178.21', '262.44'),
(7, 'Matteo RIZZO', 7, 'IT', '93.37', '164.29', '257.66'),
(8, 'Michal BREZINA', 8, 'CZ', '86.96', '167.32', '254.28'),
(9, 'Jason BROWN', 9, 'US', '96.81', '157.34', '254.15'),
(10, 'Andrei LAZUKIN', 10, 'RU', '84.05', '164.69', '248.74'),
(11, 'Alina ZAGITOVA', 1, 'RU', '82.08', '155.42', '237.50'),
(12, 'Elizabet TURSYNBAEVA', 2, 'KZ', '75.96', '148.80', '224.76'),
(13, 'Evgenia MEDVEDEVA', 3, 'RU', '74.23', '149.57', '223.80'),
(14, 'Rika KIHIRA', 4, 'JP', '70.90', '152.59', '223.49'),
(15, 'Kaori SAKAMOTO', 5, 'JP', '76.86', '145.97', '222.83'),
(16, 'Satoko MIYAHARA', 6, 'JP', '70.60', '145.35', '215.95'),
(17, 'Bradie TENNELL', 7, 'US', '69.50', '143.97', '213.47'),
(18, 'Sofia SAMODUROVA', 8, 'RU', '70.42', '138.16', '208.58'),
(19, 'Mariah BELL', 9, 'US', '71.26', '136.81', '208.07'),
(20, 'Eunsoo LIM', 10, 'KR', '72.91', '132.66', '205.57'),
(21, 'Wenjing SUI / Cong HAN', 1, 'CN', '79.24', '155.60', '234.84'),
(22, 'Evgenia TARASOVA / Vladimir MOROZOV', 2, 'RU', '81.21', '147.26', '228.47'),
(23, 'Natalia ZABIIAKO / Alexander ENBERT', 3, 'RU', '73.96', '144.02', '217.98'),
(24, 'Cheng PENG / Yang JIN', 4, 'CN', '75.51', '140.33', '215.84'),
(25, 'Vanessa JAMES / Morgan CIPRES', 5, 'FR', '68.67', '146.52', '215.19'),
(26, 'Aleksandra BOIKOVA / Dmitrii KOZLOVSKII', 6, 'RU', '69.99', '140.31', '210.30'),
(27, 'Kirsten MOORE-TOWERS / Michael MARINARO', 7, 'CA', '73.08', '126.94', '200.02'),
(28, 'Nicole DELLA MONICA / Matteo GUARISE', 8, 'IT', '67.29', '128.45', '195.74'),
(29, 'Ashley CAIN / Timothy LEDUC', 9, 'US', '66.93', '126.88', '193.81'),
(30, 'Miriam ZIEGLER / Severin KIEFER', 10, 'AT', '63.65', '115.01', '178.66'),
(31, 'Gabriella PAPADAKIS / Guillaume CIZERON', 1, 'FR', '88.42', '134.23', '222.65'),
(32, 'Victoria SINITSINA / Nikita KATSALAPOV', 2, 'RU', '83.94', '127.82', '211.76'),
(33, 'Madison HUBBELL / Zachary DONOHUE', 3, 'US', '83.09', '127.31', '210.40'),
(34, 'Alexandra STEPANOVA / Ivan BUKIN', 4, 'RU', '83.10', '125.42', '208.52'),
(35, 'Kaitlyn WEAVER / Andrew POJE', 5, 'CA', '82.84', '122.78', '205.62'),
(36, 'Madison CHOCK / Evan BATES', 6, 'US', '82.32', '122.60', '204.92'),
(37, 'Piper GILLES / Paul POIRIER', 7, 'CA', '80.44', '120.48', '200.92'),
(38, 'Charlene GUIGNARD / Marco FABBRI', 8, 'IT', '81.66', '117.52', '199.18'),
(39, 'Kaitlin HAWAYEK / Jean-Luc BAKER', 9, 'US', '75.90', '113.16', '189.06'),
(40, 'Laurence FOURNIER BEAUDRY / Nikolaj SORENSEN', 10, 'CA', '74.76', '113.34', '188.10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `records`
--
ALTER TABLE `records`
  ADD PRIMARY KEY (`recordID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `records`
--
ALTER TABLE `records`
  MODIFY `recordID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
