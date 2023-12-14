from credit_default.exception import CreditException
from credit_default.logging import logger
from credit_default.config.pipeline.training import CreditConfig
from credit_default.component.training.data_ingesion import DataIngestion
from credit_default.entity.artifact_entity import DataIngestionArtifact
import sys


class TrainingPipeline:

    def __init__(self, credit_config: CreditConfig):
        self.credit_config: CreditConfig = credit_config

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = self.credit_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            raise CreditException(e, sys)


    def start(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise CreditException(e, sys)