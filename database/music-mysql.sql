CREATE DATABASE MUSIC DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

/*
Navicat MySQL Data Transfer

Source Server         : demo
Source Server Version : 50067
Source Host           : localhost:3306
Source Database       : music

Target Server Type    : MYSQL
Target Server Version : 50067
File Encoding         : 65001

Date: 2017-04-17 14:29:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for music_rank
-- ----------------------------
DROP TABLE IF EXISTS `music_rank`;
CREATE TABLE `music_rank` (
  `UUID` varchar(36) NOT NULL,
  `music_name` varchar(255) default NULL,
  `music_singer` varchar(255) default NULL,
  `music_url_online` varchar(255) default NULL,
  `music_type` varchar(255) default NULL,
  `music_source` varchar(255) default NULL,
  `create_time` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`UUID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for music_record
-- ----------------------------
DROP TABLE IF EXISTS `music_record`;
CREATE TABLE `music_record` (
  `UUID` varchar(36) NOT NULL,
  `music_name` varchar(255) default NULL,
  `music_singer` varchar(255) default NULL,
  `music_album` varchar(255) default NULL,
  `music_url_online` varchar(255) default NULL,
  `music_url_download` varchar(255) default NULL,
  `music_desc` varchar(255) default NULL,
  `create_time` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  PRIMARY KEY  (`UUID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for music_records
-- ----------------------------
DROP TABLE IF EXISTS `music_records`;
CREATE TABLE `music_records` (
  `uuid` varchar(36) NOT NULL,
  `music_name` varchar(255) default NULL,
  `music_singer` varchar(255) default NULL,
  `music_album` varchar(255) default NULL,
  `music_desc` varchar(255) default NULL,
  `music_url_online` varchar(255) default NULL,
  `music_url_download` varchar(255) default NULL,
  `music_type` varchar(255) default NULL,
  `music_source` varchar(255) default NULL,
  `create_time` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  PRIMARY KEY  (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for music_url_unuse
-- ----------------------------
DROP TABLE IF EXISTS `music_url_unuse`;
CREATE TABLE `music_url_unuse` (
  `uuid` varchar(36) NOT NULL,
  `music_url` varchar(255) default NULL,
  `url_name` varchar(255) default NULL,
  PRIMARY KEY  (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for music_url_used
-- ----------------------------
DROP TABLE IF EXISTS `music_url_used`;
CREATE TABLE `music_url_used` (
  `uuid` varchar(36) NOT NULL,
  `music_url` varchar(255) default NULL,
  PRIMARY KEY  (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
