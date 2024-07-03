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

 Date: 28/01/2024 23:53:55
*/


-- ----------------------------
-- Table structure for dashboard
-- ----------------------------
DROP TABLE IF EXISTS "public"."dashboard";
CREATE TABLE "public"."dashboard" (
  "dashboardid" int4 NOT NULL DEFAULT nextval('dashboard_dashboardid_seq'::regclass),
  "charts" json,
  "layout" json,
  "dashboard_name" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of dashboard
-- ----------------------------
INSERT INTO "public"."dashboard" VALUES (2, '[{"dataset": 
{"example_row": {"date": "2016-07-01 00:00:00", "HUFL": "5.827000141143799", "HULL": "2.009000062942505", "MUFL": "1.5989999771118164", "MULL": "0.4620000123977661", "LUFL": "4.203000068664552", "LULL": "1.3400000333786009", "OT": "30.5310001373291"}, 
"query": "select * from test limit 10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "dataset_name": "ETTH1", "datasetid": 10, 
"config": {"host": "127.0.0.1", "port": "5433", "user": "postgres", "password": "zzh0117.", "type": "psql", "database": "al", "query": "select * from test limit 10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n"}},
 "mapping": {"date": ["date"], "X": ["HUFL"], "X_predict": ["HULL"]}, "chartid": 1, "config": {"type": "TSL", "name": "111"}, "key": 1}, {"dataset": {"example_row": {"date": "2016-07-01 00:00:00", "HUFL": "5.827000141143799", "HULL": "2.009000062942505", "MUFL": "1.5989999771118164", "MULL": "0.4620000123977661", "LUFL": "4.203000068664552", "LULL": "1.3400000333786009", "OT": "30.5310001373291"}, "query": "select * from test limit 10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "dataset_name": "ETTH1", "datasetid": 10, "config": {"host": "127.0.0.1", "port": "5433", "user": "postgres", "password": "zzh0117.", "type": "psql", "database": "al", "query": "select * from test limit 10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n"}}, "mapping": {"date": ["date"], "X": ["HUFL"], "X_predict": ["HULL"]}, "chartid": 1, "config": {"type": "TSL", "name": "111"}, "key": 1}]', '[["0", "0"], []]', '222');

-- ----------------------------
-- Primary Key structure for table dashboard
-- ----------------------------
ALTER TABLE "public"."dashboard" ADD CONSTRAINT "dashboard_pkey" PRIMARY KEY ("dashboardid");
