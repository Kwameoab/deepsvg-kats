from .default_icons import *


class ModelConfig(Hierarchical):
    def __init__(self):
        super().__init__()

        self.label_condition = False
        self.use_vae = True


class Config(Config):
    def __init__(self, num_gpus=2):
        super().__init__(num_gpus=num_gpus)

        self.model_cfg = ModelConfig()
        self.model_args = self.model_cfg.get_model_args()

        # No labels used 
        self.filter_category = None

        # Optimization
        self.learning_rate = 1e-3 * num_gpus
        self.batch_size = 128
        self.grad_clip = 1.0

        self.max_num_groups = 25 # Nubmer of paths (N_P)
        self.max_seq_len = 100 # Max allowed commands per path (N_C)

        # Concatenated sequence length for baselines
        self.max_total_len = self.max_num_groups * self.max_seq_len 

        self.self_match = False # Use Hungarian (self-match) or Ordered assignment

