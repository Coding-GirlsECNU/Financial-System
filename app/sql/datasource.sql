/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : PostgreSQL
 Source Server Version : 160001 (160001)
 Source Host           : localhost:5433
 Source Catalog        : al
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 160001 (160001)
 File Encoding         : 65001

 Date: 28/01/2024 23:54:08
*/


-- ----------------------------
-- Table structure for datasource
-- ----------------------------
DROP TABLE IF EXISTS "public"."datasource";
CREATE TABLE "public"."datasource" (
  "datasourceid" int4 NOT NULL DEFAULT nextval('datasource_datasourceid_seq'::regclass),
  "config" json NOT NULL
)
;

-- ----------------------------
-- Records of datasource
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table datasource
-- ----------------------------
ALTER TABLE "public"."datasource" ADD CONSTRAINT "datasource_pkey" PRIMARY KEY ("datasourceid");
