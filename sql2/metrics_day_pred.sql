CREATE TABLE "metrics_day_pred" 
(
    "stock"	VARCHAR(512),
    "model_name"	VARCHAR(512),
    "metrics"	VARCHAR(512),
    "value"	NUMERIC,
    PRIMARY KEY(stock,model_name,metrics)
);

INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601899.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '1.1110891535400684');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601899.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.8091456954554456');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601899.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '0.9137789524065594');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601899.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.729359787198442');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601899.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '0.7502618768034786');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601899.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.656380123658038');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('600519.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '0.7135984762168878');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('600519.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.6453684885469511');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('600519.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '0.812593601651253');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('600519.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.6518315248379977');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('600519.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '0.6103584755080914');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('600519.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.5644481366715992');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601169.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '2.041897446945849');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601169.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '1.0414195411133684');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601169.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '1.3662633187486197');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601169.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.8796815442484873');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601169.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '1.188001833911255');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601169.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.8242831946058394');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002202.XSHE', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '0.5735697398914723');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002202.XSHE', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.5701825212148743');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002202.XSHE', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '0.5327629283558576');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002202.XSHE', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.5717424824236611');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002202.XSHE', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '0.39064135973707464');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002202.XSHE', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.49001515279567504');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601618.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '1.0687072214638191');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601618.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.7736980836072034');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601618.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '0.8314535810210159');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601618.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.6841794959736822');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601618.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '0.705526888957318');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601618.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.6231440571300361');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002236.XSHE', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '1.7236335656481672');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002236.XSHE', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.9853411891745767');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002236.XSHE', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '1.7885088979801467');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002236.XSHE', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.9819212890477588');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002236.XSHE', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '1.3479289512138106');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('002236.XSHE', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.8615120815757975');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601088.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '0.6796808404039086');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601088.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.6340501834013855');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601088.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '0.5727065702752765');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601088.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.569026874302955');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601088.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '0.4476487714071465');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('601088.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.48908424270883466');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000725.XSHE', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '1.058832135902049');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000725.XSHE', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.8018089157811266');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000725.XSHE', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '0.9778230105709367');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000725.XSHE', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.7575846497860524');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000725.XSHE', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '0.854381904543505');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000725.XSHE', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.7261595764152962');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('603993.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '1.0740096916433979');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('603993.XSHG', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.7562411949386276');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('603993.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '0.9001038373467156');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('603993.XSHG', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.7070906241027938');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('603993.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '0.7451803970674367');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('603993.XSHG', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.626968797901468');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000001.XSHE', 'xgboost_2022-01-01_2023-12-31_1_5', 'MSE', '0.8688429613268955');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000001.XSHE', 'xgboost_2022-01-01_2023-12-31_1_5', 'MAE', '0.7035639676386657');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000001.XSHE', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MSE', '0.6973153253621812');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000001.XSHE', 'LinearRegression_2022-01-01_2023-12-31_1_5', 'MAE', '0.637760127175096');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000001.XSHE', 'VAR_2022-01-01_2023-12-31_1_5', 'MSE', '0.5646199062842882');
INSERT INTO "metrics_day_pred" ("stock", "model_name", "metrics", "value") VALUES ('000001.XSHE', 'VAR_2022-01-01_2023-12-31_1_5', 'MAE', '0.567829855831785');
