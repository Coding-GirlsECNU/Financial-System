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

 Date: 28/01/2024 23:54:14
*/


-- ----------------------------
-- Table structure for model
-- ----------------------------
DROP TABLE IF EXISTS "public"."model";
CREATE TABLE "public"."model" (
  "id" int4 NOT NULL DEFAULT nextval('model_id_seq'::regclass),
  "model_name" varchar(255) COLLATE "pg_catalog"."default",
  "model_config1" json
)
;

-- ----------------------------
-- Records of model
-- ----------------------------
INSERT INTO "public"."model" VALUES (1, 'triformer', '{
    "model": "PA",
    "data": "ETTh1",
    "root_path": "./data/ETT/",
    "data_path": "ETTh1.csv",
    "features": "M",
    "target": "OT",
    "freq": "h",
    "seq_len": 24,
    "label_len": 48,
    "pred_len": 24,
    "enc_in": 7,
    "dec_in": 7,
    "c_out": 7,
    "d_model": 512,
    "n_heads": 8,
    "e_layers": 2,
    "d_layers": 1,
    "s_layers": [
        3,
        2,
        1
    ],
    "d_ff": 2048,
    "factor": 5,
    "padding": 0,
    "distil": true,
    "dropout": 0.05,
    "attn": "prob",
    "embed": "timeF",
    "activation": "gelu",
    "output_attention": false,
    "do_predict": false,
    "mix": true,
    "cols": "None",
    "num_workers": 0,
    "itr": 2,
    "train_epochs": 6,
    "batch_size": 32,
    "patience": 3,
    "learning_rate": 0.0001,
    "des": "test",
    "loss": "mse",
    "lradj": "type1",
    "use_amp": false,
    "inverse": false,
    "use_gpu": true,
    "use_multi_gpu": false,
    "devices": "0,1",
    "detail_freq": "h",
    "input": [
        {
            "value": "date",
            "label": "x",
            "type": "select",
            "desc": "横坐标,用于表示时序"
        },
        {
            "value": "X",
            "label": "y_true",
            "type": "select",
            "desc": "纵坐标,用于表示实际值"
        }
    ],
    "example": {
        "type": "TSL",
        "dataset": {
            "config": {
                "host": "127.0.0.1",
                "port": "5433",
                "user": "postgres",
                "password": "zzh0117.",
                "type": "psql",
                "database": "al",
                "query": "\nselect * from test;\n\n\n\n\n\n\n\n\n\n\n\n\n"
            }
        },
        "mapping": {
            "X_predict":["y_pred"],
            "X":["y"],
            "date":["time"]
        }
    }
}
');

-- ----------------------------
-- Primary Key structure for table model
-- ----------------------------
ALTER TABLE "public"."model" ADD CONSTRAINT "model_pkey" PRIMARY KEY ("id");
