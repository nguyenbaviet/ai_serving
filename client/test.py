from ai_serving.client import AIClient, AIRedisService, AIRedisService
import time
import random
import numpy as np

class AIModel(AIRedisService):

    def get_model(self, ip, port, port_out):
        return AIClient(ip=ip, port=port, port_out=port_out, check_version=False)

    def do_work(self, model, logger):
        try:
            start=time.time()
            result = model.encode('Hello world 12345')
            end=time.time()
            response_time = end-start
          
            logger.info('response time: {:.03f}\tresult: {}'.format(response_time, result))

            time.sleep(random.randint(1, 4))

        except Exception as e:
            logger.error('error: {}'.format(e))

    def off_model(self, model):
        model.close()

if __name__ == "__main__":
    from ai_serving.client.helper import get_args_parser
    args = get_args_parser().parse_args(['-port', '12100',
                                        '-port_out', '12102',
                                        '-num_client', '5',
                                        '-remote_servers', '[["localhost", 8066, 8068]]',
                                        '-log_dir', '/data'])
    handler = AIRedisServer(AIModel, args)
    handler.start()