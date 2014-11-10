-- phpMyAdmin SQL Dump
-- version 3.5.8.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 09, 2014 at 05:14 PM
-- Server version: 5.5.40-36.1-log
-- PHP Version: 5.4.23

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `miyanki_records`
--

-- --------------------------------------------------------

--
-- Table structure for table `belongs_to_wishlist`
--

DROP TABLE IF EXISTS `belongs_to_wishlist`;
CREATE TABLE IF NOT EXISTS `belongs_to_wishlist` (
  `v_id` int(10) NOT NULL,
  `username` varchar(10) NOT NULL,
  `title` varchar(500) NOT NULL,
  PRIMARY KEY (`v_id`,`username`,`title`),
  KEY `username` (`username`),
  KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `described_by`
--

DROP TABLE IF EXISTS `described_by`;
CREATE TABLE IF NOT EXISTS `described_by` (
  `v_id` int(11) NOT NULL,
  `o_id` int(11) NOT NULL,
  PRIMARY KEY (`v_id`,`o_id`),
  KEY `o_id` (`o_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `owned_vinyl`
--

DROP TABLE IF EXISTS `owned_vinyl`;
CREATE TABLE IF NOT EXISTS `owned_vinyl` (
  `o_id` int(11) NOT NULL AUTO_INCREMENT,
  `quality` varchar(30) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `tradable` tinyint(1) NOT NULL,
  `sellable` tinyint(1) NOT NULL,
  `username` varchar(10) NOT NULL,
  PRIMARY KEY (`o_id`),
  KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
CREATE TABLE IF NOT EXISTS `records` (
  `v_id` int(10) NOT NULL AUTO_INCREMENT,
  `artist` varchar(500) NOT NULL,
  `tracklist` varchar(5000) DEFAULT NULL,
  `genre` varchar(500) DEFAULT NULL,
  `album` varchar(500) NOT NULL,
  `rarity` double NOT NULL,
  `art` varchar(500) DEFAULT NULL,
  `year` int(4) NOT NULL,
  PRIMARY KEY (`v_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `username` varchar(10) NOT NULL,
  `password` varchar(30) NOT NULL,
  `name` varchar(500) DEFAULT NULL,
  `picture` varchar(500) DEFAULT NULL,
  `email` varchar(500) DEFAULT NULL,
  `zipcode` int(5) unsigned DEFAULT NULL,
  `city` varchar(500) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL,
  `street` varchar(500) DEFAULT NULL,
  `rarity` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `wishlist`
--

DROP TABLE IF EXISTS `wishlist`;
CREATE TABLE IF NOT EXISTS `wishlist` (
  `title` varchar(500) NOT NULL,
  `username` varchar(10) NOT NULL,
  PRIMARY KEY (`title`,`username`),
  KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `belongs_to_wishlist`
--
ALTER TABLE `belongs_to_wishlist`
  ADD CONSTRAINT `belongs_to_wishlist_ibfk_3` FOREIGN KEY (`v_id`) REFERENCES `records` (`v_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `belongs_to_wishlist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `wishlist` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `belongs_to_wishlist_ibfk_2` FOREIGN KEY (`title`) REFERENCES `wishlist` (`title`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `described_by`
--
ALTER TABLE `described_by`
  ADD CONSTRAINT `described_by_ibfk_3` FOREIGN KEY (`o_id`) REFERENCES `owned_vinyl` (`o_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `described_by_ibfk_1` FOREIGN KEY (`v_id`) REFERENCES `records` (`v_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `owned_vinyl`
--
ALTER TABLE `owned_vinyl`
  ADD CONSTRAINT `owned_vinyl_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `wishlist`
--
ALTER TABLE `wishlist`
  ADD CONSTRAINT `wishlist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
