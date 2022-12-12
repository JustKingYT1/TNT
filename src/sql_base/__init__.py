from .db_tv_channels import BaseWorker
from . import models
from settings import BASE_PATH

base_worker = BaseWorker(base_path=BASE_PATH)

