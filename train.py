from credit_default.pipeline.training_pipeline import TrainingPipeline
from credit_default.entity.config_entity import TrainingPipelineConfig

if __name__=="__main__":
    training_config= TrainingPipelineConfig()
    training_pipeline = TrainingPipeline(training_config=training_config)
    training_pipeline.start()
