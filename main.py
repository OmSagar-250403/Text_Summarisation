from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger

def execute_stage(stage_name, pipeline):
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        pipeline.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

stages = [
    {"name": "Data Ingestion stage", "pipeline": DataIngestionTrainingPipeline},
    {"name": "Data Validation stage", "pipeline": DataValidationTrainingPipeline},
    {"name": "Data Transformation stage", "pipeline": DataTransformationTrainingPipeline},
    {"name": "Model Trainer stage", "pipeline": ModelTrainerTrainingPipeline},
    {"name": "Model Evaluation stage", "pipeline": ModelEvaluationTrainingPipeline}
]

for stage in stages:
    execute_stage(stage["name"], stage["pipeline"]())