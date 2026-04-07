-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 07, 2026 at 05:48 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `shop_city`
--

CREATE TABLE `shop_city` (
  `ctid` int(11) NOT NULL,
  `ctname` varchar(100) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shop_consumers`
--

CREATE TABLE `shop_consumers` (
  `customerid` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `mobile` bigint(20) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shop_contactus`
--

CREATE TABLE `shop_contactus` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `comment` text DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shop_contactus`
--

INSERT INTO `shop_contactus` (`id`, `name`, `email`, `phone`, `comment`, `created_at`) VALUES
(1, 'brijesh', 'brijesh@gmail.com', 9998003879, 'hi i am brijesh', '2026-04-02 09:48:00');

-- --------------------------------------------------------

--
-- Table structure for table `shop_country`
--

CREATE TABLE `shop_country` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `population` bigint(20) DEFAULT NULL,
  `area` float DEFAULT NULL,
  `capital` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shop_country`
--

INSERT INTO `shop_country` (`id`, `name`, `population`, `area`, `capital`) VALUES
(1, 'india', 1500000000, 85465900, 'Delhi'),
(2, 'USA', 8500000, 565837, 'California');

-- --------------------------------------------------------

--
-- Table structure for table `shop_crediters`
--

CREATE TABLE `shop_crediters` (
  `supplierid` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `gstno` varchar(255) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shop_department`
--

CREATE TABLE `shop_department` (
  `depid` int(11) NOT NULL,
  `depname` varchar(255) DEFAULT NULL,
  `roomno` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shop_employees`
--

CREATE TABLE `shop_employees` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shop_orders`
--

CREATE TABLE `shop_orders` (
  `oid` int(11) NOT NULL,
  `productname` varchar(100) DEFAULT NULL,
  `orderdate` date DEFAULT NULL,
  `ordercode` varchar(255) DEFAULT NULL,
  `customername` varchar(255) DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shop_products`
--

CREATE TABLE `shop_products` (
  `pid` int(11) NOT NULL,
  `productimage` varchar(255) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `oldprice` float DEFAULT NULL,
  `newprice` float DEFAULT NULL,
  `weight` varchar(255) DEFAULT NULL,
  `color` varchar(100) DEFAULT NULL,
  `materials` varchar(100) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `descriptions` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shop_state`
--

CREATE TABLE `shop_state` (
  `sid` int(11) NOT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `shop_city`
--
ALTER TABLE `shop_city`
  ADD PRIMARY KEY (`ctid`);

--
-- Indexes for table `shop_consumers`
--
ALTER TABLE `shop_consumers`
  ADD PRIMARY KEY (`customerid`);

--
-- Indexes for table `shop_contactus`
--
ALTER TABLE `shop_contactus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shop_country`
--
ALTER TABLE `shop_country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shop_crediters`
--
ALTER TABLE `shop_crediters`
  ADD PRIMARY KEY (`supplierid`);

--
-- Indexes for table `shop_department`
--
ALTER TABLE `shop_department`
  ADD PRIMARY KEY (`depid`);

--
-- Indexes for table `shop_orders`
--
ALTER TABLE `shop_orders`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `shop_products`
--
ALTER TABLE `shop_products`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `shop_state`
--
ALTER TABLE `shop_state`
  ADD PRIMARY KEY (`sid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `shop_city`
--
ALTER TABLE `shop_city`
  MODIFY `ctid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shop_consumers`
--
ALTER TABLE `shop_consumers`
  MODIFY `customerid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shop_contactus`
--
ALTER TABLE `shop_contactus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `shop_country`
--
ALTER TABLE `shop_country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `shop_crediters`
--
ALTER TABLE `shop_crediters`
  MODIFY `supplierid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shop_department`
--
ALTER TABLE `shop_department`
  MODIFY `depid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shop_orders`
--
ALTER TABLE `shop_orders`
  MODIFY `oid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shop_products`
--
ALTER TABLE `shop_products`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shop_state`
--
ALTER TABLE `shop_state`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
