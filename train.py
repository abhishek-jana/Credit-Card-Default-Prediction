from credit_default.pipeline.training import TrainingPipeline
from credit_default.config.pipeline.training import CreditConfig
# from dotenv import load_dotenv
# load_dotenv()

if __name__=="__main__":
    training_pipeline_config= CreditConfig()
    training_pipeline = TrainingPipeline(credit_config=training_pipeline_config)
    training_pipeline.start()

