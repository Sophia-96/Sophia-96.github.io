-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 02, 2020 at 03:04 PM
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
-- Database: `assignment_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `dance_table`
--

CREATE TABLE `dance_table` (
  `Ranking` int(11) NOT NULL,
  `Name` varchar(44) NOT NULL,
  `Nat` varchar(2) NOT NULL,
  `SP` decimal(5,2) NOT NULL,
  `FS` decimal(6,2) NOT NULL,
  `Total` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dance_table`
--

INSERT INTO `dance_table` (`Ranking`, `Name`, `Nat`, `SP`, `FS`, `Total`) VALUES
(1, 'Gabriella PAPADAKIS / Guillaume CIZERON', 'FR', '88.42', '134.23', '222.65'),
(2, 'Victoria SINITSINA / Nikita KATSALAPOV', 'RU', '83.94', '127.82', '211.76'),
(3, 'Madison HUBBELL / Zachary DONOHUE', 'US', '83.09', '127.31', '210.40'),
(4, 'Alexandra STEPANOVA / Ivan BUKIN', 'RU', '83.10', '125.42', '208.52'),
(5, 'Kaitlyn WEAVER / Andrew POJE', 'CA', '82.84', '122.78', '205.62'),
(6, 'Madison CHOCK / Evan BATES', 'US', '82.32', '122.60', '204.92'),
(7, 'Piper GILLES / Paul POIRIER', 'CA', '80.44', '120.48', '200.92'),
(8, 'Charlene GUIGNARD / Marco FABBRI', 'IT', '81.66', '117.52', '199.18'),
(9, 'Kaitlin HAWAYEK / Jean-Luc BAKER', 'US', '75.90', '113.16', '189.06'),
(10, 'Laurence FOURNIER BEAUDRY / Nikolaj SORENSEN', 'CA', '74.76', '113.34', '188.10');

-- --------------------------------------------------------

--
-- Table structure for table `ladies_table`
--

CREATE TABLE `ladies_table` (
  `Ranking` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Nat` varchar(2) NOT NULL,
  `SP` decimal(5,2) NOT NULL,
  `FS` decimal(6,2) NOT NULL,
  `Total` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ladies_table`
--

INSERT INTO `ladies_table` (`Ranking`, `Name`, `Nat`, `SP`, `FS`, `Total`) VALUES
(1, 'Alina ZAGITOVA', 'RU', '82.08', '155.42', '237.50'),
(2, 'Elizabet TURSYNBAEVA', 'KZ', '75.96', '148.80', '224.76'),
(3, 'Evgenia MEDVEDEVA', 'RU', '74.23', '149.57', '223.80'),
(4, 'Rika KIHIRA', 'JP', '70.90', '152.59', '223.49'),
(5, 'Kaori SAKAMOTO', 'JP', '76.86', '145.97', '222.83'),
(6, 'Satoko MIYAHARA', 'JP', '70.60', '145.35', '215.95'),
(7, 'Bradie TENNELL', 'US', '69.50', '143.97', '213.47'),
(8, 'Sofia SAMODUROVA', 'RU', '70.42', '138.16', '208.58'),
(9, 'Mariah BELL', 'US', '71.26', '136.81', '208.07'),
(10, 'Eunsoo LIM', 'KR', '72.91', '132.66', '205.57');

-- --------------------------------------------------------

--
-- Table structure for table `men_table`
--

CREATE TABLE `men_table` (
  `Ranking` int(11) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Nat` varchar(2) NOT NULL,
  `SP` decimal(5,2) NOT NULL,
  `FS` decimal(6,2) NOT NULL,
  `Total` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `men_table`
--

INSERT INTO `men_table` (`Ranking`, `Name`, `Nat`, `SP`, `FS`, `Total`) VALUES
(1, 'Nathan CHEN', 'US', '107.40', '216.02', '323.42'),
(2, 'Yuzuru HANYU', 'JP', '94.87', '206.10', '300.97'),
(3, 'Vincent ZHOU', 'US', '94.17', '186.99', '281.16'),
(4, 'Shoma UNO', 'JP', '91.40', '178.92', '270.32'),
(5, 'Boyang JIN', 'CN', '84.26', '178.45', '262.71'),
(6, 'Mikhail KOLYADA', 'RU', '84.23', '178.21', '262.44'),
(7, 'Matteo RIZZO', 'IT', '93.37', '164.29', '257.66'),
(8, 'Michal BREZINA', 'CZ', '86.96', '167.32', '254.28'),
(9, 'Jason BROWN', 'US', '96.81', '157.34', '254.15'),
(10, 'Andrei LAZUKIN', 'RU', '84.05', '164.69', '248.74');

-- --------------------------------------------------------

--
-- Table structure for table `pairs_table`
--

CREATE TABLE `pairs_table` (
  `Ranking` int(11) NOT NULL,
  `Name` varchar(39) NOT NULL,
  `Nat` varchar(2) NOT NULL,
  `SP` decimal(5,2) NOT NULL,
  `FS` decimal(6,2) NOT NULL,
  `Total` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pairs_table`
--

INSERT INTO `pairs_table` (`Ranking`, `Name`, `Nat`, `SP`, `FS`, `Total`) VALUES
(1, 'Wenjing SUI / Cong HAN', 'CN', '79.24', '155.60', '234.84'),
(2, 'Evgenia TARASOVA / Vladimir MOROZOV', 'RU', '81.21', '147.26', '228.47'),
(3, 'Natalia ZABIIAKO / Alexander ENBERT', 'RU', '73.96', '144.02', '217.98'),
(4, 'Cheng PENG / Yang JIN', 'CN', '75.51', '140.33', '215.84'),
(5, 'Vanessa JAMES / Morgan CIPRES', 'FR', '68.67', '146.52', '215.19'),
(6, 'Aleksandra BOIKOVA / Dmitrii KOZLOVSKII', 'RU', '69.99', '140.31', '210.30'),
(7, 'Kirsten MOORE-TOWERS / Michael MARINARO', 'CA', '73.08', '126.94', '200.02'),
(8, 'Nicole DELLA MONICA / Matteo GUARISE', 'IT', '67.29', '128.45', '195.74'),
(9, 'Ashley CAIN / Timothy LEDUC', 'US', '66.93', '126.88', '193.81'),
(10, 'Miriam ZIEGLER / Severin KIEFER', 'AT', '63.65', '115.01', '178.66');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dance_table`
--
ALTER TABLE `dance_table`
  ADD PRIMARY KEY (`Ranking`);

--
-- Indexes for table `ladies_table`
--
ALTER TABLE `ladies_table`
  ADD PRIMARY KEY (`Ranking`);

--
-- Indexes for table `men_table`
--
ALTER TABLE `men_table`
  ADD PRIMARY KEY (`Ranking`);

--
-- Indexes for table `pairs_table`
--
ALTER TABLE `pairs_table`
  ADD PRIMARY KEY (`Ranking`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
