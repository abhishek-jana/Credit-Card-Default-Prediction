import os
from credit_default.constant.training_pipeline.data_ingesion import *
from credit_default.constant.training_pipeline.data_validation import *
from credit_default.constant.training_pipeline.data_transformation import *
from credit_default.constant.training_pipeline.model_evaluation import *
from credit_default.constant.training_pipeline.model_trainer import *
from credit_default.constant.training_pipeline.model_pusher import *

TARGET_COLUMN = ""

PIPELINE_NAME = "credit_default"
ARTIFACT_DIR = "artifact"

# Common filename

FILE_NAME: str = "UCI_Credit_Card.csv"

TRAIN_FILE_NAME: str = "train.csv"

TEST_FILE_NAME: str = "test.csv"

PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"

MODEL_FILE_NAME = "model.pkl"

SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

SCHEMA_DROP_COLS = "drop_columns"

SCHEMA_TARGET_COL = "target_column"