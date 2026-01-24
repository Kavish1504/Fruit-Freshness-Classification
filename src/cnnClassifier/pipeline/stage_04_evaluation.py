from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation import Evaluation
from src.cnnClassifier import logger

STAGE_NAME="Evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        val_config=config.get_validation_config()
        obj=Evaluation(config=val_config)
        obj.evaluation()
        obj.save_score()

if __name__=="__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} started")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
