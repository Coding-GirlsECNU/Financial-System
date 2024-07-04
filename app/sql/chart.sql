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

 Date: 28/01/2024 23:53:24
*/


-- ----------------------------
-- Table structure for chart
-- ----------------------------
DROP TABLE IF EXISTS "public"."chart";
CREATE TABLE "public"."chart" (
  "chartid" int4 NOT NULL DEFAULT nextval('chart_chartid_seq'::regclass),
  "config" json,
  "dataset" json,
  "mapping" json
)
;

-- ----------------------------
-- Records of chart
-- ----------------------------
INSERT INTO "public"."chart" VALUES (1, '{"type": "TSL", "name": "111"}', '{"example_row": {"date": "2016-07-01 00:00:00", "HUFL": "5.827000141143799", "HULL": "2.009000062942505", "MUFL": "1.5989999771118164", "MULL": "0.4620000123977661", "LUFL": "4.203000068664552", "LULL": "1.3400000333786009", "OT": "30.5310001373291"}, "query": "select * from ETTh1 limit 10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "dataset_name": "ETTH1", "datasetid": 10, "config": {"host": "127.0.0.1", "port": "5433", "user": "postgres", "password": "zzh0117.", "type": "psql", "database": "al", "query": "select * from test limit 10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n"}}', '{"date": ["date"], "X": ["HUFL"], "X_predict": ["HULL"]}');

-- ----------------------------
-- Primary Key structure for table chart
-- ----------------------------
ALTER TABLE "public"."chart" ADD CONSTRAINT "chart_pkey" PRIMARY KEY ("chartid");
