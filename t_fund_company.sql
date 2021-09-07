/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50735
 Source Host           : localhost:3306
 Source Schema         : fund_data

 Target Server Type    : MySQL
 Target Server Version : 50735
 File Encoding         : 65001

 Date: 07/09/2021 21:55:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_fund_company
-- ----------------------------
DROP TABLE IF EXISTS `t_fund_company`;
CREATE TABLE `t_fund_company`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `company_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '公司名称',
  `code` int(8) UNSIGNED ZEROFILL NOT NULL DEFAULT 00000000 COMMENT '公司代码',
  `of_num` int(4) NOT NULL COMMENT '开放基金数',
  `cf_num` int(4) NOT NULL DEFAULT 0 COMMENT '封闭基金数',
  `total_num` int(4) NOT NULL DEFAULT 0 COMMENT '总基金数',
  `share_open` decimal(8, 2) NOT NULL DEFAULT 0.00 COMMENT '开放基金份额',
  `share_close` decimal(8, 2) NOT NULL DEFAULT 0.00 COMMENT '封闭基金份额',
  `share_total` decimal(8, 2) NOT NULL DEFAULT 0.00 COMMENT '总基金份额',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `company_name`(`company_name`) USING BTREE,
  INDEX `code`(`code`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_fund_company_manager
-- ----------------------------
DROP TABLE IF EXISTS `t_fund_company_manager`;
CREATE TABLE `t_fund_company_manager`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `company_id` int(10) UNSIGNED NOT NULL,
  `manager_id` int(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_fund_info
-- ----------------------------
DROP TABLE IF EXISTS `t_fund_info`;
CREATE TABLE `t_fund_info`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_fund_manager
-- ----------------------------
DROP TABLE IF EXISTS `t_fund_manager`;
CREATE TABLE `t_fund_manager`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_fund_manager_info
-- ----------------------------
DROP TABLE IF EXISTS `t_fund_manager_info`;
CREATE TABLE `t_fund_manager_info`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
