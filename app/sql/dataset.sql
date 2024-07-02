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

 Date: 28/01/2024 23:54:02
*/


-- ----------------------------
-- Table structure for dataset
-- ----------------------------
DROP TABLE IF EXISTS "public"."dataset";
CREATE TABLE "public"."dataset" (
  "datasetid" int4 NOT NULL DEFAULT nextval('dataset_datasetid_seq'::regclass),
  "query" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "example_row" json NOT NULL,
  "config" json,
  "dataset_name" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of dataset
-- ----------------------------
INSERT INTO "public"."dataset" VALUES (10, 'select * from test limit 10;













', '{"date": "2016-07-01 00:00:00", "HUFL": "5.827000141143799", "HULL": "2.009000062942505", "MUFL": "1.5989999771118164", "MULL": "0.4620000123977661", "LUFL": "4.203000068664552", "LULL": "1.3400000333786009", "OT": "30.5310001373291"}', '{"host": "127.0.0.1", "port": "5433", "user": "postgres", "password": "zzh0117.", "type": "psql", "database": "al", "query": "select * from test limit 10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n"}', 'ETTH1');

-- ----------------------------
-- Primary Key structure for table dataset
-- ----------------------------
ALTER TABLE "public"."dataset" ADD CONSTRAINT "dataset_pkey" PRIMARY KEY ("datasetid");
